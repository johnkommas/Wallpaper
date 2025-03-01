import os
import mac_imessage
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


def send(retail_point):
    """
    Send an iMessage with a predefined alert message to a recipient retrieved from environment variables.
    Handles errors that may occur during the sending process.

    Raises exceptions if the message or recipient is not provided correctly or if any other issues arise
    during the execution of the function.

    :raises TypeError: If the provided message or recipient is of invalid type.
    :raises Exception: For any other unforeseen error during execution.
    """
    try:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        message = (
            f"⚠️ PoS ALERT! ⚠️\n\n"
            f"🚨ΒΡΕΘΗΚΕ ΕΓΓΡΑΦΗ ΜΕ ΛΑΘΗ 🚨\n\n"
            f"Παρακαλώ διορθώστε την εγγραφή πληρωμής με κάρτα.\n\n"
            f"🛒 STORE: {os.getenv('MAIN_STORE_NAME')}\n\n"
            f"💳 {retail_point}\n\n"
            f"⏰ TIME: {now}"
        )

        recipient = os.getenv("IMESSAGE_PHONE")

        # Δοκιμάστε να καλέσετε τη συνάρτηση
        mac_imessage.send_iMessage(message, recipient)

    except TypeError as e:
        # Τυπώστε μια φιλική και περιγραφική πληροφορία για το σφάλμα
        print(f"Σφάλμα κατά την αποστολή του iMessage: {e}")
    except Exception as e:
        # Extra handling για οποιοδήποτε άλλο σφάλμα
        print(f"Απρόβλεπτο πρόβλημα: {e}")
