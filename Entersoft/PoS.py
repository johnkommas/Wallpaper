from SQL_FOLDER import fetch_data
from Files import plot


def get_Pos(path, path_b):
    # Εκτέλεση SQL ερωτήματος και φόρτωση δεδομένων
    query = "PoS.sql"
    df = fetch_data.get_sql_data(query)

    # Έλεγχος των συνθηκών για pos_a και pos_b
    pos_a = True
    pos_b = df.loc[df["POSID"] == "01655516", "Status"].eq("Εκκρεμής").any()

    # Λειτουργία για την κατασκευή της εικόνας
    def handle_image(pos_condition, offset):
        path_a = f"{path}/bad_pos.png" if pos_condition else f"{path}/good_pos.png"
        box_ = (2800 + offset, 50)
        plot.glue_image_general(path_a, path_b, box_, resize=.5)

    # Εικόνα για pos_a
    handle_image(pos_a, 0)

    # Εικόνα για pos_b
    handle_image(pos_b, 250)


