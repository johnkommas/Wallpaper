#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import os
import shutil
import logging
import sys

from Private import sql_connect, stores_sensitive_info
from Files import sql, plot, write
from datetime import datetime
import pandas as pd
import time
import atexit

path = f"{stores_sensitive_info.OneDrivePath}/Pictures/Wallpaper/in"
path_2 = f"{stores_sensitive_info.OneDrivePath}/Pictures/Wallpaper/roll"
path_3 = f"{stores_sensitive_info.OneDrivePath}/Pictures/Wallpaper/in/OFFLINE"
log_path = f'{os.getcwd()}/std.log'
logging.basicConfig(filename=log_path, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
wp_logger = logging.getLogger()
wp_logger.setLevel("WARNING")


def delete_all_files_inside_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def get_online_status(user, store):
    df = pd.read_sql_query(sql.check_online_user(user), store)
    if df.ID[0] == 'ESLOGIN':
        result = 'green'
    else:
        result = 'red'
    return result, df['EDate']


def run(file, flag):
    start = time.process_time()
    start_ = time.perf_counter()
    today = datetime.now()
    df_sales_elounda = pd.read_sql_query(sql.sales_elounda(today.year - 5, today.month, today.day),
                                         sql_connect.connect())
    df_sales_elounda_today = pd.read_sql_query(sql.sales_elounda_today(today.year, today.month, today.day),
                                               sql_connect.connect())

    # df_best_products_sales_today = pd.read_sql_query(sql.today_products(today.year, today.month, today.day),
    #                                            sql_connect.connect())

    # print(df_best_products_sales_today)
    a = df_sales_elounda.TurnOver[df_sales_elounda.YEAR == today.year].values[0]
    b = df_sales_elounda_today.values[0][0]
    c = df_sales_elounda

    # ΑΝΑΛΥΤΙΚΟΣ ΤΖΙΡΟΣ ΕΝΑΡΞΗ
    df = pd.read_sql_query(sql.sales_elounda_graph(today.year - 5, today.month), sql_connect.connect())
    df['DATE'] = df.apply(lambda x: f'{int(x.MONTH)}/{int(x.DAY)}/{int(x.YEAR)}', axis=1)
    df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime("%d/%m/%Y")

    product_info = 0
    pda = pd.read_sql_query(sql.pda_alert(), sql_connect.connect())
    user_status = []
    lato_user_status = []
    elapsed_time = []
    lato_elapsed_time = []

    if flag == 'a00':
        # GET PRODUCT INFO


        price_change = pd.read_sql_query(sql.price_changes_today(), sql_connect.connect())
        new_product = pd.read_sql_query(sql.new_products(), sql_connect.connect())
        special_price = pd.read_sql_query(sql.special_price(), sql_connect.connect())
        customer_prefer = pd.read_sql_query(sql.customer_prefer(), sql_connect.connect())
        product_info = {
            "price_change": price_change.COUNT.iloc[0],
            "new_product": new_product.COUNT.iloc[0],
            "special_price": special_price.COUNT.iloc[0],
            "customer_prefer": customer_prefer.COUNT.iloc[0],
        }
    elif flag == 'a000':
        # Tree map
        df = pd.read_sql_query(sql.quantity_for_tree_map(today.year, today.month), sql_connect.connect())
        plot.make_wordcloud(df, path)
        plot.tree_map(df, path)

    elif flag == 'a01':
        users = stores_sensitive_info.EM_users
        lato_users = stores_sensitive_info.LATO_users
        for user in users:
            status, date = get_online_status(user, sql_connect.connect())
            diff = today - date
            user_status.append(status)
            if diff[0].components.days == 0:
                elapsed_time.append(
                    f'{diff[0].components.hours}h.{diff[0].components.minutes}m')
            elif diff[0].components.days == 1:
                elapsed_time.append(f'{diff[0].components.days}Day')
            else:
                elapsed_time.append(f'{diff[0].components.days}Days')
        for user in lato_users:
            status, date = get_online_status(user, sql_connect.connect_lato())
            diff = today - date
            lato_user_status.append(status)
            if diff[0].components.days == 0:
                lato_elapsed_time.append(f'{diff[0].components.hours}h.{diff[0].components.minutes}m')
            elif diff[0].components.days == 1:
                lato_elapsed_time.append(f'{diff[0].components.days}Day')
            else:
                lato_elapsed_time.append(f'{diff[0].components.days}Days')

    timed = datetime.now().strftime("%d . %m . %Y   %H : %M : %S")
    print(" 🟢", end='')
    write.run(a, b, c, file, today, path, path_2, df_sales_elounda_today.values[0][0], timed, df, flag, pda,
              product_info, user_status, elapsed_time, lato_user_status, lato_elapsed_time)
    print("🟢", end='')

    # Randar Plot ΕΝΑΡΞΗ
    # df = pd.read_sql_query(sql.randar_query(today.year, today.month), sql_connect.connect())
    # df.dropna(inplace=True)
    # # print(df)
    # categories = df['BRAND'].values
    # sales = df['SALES'].values
    # plot.randar_chart(categories, sales, path)

    stop = time.process_time()
    stop_ = time.perf_counter()
    return start_, stop_, df_sales_elounda_today.values[0][0]


CRED = '\033[91m'
CBLUE = '\33[34m'
CGREEN = '\033[92m'
CEND = '\033[0m'

times = 0
failed = 0
timers = {'a0': 0,
          'l': 0,
          'a01': 0}
while True:
    # files = ['a0', 'a00', 'a000', 'a0000', 'a1', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    # files = ['a0', 'a00', 'a000', 'a01', 'l' ]
    files = ['a0', 'l', 'a01']
    for file in files:
        delete_all_files_inside_folder(f"{path}/TEMP/")
        print("[🔴]", end='')

        HOST_UP = True if os.system(f"ping -c 1  {stores_sensitive_info.ip.get('EM ROUTER')} >/dev/null") == 0 else False
        print(f"[🟢][{HOST_UP}]", end='')
        try:
            if HOST_UP:
                time.sleep(timers.get(file))
                start, stop, sales = run(file, file)
                sleep_t = 60 - round(stop - start) if 60 - round(stop - start) > 0 else 0
                timers[file] = sleep_t

                times += 1
                print(
                    f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: in {round(stop - start)} sec :: {CBLUE}{sales}€{CEND} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND} SLEPT FOR {timers.get(file)}s",
                    end='')
            else:
                write.offline(path, path_2, path_3)
                wp_logger.error('VPN OFFLINE')
                failed += 1
                print(
                    f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                    end='')
        except KeyboardInterrupt:
            write.offline(path, path_2, path_3)
            sys.exit(0)
        except Exception as e:
            print(f"\rException Occured", end='')
            wp_logger.error(e)
            failed += 1
            print(
                f"\r{CRED}Report Ready{CEND} :: {datetime.now().strftime('%H:%M:%S')} :: Refreshed {CGREEN}{times}{' time' if times == 1 else ' times'}{CEND} Faield {CRED}{failed} times {CEND}",
                end='')
