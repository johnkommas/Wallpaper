from Utilities import imessage
from SQL_FOLDER import fetch_data
from dotenv import load_dotenv
import os
import time

load_dotenv()

def run():
    # Εκτέλεση SQL ερωτήματος και φόρτωση δεδομένων
    query = ["Pos_Pending.sql"]

    df = fetch_data.get_sql_data(query[0])
    if df.empty:
        return

    imessage.mailme(df.iloc[0, 0])


if __name__ == "__main__":
    refresh_rate = int(os.getenv("REFRESH_TIMER"))
    while True:
        try:
            print(f"Job Started: {time.ctime()} || ", end='')
            startTime = time.monotonic()
            run()
            elapsed = time.monotonic() - startTime
            print(f"Job Ended: Execution time: {round(elapsed, 2)}sec ||", end='')
            print(f" Next Refresh @: {time.ctime(time.time() + refresh_rate)}")
            time.sleep(refresh_rate)
        except KeyboardInterrupt:
            break
        except Exception as e:
            break