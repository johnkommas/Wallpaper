import os

import numpy as np
from matplotlib import pyplot as plt


def monthly_turnover_donut(df, path_a, color, i):
    """
    Visualize Number of Hackers (Unique IP Count) using a Donut Chart.
    Percent values follow the donut's curve with automatically calculated font colors for better visibility.
    """

    # Color Palette Setup
    color_pallete_a = os.getenv("COLOR_A")  # Dark Blue (Main color for slices)
    highlight_color = os.getenv( "COLOR_C")  # Light Crème (Highlight color for the highest slice)

    sorted_data = df.sort_values(by="TurnOver", ascending=False)

    # Data for Chart
    turn_over = sorted_data["TurnOver"]

    # Determine colors: Highlight the API with the highest count
    colors = [
        color if count == max(turn_over) else color_pallete_a
        for count in turn_over
    ]

    # Font setup for annotations (bigger and bold)
    percentage_font_size = 18  # Adjusted for better visibility
    month_map = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    labels = (
            sorted_data["FiscalMonth"]
            .map(month_map)  # Μετατροπή του αριθμού μήνα στο όνομα του μήνα
            + "\n"  # Δημιουργία νέας γραμμής
            + sorted_data["TurnOver"].apply(
        lambda x: f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".") + "€")
    )

    # Figure Setup with Transparency
    plt.figure(figsize=(7, 7), dpi=350)  # Higher resolution

    # Calculate percentages
    percentages = (turn_over / np.sum(turn_over)) * 100

    # Find the index of the largest slice
    max_index = np.argmax(percentages)

    # Calculate rotation angle for the largest slice to start in the top-right
    offset = sum(percentages[:max_index]) + percentages[max_index] / 2
    startangle = 330 - offset  # Rotating to place it in the top-right

    # Create the donut chart with autopct to display percentages
    wedges, texts, autotexts = plt.pie(
        turn_over,
        labels=labels,
        explode=[0.01] * len(turn_over),  # Small gaps
        colors=colors,
        startangle=startangle,  # Start from top-center
        autopct="%1.1f%%",  # Automatically calculate and display percentages
        textprops={
            "fontsize": percentage_font_size
        },  # Font size for labels and percentages
        pctdistance=0.8,  # Adjust percentage text position closer to the center
    )
    # Configure the percentage text (inside the slices)
    for count, autotext in zip(turn_over, autotexts):
        # Larger, bold text for percentage annotation
        autotext.set_fontsize(percentage_font_size)
        # autotext.set_fontweight("bold")
        # Adjust font color
        if (count == max(turn_over)) and (i == 3):
            autotext.set_color(color_pallete_a)  # Default for the max slice
        else:
            autotext.set_color(highlight_color)  # Light crème for non-max slices

    # Add a colored circle at the center to create a donut effect
    center_circle = plt.Circle((0, 0), 0.60, fc=os.getenv("COLOR_BG"))  # Custom color
    plt.gca().add_artist(center_circle)

    # Save Image
    plt.tight_layout()
    plt.savefig(path_a, transparent=True, dpi=350)  # Save as high-quality image
    plt.close()
