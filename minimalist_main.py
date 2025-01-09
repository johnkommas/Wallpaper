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
from Files import minimalist_write
from Private import stores_sensitive_info, sql_connect
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import queue
import threading


class InterruptibleInput:
    def __init__(self, timeout):
        self.timeout = timeout

    def get_input(self):
        q = queue.Queue()

        def inner():
            q.put(input("Enter Refresh Rate in: sec "))

        threading.Thread(target=inner).start()

        try:
            return int(q.get(block=True, timeout=self.timeout))
        except queue.Empty:
            print("\nInput timed out, defaulting to 600 sec")
            return 600
        except ValueError:
            print("\nInput Value Error")
            return self.get_input()


refresh_rate = InterruptibleInput(timeout=5).get_input()
print(f"Refresh rate: {refresh_rate}")

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
    "ESFIItemEntry_ESFIItemPeriodics_c.sql",
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


def run(temp_file):
    # print(refresh_rate, temp_file, flag)
    print(f"🟢 DATA @{datetime.now().strftime('%H:%M:%S')} -> ", end="")

    start_ = time.perf_counter()
    today = datetime.now()

    def fetch_data_with_params(sql_file, params=None):
        result = fetch_data.get_sql_data(sql_file, params)
        if result is None or isinstance(result, type):
            raise ValueError(f"SQL file '{sql_file}' returned invalid data!")
        return result

    params = {"year": today.year - 5, "month": today.month, "day": today.day}
    params_2 = {"year": today.year - 5, "month": today.month}
    df_sales_elounda = fetch_data_with_params(SQL_FILES[0], params)
    df = fetch_data_with_params(SQL_FILES[1], params_2)
    # print(df)
    df["DATE"] = df.apply(lambda x: f"{int(x.MONTH)}/{int(x.DAY)}/{int(x.YEAR)}", axis=1)
    df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d/%m/%Y")
    minimalist_write.run(df_sales_elounda, path, path_2, temp_file, today, df)
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

        # Αναμονή για 0.5 δευτερόλεπτα πριν ξαναελέγξει
        time.sleep(0.5)


CRED = "\033[91m"
CBLUE = "\33[34m"
CGREEN = "\033[92m"
CEND = "\033[0m"

times = 0
failed = 0
timers = {"wallpaper": 0}

# Κλήση της συνάρτησης
start_at_exact_second()
while True:
    file = "wallpaper"
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
            start, stop = run(file)
            sleep_t = (
                refresh_rate - round(stop - start) if refresh_rate - round(stop - start) > 0 else 0
            )
            timers[file] = sleep_t

            times += 1
            print(
                f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: in {round(stop - start)} sec :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                end="",
            )
        else:
            wp_logger.error("VPN OFFLINE")
            sql_connect.open_vpn(failed)
            failed += 1
            print(
                f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                end="",
            )
    except KeyboardInterrupt:
        print("🟢 Safely stopping the app... Cleaning up resources.")
        print("🟢 The App will Now stop Running")
        for thread in threading.enumerate():
            if thread is not threading.main_thread():
                print(f"Stopping thread: {thread.name}")
                thread.join(0.5)  # Χρονικό όριο για να κλείσουν τα threads
        print("Clean exit. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\rException Occured", end="")
        wp_logger.error(e)
        failed += 1
        print(
            f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
            end="",
        )
