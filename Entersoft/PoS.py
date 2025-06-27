from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt
from Utilities import imessage
from SQL_FOLDER import fetch_data
import os
from Files import minimalist_write
from Sound_Pack import sound


def get_Pos(path, images, editables, font, multiple_data):
    # Εκτέλεση SQL ερωτήματος και φόρτωση δεδομένων
    query = ["PoS.sql", "Retail_PerPoint_Today_Count_Sales.sql"]

    df_retail = fetch_data.get_sql_data(query[1])
    # Ανάκτηση των τιμών για "TAMEIO Α" και "TAMEIO Β"
    RA = df_retail.loc[0, "TAMEIO Α"]  # Πρώτη γραμμή, στήλη "TAMEIO Α"
    RB = df_retail.loc[0, "TAMEIO Β"]  # Πρώτη γραμμή, στήλη "TAMEIO Β"

    df = fetch_data.get_sql_data(query[0])
    PDA_ID_A = "01655515"
    PDA_ID_B = "01655516"
    PDA_ID_A_2 = "01655517"
    # Έλεγχος των συνθηκών για pos_a και pos_b
    pos_a = df.loc[df["POSID"].isin([PDA_ID_A, PDA_ID_A_2]), "Status"].eq("Εκκρεμής").any()
    pos_b = df.loc[df["POSID"] == PDA_ID_B, "Status"].eq("Εκκρεμής").any()

    Card_Payments_A = df[(df["POSID"].isin([PDA_ID_A, PDA_ID_A_2])) & (df["Status"] == "Επιτυχημένη")].shape[0]
    Card_Payments_B = df[(df["POSID"] == PDA_ID_B) & (df["Status"] == "Επιτυχημένη")].shape[0]
    Card_Payments = [Card_Payments_A, Card_Payments_B]

    if pos_a or pos_b:
        text = "ΤΑΜΕΙΟ Α" if pos_a else "ΤΑΜΕΙΟ B"
        sound.get_notified()
        # imessage.send(text)
        imessage.mailme(text)

    if multiple_data == 3:
        # Στατιστικά για κάθε PoS
        df_pos_a = df[df["POSID"].isin([PDA_ID_A, PDA_ID_A_2])]
        data_to_text_pos_a = ""
        for status, count in zip(df_pos_a.Status.value_counts().index, df_pos_a.Status.value_counts()):
            data_to_text_pos_a = data_to_text_pos_a + f"{status[:2]}:{count} "

        df_pos_b = df[df["POSID"] == PDA_ID_B]
        data_to_text_pos_b = ""
        for status, count in zip(df_pos_b.Status.value_counts().index, df_pos_b.Status.value_counts()):
            data_to_text_pos_b = data_to_text_pos_b + f"{status[:2]}:{count} "

        data_to_text = [data_to_text_pos_a, data_to_text_pos_b]
        retail_per_point = [RA, RB]
        # print(retail_per_point)

        for image, editable in zip(images, editables):
            text_offset = 0
            for entry, retail  in zip(data_to_text, retail_per_point):
                editable.text((2480 + text_offset, 1800), f"RECEIPTS: {retail}", os.getenv("COLOR_A"), font=font)
                editable.text((2480 + text_offset, 1910), entry.upper(), os.getenv("COLOR_A"), font=font)  # Χρήση καθεμιάς εγγραφής
                text_offset += 1540

        # Λειτουργία για την κατασκευή της εικόνας
        def handle_image(pos_condition, offset, image, my_retail):
            path_a = f"{path}/bad_pos.png" if pos_condition else f"{path}/good_pos.png"
            box_ = (1980 + offset, 1780)
            box_polar = (1650 + offset, 1180)
            image = minimalist_write.paste_image(image, path_a, box_, resize=2)
            image = minimalist_write.paste_image(image, my_retail, box_polar, resize=3)

        for enum, (a, b) in enumerate(zip(Card_Payments, retail_per_point)):
            # print(f"Polar Chart {enum}, {a}, {b}")
            polar_chart(a, b, f"{path}/polar_chart_{enum}.png")

        for image in images:
            # Εικόνα για pos_a
            handle_image(pos_a, 0, image, f"{path}/polar_chart_0.png")
            # Εικόνα για pos_b
            handle_image(pos_b, 1550, image, f"{path}/polar_chart_1.png")


def polar_chart(cards, receipts, file, title="ΠΟΣΟΣΤΟ ΣΥΝΑΛΛΑΓΩΝ ΜΕ ΚΑΡΤΑ"):
    colors = [os.getenv("COLOR_A"), os.getenv("COLOR_B"), os.getenv("COLOR_A")]  # Green, Orange, Red
    ranges = [25, 50, 25]  # Ranges for low, medium and high

    fig = plt.figure(figsize=(8, 8), dpi=450)
    ax = fig.add_subplot(projection="polar")

    # Create bars for each category (low, medium, high), but now starting from right
    start = 0
    bar_widths = []
    for i, (col, rng) in enumerate(
            zip(colors[::-1], ranges[::-1])
    ):  # Reversed colors and ranges
        width = rng / 100 * np.pi  # Ranges are out of 100%
        bar_widths.append(width)
        ax.bar(
            start,
            height=1,
            width=width,
            bottom=2,
            linewidth=3,
            edgecolor="none",
            color=col,
            align="edge",
        )
        start += width

    # Get the percentage, for  50% of the 'medium' range
    if receipts in [0, None] :  # Handle 0 receipts
        percent = 0  # Or set it to a default value
    else:
        percent = cards / receipts

    angle = np.pi - percent * np.pi
    text = f"{round(100 * percent)}%"

    # Determine arrow color
    if angle < bar_widths[0]:
        color = colors[2]
    elif angle < sum(bar_widths[:2]):
        color = colors[1]
    else:
        color = colors[0]

    plt.annotate(
        text,
        xytext=(0, 0),
        xy=(angle, 2.0),
        arrowprops=dict(arrowstyle="wedge, tail_width=0.8", color=color, shrinkA=0),
        bbox=dict(boxstyle="circle", facecolor=color, linewidth=1.0, edgecolor=color),
        fontsize=40,
        color=os.getenv("COLOR_C"),
        ha="center",
    )
    # Add the title at the bottom of the chart
    # plt.figtext(
    #     0.5,  # X-coordinate of the title (centered at the middle)
    #     0.01,  # Y-coordinate of the title (just above the bottom edge)
    #     title,  # The title text to display
    #     fontsize=12,  # Font size
    #     color="black",  # Title text color
    #     ha="center",  # Horizontal alignment ("center" aligns in the middle)
    # )

    ax.set_axis_off()
    plt.savefig(file, transparent=True, bbox_inches="tight", dpi=450)
    plt.clf()
    plt.cla()
    plt.close()

def cancelled_transactions(images, editables, font, placement):
    df = fetch_data.get_sql_data("POSFailedTransactions.sql")
    # Αποθήκευση τιμών της πρώτης γραμμής
    year = df['Year'].iloc[0]
    total = df['TotalTransactions'].iloc[0]
    canceled = df['CanceledTransactions'].iloc[0]
    success = df['SuccededTransactions'].iloc[0]
    percent = df['CanceledPercent'].iloc[0]
    s_percent = df['SuccededPercent'].iloc[0]

    # Φόρματ με τελεία για τα χιλιάδες
    total_str = f"{total:,}".replace(",", ".")
    canceled_str = f"{canceled:,}".replace(",", ".")
    success_str = f"{success:,}".replace(",", ".")

    for image, editable in zip(images, editables):
        editable.text(placement, f"Card Transactions Attempts of: {year} | Total: {total_str} | Succeeded: {success_str} ({s_percent}%)| Failed: {canceled_str} ({percent}%)", os.getenv("COLOR_A"), font=font)

def cash_credit(images, editables, font, placement):
    df = fetch_data.get_sql_data("CashCredit.sql")
    total = df['TotalCount'].iloc[0]
    cash = df['CashCount'].iloc[0]
    credit = df['CreditCount'].iloc[0]
    cashP = df['CashPercent'].iloc[0]
    creditP = df['CreditPercent'].iloc[0]

    total_str = f"{total:,}".replace(",", ".")
    cash_str = f"{cash:,}".replace(",", ".")
    credit_str = f"{credit:,}".replace(",", ".")

    for image, editable in zip(images, editables):
        editable.text(placement, f"Retail Transactions of: {datetime.now().year} | Total: {total_str} | Cash: {cash_str} - ({cashP}%)  | Card: {credit_str} - ({creditP}%)", os.getenv("COLOR_A"), font=font)
