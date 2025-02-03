import requests
import pandas as pd
from dotenv import load_dotenv
import os
from urllib.parse import quote
from datetime import datetime
# Ρύθμιση ώστε να εμφανίζονται όλες οι στήλες
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

# Φόρτωση των μεταβλητών περιβάλλοντος από το αρχείο .env
load_dotenv()

# Ρύθμιση βασικών παραμέτρων από το .env αρχείο
YOU_TRACK_URL = os.getenv("YOU_TRACK_URL")
API_TOKEN = os.getenv("API_TOKEN")
PROJECT_ID = os.getenv("PROJECT_ID")  # Βεβαιωθείτε ότι έχετε ορίσει το PROJECT_ID

# Βεβαιωθείτε ότι οι απαραίτητες μεταβλητές περιβάλλοντος έχουν οριστεί
if not YOU_TRACK_URL or not API_TOKEN or not PROJECT_ID:
    raise ValueError(
        "Οι μεταβλητές YOU_TRACK_URL, API_TOKEN και PROJECT_ID πρέπει να οριστούν στο αρχείο .env"
    )

# Ορίστε τις καταστάσεις που θέλετε να συλλέξετε
states = ["Open", "In_Progress", "To_Be_Discussed", "REPEATABLE", "Fixed"]

# Κεφαλίδες για το αίτημα
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json",
}


def get_issues(state):
    try:
        formatted_state = f"state: '{state}'" if " " in state else f"state: {state}"
        encoded_query = quote(formatted_state)
        # Προσθήκη του πεδίου 'updated' στο αίτημα
        api_url = f"{YOU_TRACK_URL}/api/issues?query={encoded_query}&fields=id,summary,project(name),state(name),updated"

        # print(f"Αποστολή αιτήματος προς: {api_url}")
        response = requests.get(api_url, headers=headers)
        # print(f"Κατάσταση Απάντησης: {response.status_code}")
        if response.status_code != 200:
            print(f"Απάντηση: {response.text}")  # Εκτύπωση του μηνύματος σφάλματος
        response.raise_for_status()  # Θα εγείρει μια εξαίρεση για κωδικούς λάθους
        issues = response.json()
        # print(f"Αριθμός ζητημάτων για κατάσταση '{state}': {len(issues)}")
        return issues
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Για παράδειγμα: 400 Bad Request
    except Exception as err:
        print(f"Άλλο σφάλμα: {err}")  # Για άλλα σφάλματα


def main():
    all_issues = []
    for state in states:
        issues = get_issues(state)
        if issues:
            df = pd.json_normalize(issues)

            # Αφαίρεση των στηλών '$type' και 'project.$type'
            columns_to_drop = ["$type", "project.$type"]
            df = df.drop(columns=columns_to_drop, errors="ignore")

            # Μετονομασία των στηλών για καλύτερη αναγνωσιμότητα
            df = df.rename(
                columns={
                    "project.name": "project_name",
                    "state.name": "state_name",
                    "updated": "update_date",
                }
            )

            # Προσθήκη στήλης με το όνομα της κατάστασης
            df["state_name"] = state

            # Επιλογή συγκεκριμένων στηλών χωρίς 'creation_date'
            selected_columns = [
                "id",
                "summary",
                "project_name",
                "state_name",
                "update_date",
            ]
            df_selected = df[selected_columns]

            all_issues.append(df_selected)
        else:
            print(
                f"Δεν βρέθηκαν ζητήματα για κατάσταση '{state}' ή συνέβη κάποιο σφάλμα κατά την ανάκτηση."
            )

    if all_issues:
        complete_df = pd.concat(all_issues, ignore_index=True)
        # print("Ολοκληρωμένο DataFrame:")
        # print(complete_df)
    else:
        print("Δεν βρέθηκαν ζητήματα για καμία από τις καθορισμένες καταστάσεις.")
    complete_df = complete_df[complete_df.project_name == 'Elounda Market']
    complete_df["update_date"] = pd.to_datetime(complete_df["update_date"], unit="ms")
    complete_df["year"] = complete_df["update_date"].dt.year
    complete_df = complete_df[complete_df.year == datetime.now().year]
    df = complete_df.state_name.value_counts().to_frame()
    return df



