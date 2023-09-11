#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import concurrent.futures
import logging
import os
import shutil
import sys
import time
import numpy as np
import pandas as pd
from SQL_FOLDER import fetch_data
from Files import write
from Private import stores_sensitive_info
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

OneDrive = stores_sensitive_info.OneDrivePath
path = f"{OneDrive}/Pictures/Wallpaper/in"
path_2 = f"{OneDrive}/Pictures/Wallpaper/roll"
path_3 = f"{OneDrive}/Pictures/Wallpaper/in/OFFLINE"
log_path = f"{os.getcwd()}/std.log"
logging.basicConfig(
    filename=log_path, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s"
)
wp_logger = logging.getLogger()
wp_logger.setLevel("WARNING")
SQL_FILES = [
    "ESFIItemEntry_ESFIItemPeriodics_a.sql",
    "ESFIItemEntry_ESFIItemPeriodics_b.sql",
    "ESFIItemEntry_ESFIItemPeriodics_c.sql",
    "ESFIDocumentTrade_a.sql",
    "ESFIDocumentTrade_b.sql",
    "ESFIItem_a.sql",
    "ESFIItem_b.sql",
    "ESFIPricelistItem_a.sql",
    "ESFIItemEntry_ESFIItemPeriodics_d.sql",
    "IMP_MobileDocumentLines_a.sql",
    "ES00EventLog_a.sql",
]


def delete_all_files_inside_folder(folder: str) -> None:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def filter_data(df):
    """
    Όταν ένας χρήτης έκανε login δύο φορές και στη συνέχεια έκανε logout από το ένα η τελυταία εγγραφή είναι logout αλλά ο χρήστης είναι ακόμα συνδεδεμένος
    έτσι αυτό το φίλτρο φτιάχτηκε για να λύσει αυτό το πρόβλημα.
    :param df:
    :return:
    """
    df["UserID"] = df["UserID"].str.strip()
    df = df.drop_duplicates(subset=["WSID"], keep="first")

    filtered_df_in = df[df.ID == "ESLOGIN"].groupby("UserID").first().reset_index()
    logged = filtered_df_in.UserID.to_list()

    filtered_df_out = (
        df[(df.ID == "ESLOGOUT") & (~(df.UserID.isin(logged)))]
        .groupby("UserID")
        .first()
        .reset_index()
    )

    df = pd.concat([filtered_df_in, filtered_df_out], ignore_index=True)
    return df


def run(temp_file, flag):
    print(f"🟢 DATA @{datetime.now().strftime('%H:%M:%S')} -> ", end="")

    start_ = time.perf_counter()
    today = datetime.now()

    def fetch_data_with_params(sql_file, params=None):
        return fetch_data.get_sql_data(sql_file, params)

    params_1 = {"year": today.year - 11, "month": today.month, "day": today.day}
    params_2 = {"year": today.year, "month": today.month, "day": today.day}
    params_3 = {"year": today.year - 11, "month": today.month}

    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(
                fetch_data_with_params, SQL_FILES[0], params_1
            ): "df_sales_elounda",
            executor.submit(
                fetch_data_with_params, SQL_FILES[1], params_2
            ): "df_sales_elounda_today",
            executor.submit(fetch_data_with_params, SQL_FILES[2], params_3): "df",
            # executor.submit(fetch_data_with_params, SQL_FILES[3]): "customers",
            # executor.submit(fetch_data_with_params, SQL_FILES[4]): "customers_month",
            executor.submit(fetch_data_with_params, SQL_FILES[5]): "price_change",
            executor.submit(fetch_data_with_params, SQL_FILES[6]): "new_product",
            executor.submit(fetch_data_with_params, SQL_FILES[7]): "special_price",
            executor.submit(fetch_data_with_params, SQL_FILES[8]): "customer_prefer",
            executor.submit(fetch_data_with_params, SQL_FILES[9]): "pda",
        }

        results = {}

        for future in concurrent.futures.as_completed(futures):
            df_name = futures[future]
            try:
                results[df_name] = future.result()
            except Exception as exc:
                print(f"%r generated an exception: %s" % (df_name, exc))

    (df_sales_elounda, df_sales_elounda_today, df,
     # customers, customers_month,
     price_change, new_product, special_price, customer_prefer, pda) = (results[key] for key in ["df_sales_elounda", "df_sales_elounda_today", "df",
                                                                                                 # "customers", "customers_month",
                                                                                                 "price_change", "new_product", "special_price", "customer_prefer", "pda"])

    def get_count(temp_df):
        return temp_df.COUNT.iloc[0] if not temp_df.empty else 0

    product_info = {
        "price_change": get_count(price_change),
        "new_product": get_count(new_product),
        "special_price": get_count(special_price),
        "customer_prefer": get_count(customer_prefer),
    }
    # CUSTOMERS
    # max_live_customers = customers.COUNT.max()
    # customers["COLOR"] = customers["COUNT"].apply(
    #     lambda x: "white" if x >= max_live_customers else "#F25E49"
    # )
    #
    # max_live_customers_month = customers_month.COUNT.max()
    # customers_month["COLOR"] = customers_month["COUNT"].apply(
    #     lambda x: "white" if x >= max_live_customers_month else "#F25E49"
    # )

    c = df_sales_elounda

    df["DATE"] = df.apply(
        lambda x: f"{int(x.MONTH)}/{int(x.DAY)}/{int(x.YEAR)}", axis=1
    )
    df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d/%m/%Y")

    status_users_elounda = pd.DataFrame
    status_users_lato = pd.DataFrame

    if flag == "a01":

        def calc(df):
            if df["DIFF"].total_seconds() < 86400:  # less than one day in seconds
                hours = df["DIFF"].seconds // 3600
                minutes = (df["DIFF"].seconds // 60) % 60
                return f"{hours}h.{minutes}m"

            elif df["DIFF"].total_seconds() < 172800:  # less than two days in seconds
                return "1Day"

            else:
                days = df["DIFF"].days
                return f"{days}Days"

        def complete_df(temp_df:pd.DataFrame) -> pd.DataFrame:
            temp_df["COLOR"] = np.where(temp_df["ID"] == "ESLOGOUT", "red", "green")
            temp_df["DIFF"] = today - temp_df["EDate"]
            temp_df["elapsed_time"] = temp_df.apply(lambda row: calc(row), axis=1)
            return temp_df

        elounda_users = tuple(stores_sensitive_info.EM_users)
        lato_users = tuple(stores_sensitive_info.LATO_users)

        em_df = fetch_data.get_sql_data(SQL_FILES[10], None, tuple_data=elounda_users)
        lato_df = fetch_data.get_sql_data(SQL_FILES[10], None, tuple_data=lato_users, connection="2")

        status_users_elounda = complete_df(em_df)
        status_users_elounda = filter_data(status_users_elounda)
        status_users_lato = complete_df(lato_df)
        status_users_lato = filter_data(status_users_lato)

    timed = datetime.now().strftime("%d . %m . %Y   %H : %M : %S")
    print(f"🟢 IMAGE @{datetime.now().strftime('%H:%M:%S')} ", end="")
    write.run(
        c,
        temp_file,
        today,
        path,
        path_2,
        df_sales_elounda_today.values[0][0],
        timed,
        df,
        flag,
        pda,
        product_info,
        status_users_elounda,
        status_users_lato,
        # customers,
        # customers_month,
    )

    stop_ = time.perf_counter()

    return start_, stop_, df_sales_elounda_today.values[0][0]


CRED = "\033[91m"
CBLUE = "\33[34m"
CGREEN = "\033[92m"
CEND = "\033[0m"

times = 0
failed = 0
timers = {"a0": 0, "l": 0, "a01": 0}

calendar_check_today = datetime.now().day
write.create_calendar()
while True:
    if datetime.now().day != calendar_check_today:
        write.create_calendar()
        calendar_check_today = datetime.now().day
    # files = ["a0", "l", "a01"]
    files = ["a0"]
    for file in files:
        delete_all_files_inside_folder(f"{path}/TEMP/")

        HOST_UP = (
            True
            if os.system(
                f"ping -c 1  {stores_sensitive_info.ip.get('EM ROUTER')} >/dev/null"
            )
            == 0
            else False
        )
        try:
            if HOST_UP:
                time.sleep(timers.get(file))
                start, stop, sales = run(file, file)
                sleep_t = (
                    60 - round(stop - start) if 60 - round(stop - start) > 0 else 0
                )
                timers[file] = sleep_t

                times += 1
                print(
                    f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: in {round(stop - start)} sec :: {CBLUE}{sales}€{CEND} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                    end="",
                )
            else:
                write.offline(path, path_2, path_3)
                wp_logger.error("VPN OFFLINE")
                failed += 1
                print(
                    f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                    end="",
                )
        except KeyboardInterrupt:
            write.offline(path, path_2, path_3)
            sys.exit(0)
        except Exception as e:
            print(f"\rException Occured", end="")
            wp_logger.error(e)
            failed += 1
            print(
                f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                end="",
            )
