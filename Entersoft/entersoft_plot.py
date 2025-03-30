import os
from PIL import Image
from Files import minimalist_write
import matplotlib.pyplot as plt
import numpy as np


def monthly_turnover_donut(df, path_a, color, i):
    """
    Visualize Number of Hackers (Unique IP Count) using a Half Donut Chart.
    Percent values follow the donut's curve with automatically calculated font colors
    for better visibility (closer to the edge of the circle).
    """
    # Color Palette Setup
    color_pallete_a = os.getenv("COLOR_A")
    highlight_color = os.getenv("COLOR_C")

    sorted_data = df.sort_values(by="TurnOver", ascending=False)
    sorted_data = sorted_data.head(6)

    # Data for Chart
    turn_over = sorted_data["TurnOver"]

    # Determine colors
    colors = [
        color if count == max(turn_over) else color_pallete_a for count in turn_over
    ]

    # Add a dummy slice for the empty half
    turn_over = turn_over.tolist() + [sum(turn_over)]
    month_map = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }

    labels = [
        f"{month_map[row['FiscalMonth']]}\n"
        f"{row['TurnOver']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        + "€"
        for _, row in sorted_data.iterrows()
    ] + [""]

    colors.append("none")  # Make the dummy slice transparent

    # Calculate percentages
    percentages = (np.array(turn_over) / np.sum(turn_over)) * 100

    plt.figure(figsize=(8, 8), dpi=450)  # Higher resolution

    # Create the half-donut chart
    wedges, texts, autotexts = plt.pie(
        turn_over,
        labels=labels,
        explode=[0.01] * len(turn_over),
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops=dict(width=0.4),
        autopct=lambda pct: "",
        textprops={"fontsize": 18},
    )

    # Move percentages closer to the edge
    for enum, (wedge, count, pct) in enumerate(zip(wedges,turn_over, percentages)):
        if enum < len(turn_over) - 1:  # Αγνοούμε το dummy μέρος
            x, y = wedge.center  # Κέντρο wedge
            angle = (wedge.theta2 + wedge.theta1) / 2  # Γωνία wedge
            x = np.cos(np.radians(angle)) * 0.8  # Υπολογισμός x
            y = np.sin(np.radians(angle)) * 0.8  # Υπολογισμός y
            # Επιλέγουμε χρώμα για το max κομμάτι
            text_color = (
                color_pallete_a
                if (count == max(turn_over[:-1]) and i == 3)
                else highlight_color
            )
            plt.text(
                x,
                y,
                f"{pct * 2:.1f}%",
                ha="center",
                va="center",
                fontsize=18,
                color=text_color,
            )

    # Add a transparent circle in the center
    center_circle = plt.Circle((0, 0), 0.60, fc="none")
    plt.gca().add_artist(center_circle)

    # Ensure equal aspect
    plt.axis("equal")

    # Save the figure
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
        width - 2000, 0
    )  # Ξεκίνα 1500 pixels πριν το τέλος ή 0 αν η εικόνα είναι μικρότερη
    end_x = width  # Μέχρι το τέλος της εικόνας

    # Κόψιμο της περιοχής που θέλουμε
    cropped_image = image.crop((start_x, 0, end_x, height))

    # Αποθήκευση της κομμένης εικόνας
    cropped_image.save(output_path)


def plot_run_monthly_turnover(dataframe, path, images):
    for i, image in enumerate(images, start=1):
        _path = f"{path}/monthly_turn_over.png"
        colors = [None, os.getenv("COLOR_A"), os.getenv("COLOR_B"), os.getenv("COLOR_C")]
        logo_path = f"{path}/gears_{i}.png"
        # print(f"TEST {i}")
        monthly_turnover_donut(dataframe, _path, colors[i], i)
        # y+750
        ya = 2520
        image = minimalist_write.paste_image(image, _path, (150, ya), 2)
        image = minimalist_write.paste_image(image, logo_path, (150, ya + 750), 2)
