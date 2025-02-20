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


def create_sankey(data, path):
    """
    Δημιουργεί ένα Sankey Diagram με προσαρμοσμένα χρώματα για κόμβους και γραμμές (links).

    :param data: Λίστα λεξικών με τα δεδομένα (π.χ. MONTH, TYPE, PdaId, Katahorimeno, DOCS, LINES).
    :param path: Το μονοπάτι για αποθήκευση του Sankey Diagram.
    """
    import pandas as pd
    from plotly import graph_objects as go

    # Μετατροπή δεδομένων σε DataFrame
    df = pd.DataFrame(data)

    # Υπολογισμός συνολικών τιμών ανά μήνα
    month_totals = (
        df.groupby("MONTH").agg({"DOCS": "sum", "LINES": "sum"}).reset_index()
    )
    df["MONTH"] = df["MONTH"].apply(
        lambda x: f"{x}<br>({month_totals.loc[month_totals['MONTH'] == x, 'DOCS'].values[0]}, "
                  f"{month_totals.loc[month_totals['MONTH'] == x, 'LINES'].values[0]})"
    )

    # Υπολογισμός συνολικών τιμών ανά τύπο
    type_totals = df.groupby("TYPE").agg({"DOCS": "sum", "LINES": "sum"}).reset_index()
    df["TYPE"] = df["TYPE"].apply(
        lambda x: f"{x[:4]}<br>({type_totals.loc[type_totals['TYPE'] == x, 'DOCS'].values[0]}, "
                  f"{type_totals.loc[type_totals['TYPE'] == x, 'LINES'].values[0]})"
    )

    # Δημιουργία μοναδικών κόμβων με βάση τα δεδομένα
    unique_months = sorted(df["MONTH"].unique())
    all_nodes = list(unique_months) + list(
        pd.concat([df["TYPE"], df["PdaId"], df["Katahorimeno"]]).unique()
    )

    # Δομή για index mapping των κόμβων
    node_indices = {node: idx for idx, node in enumerate(all_nodes)}

    # Δημιουργία πηγών (sources), προορισμών (targets) και τιμών (values)
    sources, targets, values = [], [], []

    # Συνδέσεις από TYPE -> PdaId
    for _, row in df.iterrows():
        sources.append(node_indices[row["TYPE"]])
        targets.append(node_indices[row["MONTH"]])
        values.append(1)

    # Συνδέσεις από PdaId -> MONTH
    # for _, row in df.iterrows():
    #     sources.append(node_indices[row["PdaId"]])
    #     targets.append(node_indices[row["MONTH"]])
    #     values.append(1)

    # Δημιουργία παλέτας χρωμάτων
    # Χρώματα κόμβων (επαναλαμβανόμενη παλέτα)
    color_palette = [
        "#1f77b4",  # Μπλε
        "#ff7f0e",  # Πορτοκαλί
        "#2ca02c",  # Πράσινο
        "#d62728",  # Κόκκινο
        "#9467bd",  # Μωβ
        "#8c564b",  # Καφέ
        "#e377c2",  # Ροζ
        "#7f7f7f",  # Γκρι
        "#bcbd22",  # Κίτρινο-Λάιμ
        "#17becf",  # Γαλάζιο
    ]

    # Αντιστοίχιση χρωμάτων κόμβων
    node_colors = [
        color_palette[idx % len(color_palette)] for idx in range(len(all_nodes))
    ]

    # Δημιουργία χρωμάτων links που βασίζονται στην πηγή τους
    link_colors = [node_colors[source] for source in sources]

    # Δημιουργία Sankey Diagram
    fig = go.Figure(
        go.Sankey(
            node=dict(
                pad=15,
                thickness=1,
                line=dict(color="black", width=0.5),
                label=all_nodes,  # Ετικέτες κόμβων
                color=node_colors,  # Χρώματα κόμβων
            ),
            link=dict(
                source=sources,  # Πηγές (indexes κόμβων)
                target=targets,  # Προορισμοί (indexes κόμβων)
                value=values,  # Τιμές συνδέσεων
                color=link_colors,  # Χρώματα συνδέσεων βασισμένα στους κόμβους
            ),
        )
    )

    # Ρυθμίσεις εμφάνισης
    fig.update_layout(
        title_text="Sankey Diagram - Προσαρμοσμένα Χρώματα",
        font=dict(size=12, color="black"),
        paper_bgcolor="#FFFFFF",  # Λευκό φόντο
        width=900,
        height=1800,
    )

    # Αποθήκευση Sankey Diagram ως εικόνα
    fig.write_image(path, scale=2)


def run(path_a, images):
    df = get_Pos()
    box_ = (750, 2200)
    create_sankey(df, path_a)
    # for image in images:
    #     pass