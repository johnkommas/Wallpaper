import imaplib
import email
from email.header import decode_header
import pandas as pd
from dotenv import load_dotenv
import os
import re
from tqdm import tqdm
from mikrotik import data_analysis
from routeros_api import connect
import routeros_api
import paramiko

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
        print(f"Failed to connect: {e}", end="")
        return None
    except ValueError as e:
        print(f"Error: {e}", end="")
        return None


import paramiko


def connect_via_ssh():
    try:
        # Δημιουργία SSH Client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Σύνδεση
        client.connect(
            hostname=os.getenv("MIKROTIK_HOST"),
            username=os.getenv("MIKROTIK_USER"),
            password=os.getenv("MIKROTIK_PASS"),
            port=int(os.getenv("MIKROTIK_PORT", 22)),  # Προεπιλογή port: 22
        )
        # print("Connected via SSH successfully.")

        # Εκτέλεση εντολής για ενεργές PPP συνδέσεις (VPN)
        # print("\nFetching active PPP connections:")
        stdin, stdout, stderr = client.exec_command("/ppp active print terse")
        ppp_output = stdout.read().decode("utf-8")

        # Διαχωρισμός εξόδου σε λίστα, γραμμή ανά γραμμή
        lines = ppp_output.strip().split("\n")

        # Δημιουργία λίστας λεξικών για τα δεδομένα
        data = []
        for line in lines:
            entry = {}
            # Χώρισμα κάθε γραμμής με βάση το κενό διάστημα
            for part in line.split():
                if "=" in part:
                    key, value = part.split("=", 1)  # Διαχωρισμός στο "="
                    entry[key] = value
            data.append(entry)

        # Μετατροπή σε DataFrame
        df = pd.DataFrame(data)

        # Κλείσιμο σύνδεσης
        client.close()

        return df  # Επιστροφή του DataFrame

    except Exception as e:
        print(f"Error connecting via SSH: {e}")
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


def retrieve_mikrotik_emails(_mail, label, counter_file="counter.txt"):
    try:
        # Επιλογή φακέλου
        status, messages = _mail.select(label)
        if status != "OK":
            raise ValueError(
                f"Failed to select folder/label '{label}'. Please ensure it exists."
            )

        # Ανάγνωση ή δημιουργία του αρχείου counter.txt
        if not os.path.exists(counter_file):
            # Αν το αρχείο δεν υπάρχει, το δημιουργούμε με αρχική τιμή "0"
            with open(counter_file, "w") as f:
                f.write("0")
            last_read_email_count = 0
        else:
            # Αν το αρχείο υπάρχει, διαβάζουμε την τελευταία καταμέτρηση
            with open(counter_file, "r") as f:
                last_read_email_count = int(f.read().strip())

        # Αναζήτηση όλων των emails με το κατάλληλο θέμα
        status, messages = _mail.search(None, '(SUBJECT "MikroTik Alert:")')
        if status != "OK":
            raise RuntimeError("Failed to execute SEARCH command.")

        email_ids = messages[0].split()
        total_emails = len(email_ids)

        # Αν δεν υπάρχουν νέα emails
        if last_read_email_count >= total_emails:
            print("No new emails to process.", end="")
            return None  # Καμία νέα εγγραφή

        # Λίστα για την αποθήκευση δεδομένων email
        email_data = []

        # Επεξεργασία μόνο των νέων emails
        for email_id in tqdm(email_ids[last_read_email_count:]):
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

        # Μετατροπή δεδομένων σε pandas DataFrame
        new_df = pd.DataFrame(email_data)

        # Ενημέρωση του αρχείου καταμέτρησης emails
        with open(counter_file, "w") as f:
            f.write(str(total_emails))

        return new_df  # Επιστροφή του DataFrame με τα νέα δεδομένα

    except Exception as e:
        print(f"Error while fetching emails: {e}", end="")
        return None  # Επιστροφή None σε περίπτωση σφάλματος


def run(csv_file="emails_data.csv"):
    # Σύνδεση στο Gmail
    mail = connect_to_gmail()
    if mail:
        # Ελέγχουμε για νέα emails
        new_emails_df = retrieve_mikrotik_emails(mail, label="MIKROTIK")  # Χρησιμοποιήστε το 'INBOX' ή το κατάλληλο label
        mail.logout()

        if new_emails_df is not None:
            print("New emails fetched. Processing...", end="")

            # Επεξεργασία δεδομένων
            new_emails_df = extend_df_with_columns(new_emails_df)

            if os.path.exists(csv_file):
                print(f"CSV file {csv_file} exists. Appending data...", end="")
                # Διαβάζουμε τα υπάρχοντα δεδομένα
                try:
                    existing_df = pd.read_csv(csv_file)
                    # Συγχώνευση χωρίς διπλότυπα
                    combined_df = (
                        pd.concat([existing_df, new_emails_df])
                        .drop_duplicates()
                        .reset_index(drop=True)
                    )
                except Exception as e:
                    combined_df = new_emails_df

            else:
                print(f"CSV file {csv_file} does not exist. Creating...", end="")
                combined_df = new_emails_df

            # Αποθήκευση συγχωνευμένου DataFrame στο CSV
            combined_df.to_csv(csv_file, index=False)
            return combined_df

        else:
            print("No new emails. Loading data from CSV...", end="")
            # Δεν υπάρχουν νέα emails, διαβάζουμε από το CSV (αν υπάρχει)
            if os.path.exists(csv_file):
                return pd.read_csv(csv_file)
            else:
                print(f"CSV file {csv_file} does not exist. Returning empty DataFrame.", end="")
                return pd.DataFrame()


def plot_run(df, path, sankey_path, color, loop_counter):
    data_analysis.visualize_api_hackers_ports_donut(df, path_a=path, color=color)
    data_analysis.sankey_graph(loop_counter, df, path_a=sankey_path)


