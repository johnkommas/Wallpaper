from SQL_FOLDER import fetch_data
import os
from Files import plot
import pandas as pd
import plotly.graph_objects as go


def get_Pos():
    # Εκτέλεση SQL ερωτήματος και φόρτωση δεδομένων
    query = "PDA.sql"
    df = fetch_data.get_sql_data(query)
    # print(df)
    return df


def create_sankey(i, data, path):
    """
    Δημιουργεί ένα Sankey Diagram από δεδομένα που περιλαμβάνουν τις στήλες:
    MONTH, TYPE, PdaId, Katahorimeno, DOCS, LINES.

    :param i: Δείκτης για το τρέχον διάγραμμα (π.χ. πολλαπλά Sankey σε loop).
    :param data: Λίστα λεξικών με τα δεδομένα, όπου κάθε λεξικό αντιπροσωπεύει μία γραμμή.
    :param path: Το μονοπάτι για την αποθήκευση του Sankey διαγράμματος.
    """
    # Αποκτάμε τα χρώματα από το περιβάλλον (default χρώματα αν δεν έχουν οριστεί)
    color_a = os.getenv("COLOR_A") or "#003049"  # Περιοδικό χρώμα 1 (π.χ. μπλε)
    color_c = os.getenv("COLOR_C") or "#FDF0D5"  # Περιοδικό χρώμα 2 (π.χ. κίτρινο)

    # Μετατροπή δεδομένων σε DataFrame
    df = pd.DataFrame(data)

    month_totals = df.groupby("MONTH").agg({"DOCS": "sum", "LINES": "sum"}).reset_index()

    # Ενημέρωση κάθε μήνα με τις τιμές των συνόλων (DOCS και LINES)
    df["MONTH"] = df["MONTH"].apply(
        lambda x: f"{x}<br>({month_totals.loc[month_totals['MONTH'] == x, 'DOCS'].values[0]}, "
                  f"{month_totals.loc[month_totals['MONTH'] == x, 'LINES'].values[0]})"
    )

    # Υπολογισμός του συνόλου `DOCS` και `LINES` ανά τύπο (TYPE)
    type_totals = df.groupby("TYPE").agg({"DOCS": "sum", "LINES": "sum"}).reset_index()

    # Ενημέρωση κάθε τύπου με τις τιμές των συνόλων (DOCS και LINES)
    df["TYPE"] = df["TYPE"].apply(
        lambda x: f"{x[:4]}.<br>({type_totals.loc[type_totals['TYPE'] == x, 'DOCS'].values[0]}, "
                  f"{type_totals.loc[type_totals['TYPE'] == x, 'LINES'].values[0]})"
    )

    # Εξασφαλίζουμε ότι η στήλη MONTH είναι μοναδική και ταξινομημένη ώστε να μπορούμε να εναλλάξουμε τα χρώματα σωστά
    unique_months = df["MONTH"].unique()
    unique_months.sort()

    # Δημιουργία χρωμάτων κόμβων και κειμένου για κάθε ΜΗΝΑ
    month_colors = {
        month: (color_a if idx % 2 == 0 else color_c)
        for idx, month in enumerate(unique_months)
    }
    text_colors = {
        month: (color_c if idx % 2 == 0 else color_a)
        for idx, month in enumerate(unique_months)
    }

    # Εξασφαλίζουμε ότι η στήλη MONTH είναι μοναδική και ταξινομημένη
    unique_months = sorted(df["MONTH"].unique())  # Ταξινομημένοι μήνες

    # Δημιουργία όλων των κόμβων με ταξινομημένους τους μήνες να είναι πρώτοι
    all_nodes = list(unique_months) + list(
        pd.concat(
            [
                df["TYPE"],
                df["PdaId"],
                df["Katahorimeno"],
                df["DOCS"].astype(str),
                df["LINES"].astype(str),
            ]
        ).unique()
    )

    # Δημιουργία λεξικού για mapping των κόμβων σε indexes
    node_indices = {node: idx for idx, node in enumerate(all_nodes)}

    # Sankey συνδέσεις: sources και targets
    sources = []
    targets = []
    values = []

    # Ανάμεσα στα MONTH -> TYPE
    for _, row in df.iterrows():
        sources.append(node_indices[row["TYPE"]])
        targets.append(node_indices[row["MONTH"]])
        values.append(1)

    # # Ανάμεσα στα TYPE -> PdaId
    # for _, row in df.iterrows():
    #     sources.append(node_indices[row["TYPE"]])
    #     targets.append(node_indices[row["PdaId"]])
    #     values.append(1)
    #
    # # Ανάμεσα στα PdaId -> Katahorimeno
    # for _, row in df.iterrows():
    #     sources.append(node_indices[row["PdaId"]])
    #     targets.append(node_indices[row["Katahorimeno"]])
    #     values.append(1)

    # Εφαρμογή των χρωμάτων στους κόμβους ανάλογα με τη στήλη MONTH
    node_colors = []
    for node in all_nodes:
        if node in month_colors:  # Χρήση του χρώματος του ΜΗΝΑ
            node_colors.append(month_colors[node])
        else:
            node_colors.append("#D3D3D3")  # Default γκρι για μη-MONTH κόμβους

    # Δημιουργία Sankey Diagram
    fig = go.Figure(
        go.Sankey(
            node=dict(
                pad=15,
                thickness=1,
                line=dict(color=color_a, width=0.5),
                label=list(all_nodes),
                color="rgba(0,0,0,0.05)",  # Χρώματα κόμβων ανά μήνα
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                color="rgba(0,0,0,0.05)",  # Σταθερό χρώμα για τα links
            ),
        )
    )

    # Ενημέρωση layout για εναλλάξ χρώματα στο κείμενο
    fig.update_layout(
        width=370,  # Προσαρμοσμένο πλάτος
        height=760,  # Προσαρμοσμένο ύψος
        paper_bgcolor="rgba(0,0,0,0)",  # Διαφάνεια φόντου
        font=dict(color=color_c, size=10 ),  # Σταθερό χρώμα για το κείμενο ολόκληρου του layout
    )

    # Αποθήκευση ως εικόνα
    fig.write_image(path, scale=6)


def run(path_a, path, file_in, time):
    df = get_Pos()
    box_ = (750, 2200)
    for i in range(1, 4):
        create_sankey(i, df, path_a)
        # plot.glue_image_general(path_a, f"{path}/TEMP/{file_in}_{time}_{i}.jpg", box_,)