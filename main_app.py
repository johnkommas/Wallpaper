#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import os
import shutil
import logging
import sys
import concurrent.futures

import numpy as np

from Private import sql_connect, stores_sensitive_info
from Files import sql, plot, write
from datetime import datetime
import pandas as pd
import time
import atexit

path = f"{stores_sensitive_info.OneDrivePath}/Pictures/Wallpaper/in"
path_2 = f"{stores_sensitive_info.OneDrivePath}/Pictures/Wallpaper/roll"
path_3 = f"{stores_sensitive_info.OneDrivePath}/Pictures/Wallpaper/in/OFFLINE"
log_path = f"{os.getcwd()}/std.log"
logging.basicConfig(
    filename=log_path, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s"
)
wp_logger = logging.getLogger()
wp_logger.setLevel("WARNING")


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
    Όταν ένας χρήτης έκανε login δύο φορές και στην συνέχεια έκανε logout από το ένα η τελυταία εγγραφή είναι logout αλλά ο χρήστης είναι ακόμα συνδεδεμένος
    έτσι αυτό το φίλτρο φτιάχτηκε για να λύσει αυτό το πρόβλημα.
    :param df:
    :return:
    """
    df['UserID'] = df['UserID'].str.strip()
    df = df.drop_duplicates(subset=['WSID'], keep='first')

    filtered_df_in = df[df.ID == 'ESLOGIN'].groupby('UserID').first().reset_index()
    logged = filtered_df_in.UserID.to_list()

    filtered_df_out = df[(df.ID == 'ESLOGOUT') & (~(df.UserID.isin(logged)))].groupby('UserID').first().reset_index()

    df = pd.concat([filtered_df_in, filtered_df_out], ignore_index=True)
    return df


def run(file, flag):
    connection = sql_connect.connect()

    start_ = time.perf_counter()
    today = datetime.now()

    # Use a ThreadPoolExecutor to run execute_query_and_get_count in parallel for each query.
    # Moved sql execution to a separate function
    def execute_query(query, connection):
        return pd.read_sql_query(query, connection)

    # Each query and its respective connection are kept as tuple in a list.
    # In case the all queries are to be executed on the same connection, replace `sql_connect.connect()` and `connection` with your preferred connection.
    queries = [
        (
            sql.sales_elounda(today.year - 5, today.month, today.day),
            sql_connect.connect(),
        ),
        (sql.sales_elounda_today(today.year, today.month, today.day), connection),
        (sql.sales_elounda_graph(today.year - 5, today.month), connection),
        (sql.count_customers(), connection),
        (sql.count_customers_month(), connection)
    ]

    # Use a ThreadPoolExecutor to run execute_query in parallel for each query
    with concurrent.futures.ThreadPoolExecutor() as executor:
        dfs = executor.map(lambda query: execute_query(*query), queries)

    df_sales_elounda, df_sales_elounda_today, df, customers, customers_month = dfs

    max_live_customers = customers.COUNT.max()
    customers['COLOR'] = customers['COUNT'].apply(lambda x: 'white' if x >= max_live_customers else 'orange')

    max_live_customers_month = customers_month.COUNT.max()
    customers_month["COLOR"] = customers_month["COUNT"].apply(
        lambda x: "white" if x >= max_live_customers_month else "orange"
    )


    # print(df_best_products_sales_today)
    a = df_sales_elounda.TurnOver[df_sales_elounda.YEAR == today.year].values[0]
    b = df_sales_elounda_today.values[0][0]
    c = df_sales_elounda

    df["DATE"] = df.apply(
        lambda x: f"{int(x.MONTH)}/{int(x.DAY)}/{int(x.YEAR)}", axis=1
    )
    df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d/%m/%Y")

    # Define a function to execute the SQL query and get the count.
    def execute_query_and_get_count(query, connection):
        df = pd.read_sql_query(query, connection)
        return df.COUNT.iloc[0] if not df.empty else 0

    # Define a dictionary to store your queries; Keys will be used as keys in the final dict too.
    queries = {
        "price_change": sql.price_changes_today(),
        "new_product": sql.new_products(),
        "special_price": sql.special_price(),
        "customer_prefer": sql.customer_prefer(),
    }

    # Use a ThreadPoolExecutor to run execute_query_and_get_count in parallel for each query.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        product_info = {
            key: executor.submit(
                execute_query_and_get_count, query, connection
            ).result()
            for key, query in queries.items()
        }

    pda = pd.read_sql_query(sql.pda_alert(), connection)
    status_users_elounda = pd.DataFrame
    status_users_lato = pd.DataFrame
    if flag == "a000":
        # Tree map
        df = pd.read_sql_query(
            sql.quantity_for_tree_map(today.year, today.month), connection
        )
        plot.make_wordcloud(df, path)
        plot.tree_map(df, path)

    elif flag == "a01":
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

        def complete_df(df):
            df['COLOR'] = np.where(df['ID'] == 'ESLOGOUT', 'red', 'green')
            df['DIFF'] = today - df['EDate']
            df['elapsed_time'] = df.apply(lambda row: calc(row), axis=1)
            return df



        elounda_users = tuple(stores_sensitive_info.EM_users)
        lato_users = tuple(stores_sensitive_info.LATO_users)

        status_users_elounda = complete_df(pd.read_sql_query(sql.check_online_user(elounda_users), connection))
        status_users_elounda = filter_data(status_users_elounda)
        status_users_lato = complete_df(pd.read_sql_query(sql.check_online_user(lato_users), sql_connect.connect_lato()))
        status_users_lato = filter_data(status_users_lato)


    timed = datetime.now().strftime("%d . %m . %Y   %H : %M : %S")
    print(" 🟢", end="")
    write.run(
        a,
        b,
        c,
        file,
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
        customers,
        customers_month
    )
    print("🟢", end="")

    # Randar Plot ΕΝΑΡΞΗ
    # df = pd.read_sql_query(sql.randar_query(today.year, today.month), sql_connect.connect())
    # df.dropna(inplace=True)
    # # print(df)
    # categories = df['BRAND'].values
    # sales = df['SALES'].values
    # plot.randar_chart(categories, sales, path)

    stop_ = time.perf_counter()

    return start_, stop_, df_sales_elounda_today.values[0][0]


CRED = "\033[91m"
CBLUE = "\33[34m"
CGREEN = "\033[92m"
CEND = "\033[0m"

times = 0
failed = 0
timers = {"a0": 0, "l": 0, "a01": 0}
while True:
    # files = ['a0', 'a00', 'a000', 'a0000', 'a1', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    # files = ['a0', 'a00', 'a000', 'a01', 'l' ]
    files = ["a0", "l", "a01"]
    # files = ["a01"]
    for file in files:
        delete_all_files_inside_folder(f"{path}/TEMP/")
        print("[🔴]", end="")

        HOST_UP = (
            True
            if os.system(
                f"ping -c 1  {stores_sensitive_info.ip.get('EM ROUTER')} >/dev/null"
            )
            == 0
            else False
        )
        print(f"[🟢][{HOST_UP}]", end="")
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
                    f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: in {round(stop - start)} sec :: {CBLUE}{sales}€{CEND} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND} SLEPT FOR {timers.get(file)}s",
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
