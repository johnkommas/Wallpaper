#  Copyright (c) Ioannis E. Kommas 2024. All Rights Reserved

# Make the Connection
import pyodbc
from Private.stores_sensitive_info import ip
from subprocess import call, check_output
import time
import socket
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def connect():
    load_dotenv()
    sql_counter = 0
    max_retries = 3
    my_ip = get_ip_address()

    for attempt in range(max_retries + 1):
        try:
            cnxn = f"""DRIVER={{ODBC Driver 17 for SQL Server}};
                                                 Server={os.getenv('SQL_SERVER')};
                                                 UID={os.getenv('UID')};
                                                 PWD={os.getenv('SQL_PWD')};
                                                 Database={os.getenv('DATABASE')};
                                                 TrustServerCertificate={os.getenv('TSC')}"""
            connection_string = cnxn
            connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
            engine = create_engine(connection_url)
            return engine
        except pyodbc.OperationalError:
            if attempt < max_retries:
                print(f"\r🔴: (SQL) Connection failed on attempt {attempt + 1}. Retrying...", end='')
                time.sleep(2)  # Μικρή καθυστέρηση πριν την επόμενη προσπάθεια
            else:
                print(f"\r🔴: (!SQL!) Working Remotely: My IP ADDRESS is {my_ip}", end='')
                return open_vpn(sql_counter)


def open_vpn(sql_counter):
    EM_mode = os.system(f"ping -c 1  {ip.get('EM')} >/dev/null")
    if EM_mode == 0:
        print("\r🟢: (SQL) Elounda Market is UP, Trying to get VPN UP...", end='')
        call(["scutil", "--nc", "start", os.getenv('VPN_NAME'), '--secret', os.getenv('VPN_PWD')])
        time.sleep(5)
        Server_mode = os.system(f"ping -c 1  {ip.get('EM ROUTER')} >/dev/null")
        if Server_mode == 0:
            print("\r🟢: (SQL) VPN IS UP", end='')
            return connect()
        else:
            sql_counter += 1
            print(f"\r🔴: (SQL) VPN IS STILL DOWN || Tries: {sql_counter}", end='')
            return open_vpn(sql_counter)

    else:
        sql_counter += 1
        print(f"\r🔴: (SQL) Internet on Site Is Down || Tries: {sql_counter}", end='')
        return open_vpn(sql_counter)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
