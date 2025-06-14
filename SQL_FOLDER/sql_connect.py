#  Copyright (c) Ioannis E. Kommas 2024. All Rights Reserved

# Make the Connection
import pyodbc
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
    load_dotenv()  # Φόρτωση μεταβλητών περιβάλλοντος από το .env αρχείο

    # Έλεγχος αν το site (π.χ. Elounda Market) είναι προσβάσιμο
    EM_mode = os.system(f"ping -c 1 {os.getenv('IP_EM')} >/dev/null")
    if EM_mode == 0:
        print("\r🟢: (SQL) Elounda Market is UP, Trying to get VPN UP...", end='')

        # Προσπάθεια σύνδεσης μέσω AppleScript
        vpn_name = "Elounda Market"
        apple_script = f"""
        tell application "System Events"
            tell current location of network preferences
                if exists service "{vpn_name}" then
                    connect service "{vpn_name}"
                end if
            end tell
        end tell
        """
        os.system(f"osascript -e '{apple_script}'")

        # Χρόνος αναμονής για να σταθεροποιηθεί η σύνδεση VPN
        time.sleep(5)

        # Έλεγχος εάν το VPN router είναι πλέον προσβάσιμο
        Server_mode = os.system(f"ping -c 1 {os.getenv('IP_EM_ROUTER')} >/dev/null")
        if Server_mode == 0:
            print("\r🟢: (SQL) VPN IS UP", end='')
            return connect()  # Σύνδεση με τη βάση δεδομένων
        else:
            sql_counter += 1
            print(f"\r🔴: (SQL) VPN IS STILL DOWN || Tries: {sql_counter}", end='')
            return open_vpn(sql_counter)  # Επανεκκίνηση της προσπάθειας για VPN

    else:
        sql_counter += 1
        print(f"\r🔴: (SQL) Internet on Site Is Down || Tries: {sql_counter}", end='')
        time.sleep(10)  # Καθυστέρηση πριν την επόμενη προσπάθεια
        return open_vpn(sql_counter)  # Επανεκκίνηση προσπάθειας



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
