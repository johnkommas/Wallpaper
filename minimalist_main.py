#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import logging
import shutil
import sys
import time
import numpy as np
import pandas as pd
from SQL_FOLDER import fetch_data, sql_connect
from Files import minimalist_write
from datetime import datetime
from Sound_Pack import sound
import signal
from dotenv import load_dotenv
import os

load_dotenv()


def timeout_handler(signum, frame):
    raise TimeoutError


def get_input_with_timeout(prompt, timeout, default):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    try:
        return input(prompt)
    except (TimeoutError, EOFError):
        print(f"\nInput timed out. Defaulting to {default}.")
        return default
    finally:
        signal.alarm(0)  # Disable alarm


refresh_rate = int(get_input_with_timeout("Enter Refresh Rate in: sec ", 5, os.getenv("REFRESH_TIMER")))
data = ["MIKROTIK", "NONE", "SIMPLE"]
# Λήψη της τιμής της μεταβλητής περιβάλλοντος
color_pallete = os.getenv("COLOR_PALLETE")

# Έλεγχος εάν η μεταβλητή περιβάλλοντος είναι έγκυρη και υπάρχει στη λίστα
if color_pallete in data:
    multiple_data = data.index(color_pallete)
else:
    multiple_data = 3


print(f"Refresh rate: {refresh_rate}")
print(f"Multiple Data: {multiple_data}")


def create_folder_if_not_exists(folder: str) -> None:
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
            print(f"Folder created: {folder}")
        except Exception as e:
            print(f"Failed to create folder {folder}. Reason: {e}")


path = f"{os.getcwd()}/in/{os.getenv('COLOR_PALLETE')}"
path_2 = f"{os.getcwd()}/roll"

create_folder_if_not_exists(f'{path}/TEMP')
create_folder_if_not_exists(path_2)

log_path = f"{os.getcwd()}/std.log"
logging.basicConfig(
    filename=log_path, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s"
)
wp_logger = logging.getLogger()
wp_logger.setLevel("WARNING")
SQL_FILES = [
    "ESFIItemEntry_ESFIItemPeriodics_a.sql",  # 0
    "ESFIItemEntry_ESFIItemPeriodics_c.sql",  # 1
    "ES00EventLog_a.sql",  # 2
    "ESFIItemPeriodics_MonthlyTurnOver.sql"  # 3
]


def delete_all_files_inside_folder(folder: str) -> None:
    # print(f"Deleting files in folder: {folder}")
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


def run(temp_file, multiple_data):
    # print(refresh_rate, temp_file, flag)
    print(f"\r🟢 DATA @{datetime.now().strftime('%H:%M:%S')} -> ", end="")

    start_ = time.perf_counter()
    today = datetime.now()

    # get_online_offline_ users_info
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

    def complete_df(temp_df: pd.DataFrame) -> pd.DataFrame:
        temp_df["COLOR"] = np.where(temp_df["ID"] == "ESLOGOUT", "red", "green")
        temp_df["DIFF"] = today - temp_df["EDate"]
        temp_df["elapsed_time"] = temp_df.apply(lambda row: calc(row), axis=1)
        return temp_df

    def fetch_data_with_params(sql_file, params=None):
        result = fetch_data.get_sql_data(sql_file, params)
        if result is None or isinstance(result, type):
            raise ValueError(f"SQL file '{sql_file}' returned invalid data!")
        return result

    params = {"year": today.year - 5, "month": today.month, "day": today.day}
    params_2 = {"year": today.year - 5, "month": today.month}

    #
    if multiple_data >= 2:
        df_sales_elounda = fetch_data_with_params(SQL_FILES[0], params)
    else:
        df_sales_elounda = pd.DataFrame()

    first_q_timer = time.perf_counter()
    print(f"🟢DONE IN:{round(first_q_timer - start_)} sec DB YTD || ", end="")

    if multiple_data == 3:
        df = fetch_data_with_params(SQL_FILES[1], params_2)
        second_q_timer = time.perf_counter()
        df["DATE"] = df.apply(lambda x: f"{int(x.MONTH)}/{int(x.DAY)}/{int(x.YEAR)}", axis=1)
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d/%m/%Y")
        print(f"🟢DONE IN: {round(second_q_timer - first_q_timer)} sec MONTHLY DATA || ", end="")

        elounda_users = tuple(os.getenv("EMUSERS").split(","))
        em_df = fetch_data.get_sql_data(SQL_FILES[2], None, tuple_data=elounda_users)
        status_users_elounda = complete_df(em_df)
        status_users_elounda = filter_data(status_users_elounda)

    else:
        df = pd.DataFrame()
        status_users_elounda = None

    # GET MONTHLY TURNOVER DATA
    monthly_turnover_df = fetch_data.get_sql_data(SQL_FILES[3])
    print(f"🟢DONE MONTHLY TURNOVER || ", end="")


    minimalist_write.run(df_sales_elounda, path, path_2, temp_file, today, df, multiple_data, status_users_elounda, monthly_turnover_df)
    stop_ = time.perf_counter()
    return start_, stop_


def start_at_exact_second():
    """
    Περιμένει μέχρι τα δευτερόλεπτα του ρολογιού να είναι 00 και ξεκινά το πρόγραμμα.
    """
    while True:
        # Πάρε τον τρέχοντα χρόνο
        now = datetime.now()

        # Έλεγχος αν τα δευτερόλεπτα είναι 00
        if now.second == 56:
            print("Ξεκινάω το πρόγραμμα στις: ", now)
            break  # Σπάει το loop και ξεκινά το πρόγραμμα

        # Αναμονή για 0.5 δευτερόλεπτα πριν ξανά ελέγξει
        time.sleep(0.5)


CRED = "\033[91m"
CBLUE = "\33[34m"
CGREEN = "\033[92m"
CEND = "\033[0m"

times = 0
failed = 0
timers = {"wallpaper": 0}

sound.done()
# Κλήση της συνάρτησης
# start_at_exact_second()
sound.run()
running = True
total_timers = []
while running:
    file = "wallpaper"
    delete_all_files_inside_folder(f"{path}/TEMP/")
    HOST_UP = (
        True
        if os.system(
            f"ping -c 1  {os.getenv('IP_EM_ROUTER')} >/dev/null"
        )
           == 0
        else False
    )
    try:
        if HOST_UP:
            time.sleep(timers.get(file))

            start, stop = run(file, multiple_data)
            sleep_t = (refresh_rate - round(stop - start) if refresh_rate - round(stop - start) > 0 else 0)
            timers[file] = sleep_t

            times += 1
            total_timers.append(round(stop - start))
            print(
                f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: in {round(stop - start)} sec :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND} || TIMERS TABLE {total_timers}",
                end="", )
            sound.done()
            if multiple_data == 1:
                raise KeyboardInterrupt

        else:
            sound.error()
            sql_connect.open_vpn(failed)
            failed += 1
            print(
                f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                end="")
    except KeyboardInterrupt:
        sound.error()
        print("\n🟢 Safely stopping the app... Cleaning up resources.")
        sound.exit()
        print("🟢 The App will Now stop Running")
        running = False
        sys.exit(0)
    except Exception as e:
        sound.error()
        print(f"\rException Occured", end="")
        wp_logger.error(e)
        failed += 1
        print(
            f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
            end="")
