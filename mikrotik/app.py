import imaplib
import email
from email.header import decode_header
import pandas as pd
from dotenv import load_dotenv
import os
import re
from tqdm import tqdm
from mikrotik import data_analysis

# Προβολή όλων των στηλών
pd.set_option("display.max_columns", None)

# Αν θέλετε επίσης να δείτε και όλες τις σειρές
pd.set_option("display.max_rows", None)

# Για πλήρη εμφάνιση περιεχομένου των δεδομένων (σε περίπτωση που κόβονται)
pd.set_option("display.max_colwidth", None)

# Προβολή χωρίς συντόμευση (όπως "...")
pd.set_option("display.expand_frame_repr", False)

load_dotenv()


# Σύνδεση με το Gmail
def connect_to_gmail():
    try:
        # Λήψη διαπιστευτηρίων από περιβαλλοντικές μεταβλητές
        gmail_user = os.getenv("GMAIL_USER")
        gmail_pass = os.getenv("GMAIL_PASS")

        if not gmail_user or not gmail_pass:
            raise ValueError(
                "Missing Gmail credentials (GMAIL_USER and/or GMAIL_PASS)."
            )

        # Σύνδεση στον IMAP Server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(gmail_user, gmail_pass)
        # print("Connected")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"Failed to connect: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None


# Συνάρτηση για ασφαλή αποκωδικοποίηση
def decode_safe(payload, encoding="utf-8"):
    try:
        # Πρώτη προσπάθεια βασισμένη στην προκαθορισμένη κωδικοποίηση (UTF-8)
        return payload.decode(encoding)
    except UnicodeDecodeError:
        try:
            # Εναλλακτική χρήση της κατάλληλης προσδιορισμένης κωδικοποίησης στη λογική email
            return payload.decode("ISO-8859-1")
        except UnicodeDecodeError:
            print("None encoding found")
            # Fallback: αγνόησε μη έγκυρους χαρακτήρες για να προχωρήσεις στην επεξεργασία
            return payload.decode("utf-8", errors="ignore")


from datetime import datetime


def extend_df_with_columns(df):
    """
    Επεξεργάζεται το DataFrame:
    - Εξάγει πληροφορίες από τη στήλη `Body` για `Port`, `Public IP`, `Time`, και `Api`.
    - Μετατρέπει τη στήλη `Time` σε `Date` (2025.30.01) και `Time` (15:03:38).
    - Διαγράφει τις στήλες `Subject` και `From`, και αφαιρεί τη στήλη `Body`.
    """

    # Κανονικές εκφράσεις για τα δεδομένα
    data_patterns = {
        "Port": r"Port:\s*(\d+)",
        "Public IP": r"Public IP:\s*([\d.]+)",
        "Time": r"Time:\s*([\d:]+\s\w+\s[\w/]+)",
        "Api": r"Api:\s*(.+)",
    }

    # Συνάρτηση για εξαγωγή τιμών από το body ενός email
    def extract_value_from_body(body, pattern):
        match = re.search(pattern, body)
        return match.group(1).strip() if match else None

    # Δημιουργία νέων στηλών στο DataFrame
    for key, pattern in data_patterns.items():
        df[key] = df["Body"].apply(lambda body: extract_value_from_body(body, pattern))

    # Διαχωρισμός και μετατροπή `Time` σε δύο νέες στήλες `Date` και `Time`
    def split_time_column(value):
        if value and " on " in value:
            try:
                # Διαχωρισμός Time και Date
                time_part, date_part = value.split(" on ")
                # Μετατροπή του date_part (π.χ. "jan/30/2025") στη μορφή 2025.30.01
                date_obj = datetime.strptime(date_part, "%b/%d/%Y")
                formatted_date = date_obj.strftime("%Y.%d.%m")
                return pd.Series({"Time": time_part.strip(), "Date": formatted_date})
            except Exception as e:
                print(f"Error parsing date/time: {value}. Error: {e}")
        return pd.Series({"Time": None, "Date": None})

    # Ανάλυση Time σε δύο στήλες - Date και Time
    df[["Time", "Date"]] = df["Time"].apply(split_time_column)

    # Αφαιρεί χαρακτήρες `\r` από τη στήλη `Api`
    df["Api"] = df["Api"].str.replace("\r", "", regex=False)

    # Διαγραφή περιττών στηλών
    df.drop(columns=["Subject", "From", "Body"], inplace=True)

    # Επαναταξινόμηση στηλών όπως ζητήθηκε
    df = df[["Port", "Public IP", "Date", "Time", "Api"]]

    return df




# Ανάκτηση email με το συγκεκριμένο θέμα
def retrieve_mikrotik_emails(_mail, label):
    try:
        # Επιλογή φακέλου
        status, messages = _mail.select(label)
        if status != "OK":
            raise ValueError(
                f"Failed to select folder/label '{label}'. Please ensure it exists."
            )

        # Αναζητούμε emails με το κατάλληλο θέμα
        status, messages = _mail.search(None, '(SUBJECT "MikroTik Alert:")')
        if status != "OK":
            raise RuntimeError("Failed to execute SEARCH command.")

        email_ids = messages[0].split()
        email_data = []

        for email_id in email_ids:

            # Ανάγνωση email
            status, msg_data = _mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Αποκωδικοποίηση του email
                    msg = email.message_from_bytes(response_part[1])

                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()  # Αποκωδικοποίηση αν είναι bytes
                    from_ = msg.get("From")

                    # Ανάγνωση σώματος email
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            if (
                                    content_type == "text/plain"
                                    and "attachment" not in content_disposition
                            ):
                                # Απόκτηση του περιεχομένου και ασφαλής αποκωδικοποίηση
                                body = decode_safe(part.get_payload(decode=True))
                                break
                    else:
                        # Μη-πολυμερές μήνυμα (απλό σώμα)
                        body = decode_safe(msg.get_payload(decode=True))

                    # Προσθήκη στη λίστα δεδομένων
                    email_data.append({"Subject": subject, "From": from_, "Body": body})

        # Μετατροπή σε pandas DataFrame
        df = pd.DataFrame(email_data)
        return df

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error while fetching emails: {e}")
        return None


def run():
    # Σύνδεση στο Gmail
    mail = connect_to_gmail()
    df = pd.DataFrame()
    if mail:
        # Ανάκτηση δεδομένων
        df = retrieve_mikrotik_emails(
            mail, label="MIKROTIK"
        )  # Χρησιμοποιήστε το 'INBOX' ή το κατάλληλο label
        mail.logout()

        # Εμφάνιση δεδομένων
        if df is not None:
            df = extend_df_with_columns(df)
            return df
        else:
            print("No valid emails found.")


def plot_run(df, path, color):
    data_analysis.visualize_api_hackers_ports_pie(df, path_a=path, color=color)


