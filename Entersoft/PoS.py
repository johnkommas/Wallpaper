from SQL_FOLDER import fetch_data
import os
from Files import minimalist_write


def get_Pos(path, images, editables, font):
    # Εκτέλεση SQL ερωτήματος και φόρτωση δεδομένων
    query = "PoS.sql"
    df = fetch_data.get_sql_data(query)

    # Έλεγχος των συνθηκών για pos_a και pos_b
    pos_a = False
    pos_b = df.loc[df["POSID"] == "01655516", "Status"].eq("Εκκρεμής").any()

    # Στατιστικά για κάθε PoS
    # df_pos_a = df[df["POSID"] == "???????"]
    data_to_text_pos_a = "Επ:000 Απ:00"
    # for status, count in zip(df_pos_a.Status.value_counts().index, df_pos_a.Status.value_counts()):
    #     data_to_text_pos_b = data_to_text_pos_b + f"{count} "

    df_pos_b = df[df["POSID"] == "01655516"]
    data_to_text_pos_b = ""
    for status, count in zip(df_pos_b.Status.value_counts().index, df_pos_b.Status.value_counts()):
        data_to_text_pos_b = data_to_text_pos_b + f"{status[:2]}:{count} "

    data_to_text = [data_to_text_pos_a, data_to_text_pos_b]

    for image, editable in zip(images, editables):
        text_offset = 0
        for entry in data_to_text:
            editable.text(
                (2480 + text_offset, 160), entry, os.getenv("COLOR_A"), font=font
            )  # Χρήση καθεμιάς εγγραφής
            text_offset += 1540

    # Λειτουργία για την κατασκευή της εικόνας
    def handle_image(pos_condition, offset, image):
        path_a = f"{path}/bad_pos.png" if pos_condition else f"{path}/good_pos.png"
        box_ = (1980 + offset, 0)
        image = minimalist_write.paste_image(image, path_a, box_, resize=2)

    for image in images:
        # Εικόνα για pos_a
        handle_image(pos_a, 0, image)
        # Εικόνα για pos_b
        handle_image(pos_b, 1550, image)
