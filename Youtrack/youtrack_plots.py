import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def cards_donut(df, path_a, color):

    # REMOVE Fixed
    df = df[df.index != "Fixed"]
    # Χρώματα παλέτας
    color_pallete_a = "#0D1B2A"  # Σκούρο μπλε (κύριο χρώμα για τα κομμάτια)
    highlight_color = "#D7C9AA"  # Ανοιχτό μπεζ για τη μεγαλύτερη φέτα

    # Δεδομένα
    labels = df.index.tolist()  # Κατηγορίες (labels)
    card_count = df["count"].tolist()  # Τιμές για κάθε κατηγορία (από το DataFrame)

    # Προσθήκη dummy τιμής για το δεξί ημικύκλιο
    labels.append("")  # Dummy label για το κενό
    card_count.append(sum(card_count))  # Dummy τιμή ίση με το σύνολο ώστε να καλύπτει το δεξί μέρος

    # Χρώματα (dummy wedge παίρνει "none" για να είναι αόρατο)
    colors = [
        color if count == max(card_count[:-1]) else color_pallete_a for count in card_count
    ]
    colors[-1] = "none"  # Το dummy wedge δεν έχει χρώμα

    # Δημιουργία ντόνατ διαγράμματος
    wedges, texts = plt.pie(
        card_count,
        labels=labels,
        explode=[0.01] * len(card_count),  # Μικρό ξεκόλλημα για εφέ
        colors=colors,
        startangle=90,  # Ξεκινάει από την κορυφή και περιστρέφεται
        counterclock=False,  # Δεξιόστροφη φορά
        wedgeprops=dict(width=0.4),  # Πάχος ντόνατ
        textprops={"fontsize": 12},
    )

    # Προσθήκη απόλυτων αριθμών πάνω από τις φέτες (χωρίς υπολογισμό ποσοστού)
    for i, wedge in enumerate(wedges):
        if i < len(card_count) - 1:  # Αγνοούμε το dummy μέρος
            x, y = wedge.center  # Κέντρο wedge
            angle = (wedge.theta2 + wedge.theta1) / 2  # Γωνία wedge
            x = np.cos(np.radians(angle)) * 0.8  # Υπολογισμός x
            y = np.sin(np.radians(angle)) * 0.8  # Υπολογισμός y
            plt.text(
                x,
                y,
                f"{card_count[i]}",  # Ακριβής αριθμός από το DataFrame
                ha="center",
                va="center",
                fontsize=10,
                color="white"
            )

    # Κεντρικός κύκλος για το σχεδιαστικό εφέ
    center_circle = plt.Circle((0, 0), 0.60, fc="#415a77")  # Χρώμα διατηρούμε όπως θέλεις
    fig = plt.gcf()
    plt.gca().add_artist(center_circle)

    # Ισομερής εμφάνιση
    plt.axis("equal")

    # Αποθήκευση της εικόνας
    plt.tight_layout()
    plt.savefig(path_a, transparent=True, dpi=450)
    plt.close()
    split_image_in_half(path_a, path_a)


def split_image_in_half(image_path, output_path):
    # Φόρτωση της εικόνας
    image = Image.open(image_path)

    # Διαστάσεις της εικόνας
    width, height = image.size
    # print(f"Αρχικές διαστάσεις εικόνας: {width}x{height}")

    # Υπολογισμός του σημείου έναρξης (για 1500 pixels πλάτος από τα δεξιά)
    start_x = max(
        width - 1620, 0
    )  # Ξεκίνα 1500 pixels πριν το τέλος ή 0 αν η εικόνα είναι μικρότερη
    end_x = width  # Μέχρι το τέλος της εικόνας

    # Κόψιμο της περιοχής που θέλουμε
    cropped_image = image.crop((start_x, 0, end_x, height))

    # Αποθήκευση της κομμένης εικόνας
    cropped_image.save(output_path)


