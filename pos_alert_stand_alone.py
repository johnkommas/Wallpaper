from Utilities import imessage
from SQL_FOLDER import fetch_data
from dotenv import load_dotenv
import os
import time

# Ορισμός χρωμάτων ANSI για το τερματικό
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

load_dotenv()



def run():
    # Εκτέλεση SQL ερωτήματος και φόρτωση δεδομένων
    query = "Pos_Pending.sql"

    df = fetch_data.get_sql_data(query)
    if df.empty:
        return

    imessage.mailme(df.iloc[0, 0])



if __name__ == "__main__":
    refresh_rate = int(os.getenv("REFRESH_TIMER"))
    while True: 
        try:
            print(f"{GREEN}Job Started: {time.ctime()} {RESET}|| ", end='')
            startTime = time.monotonic()
            run()
            elapsed = time.monotonic() - startTime
            print(f"{YELLOW}Job Ended: Execution time: {round(elapsed, 2)}sec {RESET}||", end='')
            print(f" {RED} Next Refresh @: {time.ctime(time.time() + refresh_rate)}{RESET}")
            time.sleep(refresh_rate)
        except KeyboardInterrupt:
            break
        except Exception as e:
            break