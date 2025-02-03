import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.colors as mcolors  # For brightness calculation
import plotly.graph_objects as go


def time_series_analysis(df, path_a, loop_counter):
    """
    Δημιουργεί ένα Time Series Analysis για τη συχνότητα επιθέσεων ανά ώρα.
    Εξάγουμε ένα διάγραμμα τύπου line όπου εμφανίζεται η δραστηριότητα στον χρόνο.
    """
    # SETUP COLORS
    color = ["#778DA9", "#0D1B2A", "#778DA9", "#D7C9AA",]


    # Συνδυασμός ημερομηνίας και ώρας για δημιουργία πλήρους timestamp
    df["Timestamp"] = pd.to_datetime(
        df["Date"] + " " + df["Time"], format="%Y.%d.%m %H:%M:%S"
    )

    # Ομαδοποίηση ανά ώρα (resample για καταμέτρηση ανά ώρα)
    attack_counts = df.resample("H", on="Timestamp").size()

    # Γράφημα χρονοσειράς
    plt.figure(figsize=(17, 6), dpi=300, facecolor="#1a376e")
    attack_counts.plot(
        kind="line",
        marker="o",
        color=color[1],
        title=f"{len(df)} Attacks Over Time "
    )
    # plt.xlabel("Time", fontsize=12, color=color_pallete_b)  # Προσαρμογή στα labels
    # plt.ylabel("Number of Attacks", fontsize=12, color=color_pallete_b)

    # Αφαίρεση περιγράμματος (box off)
    ax = plt.gca()  # Λήψη του τρέχοντος άξονα
    ax.spines["top"].set_visible(False)  # Αφαίρεση κορυφής
    ax.spines["right"].set_visible(False)  # Αφαίρεση δεξιού περιγράμματος
    ax.spines["left"].set_visible(False)  # Αφαίρεση αριστερού περιγράμματος
    ax.spines["bottom"].set_visible(False)  # Αφαίρεση κάτω περιγράμματος

    # Αφαίρεση ticks (Κλίμακα στο διάγραμμα)
    ax.tick_params(left=False, bottom=False)  # Απενεργοποίηση ticks

    # Αποθήκευση γραφήματος χωρίς grid
    plt.tight_layout()  # Εξασφαλίζει σωστή διαμόρφωση στοιχείων
    plt.savefig(path_a, transparent=True, dpi=300)
    plt.close()


    return attack_counts


def analyze_top_ips(df, top_n=5):
    """
    Εντοπίζει τα πιο συχνά χρησιμοποιημένα IPs και εμφανίζει τα αποτελέσματα
    σε μορφή horizontal bar chart.
    """
    # Αναγνώριση πιο συχνών Public IPs
    frequent_ips = df["Public IP"].value_counts().head(top_n)

    # Γράφημα bar (horizontal)
    plt.figure(figsize=(10, 6))
    frequent_ips.plot(
        kind="barh",
        color="orange",
        title=f"Top {top_n} Public IPs Attempting Penetration",
    )
    plt.xlabel("Number of Attacks")
    plt.ylabel("Public IP")
    plt.grid(axis="x")
    plt.show()

    return frequent_ips


def analyze_targeted_apis(df, top_n=5):
    """
    Εξετάζει ποιες APIs στοχεύονται περισσότερο.
    Εμφανίζει τα αποτελέσματα με horizontal bar chart για τις top-n APIs.
    """
    # Αναγνώριση πιο στοχευμένων APIs
    targeted_apis = df["Api"].value_counts().head(top_n)

    # Γράφημα bar (horizontal)
    plt.figure(figsize=(10, 6))
    targeted_apis.plot(kind="barh", color="purple", title=f"Top {top_n} Targeted APIs")
    plt.xlabel("Number of Attacks")
    plt.ylabel("API")
    plt.grid(axis="x")
    plt.show()

    return targeted_apis


def analyze_ips_ports_apis(df):
    """
    Εξετάζει τη συσχέτιση μεταξύ των Public IPs, των Ports και των APIs.
    Επιστρέφει έναν συγκεντρωτικό πίνακα (grouped results).
    """
    # Καθαρισμός και δημιουργία αναφοράς
    ip_port_api_analysis = (
        df.groupby(["Public IP", "Port", "Api"]).size().reset_index(name="Count")
    )

    # Εμφάνιση των αποτελεσμάτων με βάση αριθμό επιθέσεων
    sorted_analysis = ip_port_api_analysis.sort_values(by="Count", ascending=False)

    # Επιστροφή του πίνακα
    return sorted_analysis


def analyze_repeated_patterns(df):
    """
    Εξετάζει IPs που επιχειρούν συχνά σε πολλαπλά Ports ή APIs.
    Εμφανίζει έναν πίνακα με τα πιο "επίμονα" IPs.
    """
    # Εξετάστε πόσα μοναδικά Ports έχουν στοχεύσει από το ίδιο Public IP
    ip_multi_port = (
        df.groupby("Public IP")["Port"]
        .nunique()
        .reset_index(name="Unique Ports Targeted")
    )

    # Εξετάστε πόσα μοναδικά APIs έχουν στοχεύσει τα ίδια IPs
    ip_multi_api = (
        df.groupby("Public IP")["Api"]
        .nunique()
        .reset_index(name="Unique APIs Targeted")
    )

    # Συνένωση αποτελεσμάτων
    merged_patterns = pd.merge(ip_multi_port, ip_multi_api, on="Public IP")

    # Ταξινόμηση κατά μέγιστο αριθμό επιθέσεων
    sorted_patterns = merged_patterns.sort_values(
        by=["Unique Ports Targeted", "Unique APIs Targeted"], ascending=False
    )

    return sorted_patterns


def create_heatmap(df):
    """
    Δημιουργία Heatmap για την κατανομή επιθέσεων ανά ώρα και ημερομηνία.
    """
    # Απόσπαση ώρας
    df["Hour"] = df["Time"].str.split(":").str[0]

    # Δημιουργία pivot table για heatmap
    heatmap_data = df.pivot_table(
        index="Hour", columns="Date", values="Api", aggfunc="count", fill_value=0
    )

    # Heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="d")
    plt.title("Attack Distribution by Hour and Date")
    plt.xlabel("Date")
    plt.ylabel("Hour")
    plt.show()


def visualize_repeated_patterns(df, top_n=5):
    """
    Δημιουργεί ένα stacked bar chart για επίμονες IPs που στοχεύουν πολλαπλά Ports & APIs.
    """
    # Εξετάστε τα μοναδικά Ports και APIs που στοχεύονται από κάθε IP
    ip_multi_port = (
        df.groupby("Public IP")["Port"]
        .nunique()
        .reset_index(name="Unique Ports Targeted")
    )
    ip_multi_api = (
        df.groupby("Public IP")["Api"]
        .nunique()
        .reset_index(name="Unique APIs Targeted")
    )

    # Συνένωση δεδομένων
    combined_data = pd.merge(ip_multi_port, ip_multi_api, on="Public IP")
    combined_data = combined_data.sort_values(
        by=["Unique Ports Targeted", "Unique APIs Targeted"], ascending=False
    ).head(top_n)

    # Γράφημα bar (stacked)
    plt.figure(figsize=(12, 7))
    plt.barh(
        combined_data["Public IP"],
        combined_data["Unique Ports Targeted"],
        color="skyblue",
        label="Unique Ports",
    )
    plt.barh(
        combined_data["Public IP"],
        combined_data["Unique APIs Targeted"],
        color="darkblue",
        left=combined_data["Unique Ports Targeted"],
        label="Unique APIs",
    )

    plt.title(f"Top {top_n} Persistent Attackers: Ports vs APIs")
    plt.xlabel("Count")
    plt.ylabel("Public IP")
    plt.legend()
    plt.grid(axis="x")
    plt.show()

    return combined_data


def visualize_ips_ports_apis(df, top_n=5):
    """
    Αναλύει και δημιουργεί ένα bubble chart για τις σχέσεις Public IPs, Ports, και APIs.
    """
    # Ομαδοποίηση Public IPs -> Ports -> APIs
    ip_port_api_analysis = (
        df.groupby(["Public IP", "Port", "Api"]).size().reset_index(name="Count")
    )

    # Επιλογή των κορυφαίων συνδυασμών
    ip_port_api_analysis = ip_port_api_analysis.sort_values(
        by="Count", ascending=False
    ).head(top_n)

    # Δημιουργία γραφήματος
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        ip_port_api_analysis["Port"],
        ip_port_api_analysis["Api"],
        s=ip_port_api_analysis["Count"] * 10,  # Μέγεθος φούσκας: πλήθος επιθέσεων
        alpha=0.6,
        c=ip_port_api_analysis["Count"],  # Χρώμα ανάλογα του "Count"
        cmap="viridis",
    )

    # Προσθήκη ετικετών
    for i, row in ip_port_api_analysis.iterrows():
        plt.text(row["Port"], row["Api"], row["Public IP"], fontsize=8, ha="right")

    # Τίτλοι
    plt.title(
        f"Bubble Chart for Relationship between Public IPs, Ports, and APIs (Top {top_n})"
    )
    plt.xlabel("Port")
    plt.ylabel("API")
    plt.colorbar(scatter, label="Number of Attacks")
    plt.grid(alpha=0.5)
    plt.show()

    return ip_port_api_analysis


def visualize_bidirectional_targets(df, top_n=5):
    """
    Δημιουργεί ένα bidirectional bar chart για να συγκρίνει στόχους μεταξύ
    Ports και APIs ανά Public IP.
    """
    # Συγκέντρωση δεδομένων για Ports και APIs
    ip_ports = (
        df.groupby("Public IP")["Port"]
        .nunique()
        .reset_index(name="Unique Ports Targeted")
    )
    ip_apis = (
        df.groupby("Public IP")["Api"]
        .nunique()
        .reset_index(name="Unique APIs Targeted")
    )

    # Συνένωση δεδομένων
    combined_data = pd.merge(ip_ports, ip_apis, on="Public IP")
    combined_data = combined_data.sort_values(
        by=["Unique Ports Targeted", "Unique APIs Targeted"], ascending=False
    ).head(top_n)

    # Δημιουργία bidirectional bar chart
    plt.figure(figsize=(12, 7))
    plt.barh(
        combined_data["Public IP"],
        combined_data["Unique Ports Targeted"],
        color="skyblue",
        label="Unique Ports",
    )
    plt.barh(
        combined_data["Public IP"],
        -combined_data["Unique APIs Targeted"],
        color="orange",
        label="Unique APIs",
    )  # Αρνητική κατεύθυνση για APIs

    # Ετικέτες
    plt.xlabel("Count (Positive: Ports, Negative: APIs)")
    plt.ylabel("Public IPs")
    plt.title(f"Bidirectional Bar Chart for Ports vs APIs (Top {top_n})")

    # Αξονική γραμμή στο 0 για διαχωρισμό
    plt.axvline(0, color="black", linewidth=0.8)

    # Θρύλος και πλέγμα
    plt.legend()
    plt.grid(axis="x", alpha=0.6)
    plt.show()

    return combined_data


def visualize_api_ip_port(df, top_n=5):
    """
    Δημιουργεί θέαση για κάθε API με:
    - Πλήθος μοναδικών IPs (Unique IP Count)
    - Πλήθος διαφορετικών Ports (Unique Ports Count)
    χρησιμοποιώντας bidirectional bar chart.
    """
    # Υπολογισμός Unique IPs και Unique Ports για κάθε API
    api_ips = (
        df.groupby("Api")["Public IP"].nunique().reset_index(name="Unique IP Count")
    )
    api_ports = (
        df.groupby("Api")["Port"].nunique().reset_index(name="Unique Port Count")
    )

    # Συνένωση δεδομένων
    combined_data = pd.merge(api_ips, api_ports, on="Api")
    combined_data = combined_data.sort_values(
        by=["Unique IP Count", "Unique Port Count"], ascending=False
    ).head(top_n)

    # Δημιουργούμε το bidirectional bar chart
    plt.figure(figsize=(12, 8))
    plt.barh(
        combined_data["Api"],
        combined_data["Unique IP Count"],
        color="mediumseagreen",
        label="Unique IPs",
    )
    plt.barh(
        combined_data["Api"],
        -combined_data["Unique Port Count"],
        color="coral",
        label="Unique Ports",
    )  # Αρνητικές τιμές για Ports

    # Ρυθμίσεις οπτικοποίησης
    plt.axvline(0, color="black", linewidth=0.8)  # Άξονας για διαχωρισμό
    plt.title(f"Unique IPs vs Unique Ports for APIs (Top {top_n})")
    plt.xlabel("Count (Positive: IPs, Negative: Ports)")
    plt.ylabel("APIs")
    plt.grid(axis="x", alpha=0.6)  # Οριζόντιο πλέγμα
    plt.legend()
    plt.show()

    return combined_data


def visualize_api_ip_port_vertical(df, top_n=5):
    """
    Δημιουργεί bidirectional vertical bar chart για κάθε API:
    - Πλήθος μοναδικών IPs (Positive side)
    - Πλήθος διαφορετικών Ports (Negative side).
    """
    # Υπολογισμός Unique IPs και Unique Ports για κάθε API
    api_ips = (
        df.groupby("Api")["Public IP"].nunique().reset_index(name="Unique IP Count")
    )
    api_ports = (
        df.groupby("Api")["Port"].nunique().reset_index(name="Unique Port Count")
    )

    # Συνένωση δεδομένων
    combined_data = pd.merge(api_ips, api_ports, on="Api")
    combined_data = combined_data.sort_values(
        by=["Unique IP Count", "Unique Port Count"], ascending=False
    ).head(top_n)

    # Δημιουργούμε το bidirectional vertical bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(
        combined_data["Api"],
        combined_data["Unique IP Count"],
        color="mediumseagreen",
        label="Unique IPs",
    )
    plt.bar(
        combined_data["Api"],
        -combined_data["Unique Port Count"],
        color="coral",
        label="Unique Ports",
    )  # Αρνητικές τιμές για Ports

    # Ρυθμίσεις οπτικοποίησης
    plt.axhline(0, color="black", linewidth=0.8)  # Οριζόντιος άξονας για διαχωρισμό
    plt.title(f"Unique IPs vs Unique Ports for APIs (Top {top_n})")
    plt.ylabel("Count (Positive: IPs, Negative: Ports)")
    plt.xlabel("APIs")
    plt.grid(axis="y", alpha=0.6)  # Κάθετο πλέγμα
    plt.xticks(rotation=0, ha="right")  # Περιστροφή ετικετών API
    plt.legend()
    plt.show()

    return combined_data


def visualize_api_ip_port_grouped(df, top_n=5):
    """
    Δημιουργεί grouped bar chart για κάθε API με:
    - Πλήθος μοναδικών IPs
    - Πλήθος διαφορετικών Ports.
    """


    # Υπολογισμός Unique IPs και Unique Ports για κάθε API
    api_ips = (
        df.groupby("Api")["Public IP"].nunique().reset_index(name="Unique IP Count")
    )
    api_ports = (
        df.groupby("Api")["Port"].nunique().reset_index(name="Unique Port Count")
    )

    # Συνένωση δεδομένων
    combined_data = pd.merge(api_ips, api_ports, on="Api")
    combined_data = combined_data.sort_values(
        by=["Unique IP Count", "Unique Port Count"], ascending=False
    ).head(top_n)

    # Δημιουργούμε τα δεδομένα για grouped bar chart
    bar_width = 0.35
    indices = np.arange(len(combined_data["Api"]))

    plt.figure(figsize=(12, 7))
    plt.bar(
        indices,
        combined_data["Unique IP Count"],
        bar_width,
        label="Unique IPs",
        color="mediumseagreen",
    )
    plt.bar(
        indices + bar_width,
        combined_data["Unique Port Count"],
        bar_width,
        label="Unique Ports",
        color="coral",
    )

    # Ρυθμίσεις οπτικοποίησης
    plt.title(f"Unique IPs and Ports by API (Top {top_n})")
    plt.xlabel("APIs")
    plt.ylabel("Counts")
    plt.xticks(indices + bar_width / 2, combined_data["Api"], rotation=45, ha="right")
    plt.legend()
    plt.grid(axis="y", alpha=0.6)  # Οριζόντιες γραμμές πλέγματος
    plt.tight_layout()
    plt.show()

    return combined_data


def visualize_api_hackers_ports(df, top_n=5, path_a="./hacker_analysis_donut.png"):
    """
    Visualize Number of Hackers (Unique IP Count) using a Donut Chart.
    The slice with the highest value is highlighted, and percentages are displayed.
    """


    # Color Palette Setup
    color_pallete_a = "#0D1B2A"  # Dark Blue (Main colors for slices)
    highlight_color = "#D7C9AA"  # Light Crème (Highlight color for the highest slice)

    # Compute Number of Hackers (Unique IP Count) for each API
    api_ips = (
        df.groupby("Api")["Public IP"].nunique().reset_index(name="Number of Hackers")
    )
    sorted_data = api_ips.sort_values(by="Number of Hackers", ascending=False).head(
        top_n
    )

    # Data for Chart
    labels = sorted_data["Api"]
    hacker_counts = sorted_data["Number of Hackers"]

    # Determine colors: Highlight the API with the highest count
    colors = [
        highlight_color if count == max(hacker_counts) else color_pallete_a
        for count in hacker_counts
    ]

    # Font setup for annotations
    font = FontProperties(family="Futura", weight="regular", size=10)

    # Figure Setup
    plt.figure(
        figsize=(8, 8), dpi=450, facecolor="#FFFFFF"
    )  # White background for clarity
    with plt.rc_context(
            {"text.color": "#000000"}
    ):  # Ensure text is readable (black color)
        wedges, texts, autotexts = plt.pie(
            hacker_counts,
            labels=labels,
            labeldistance=1.1,  # Distance for labels from the center
            colors=colors,
            autopct="%1.1f%%",  # Format percentage labels
            startangle=140,  # Start at a better angle
            pctdistance=0.85,  # Percentage label positioning for donut
            textprops={"fontproperties": font},
        )

        # Donut Hole (inner white space)
        center_circle = plt.Circle(
            (0, 0), 0.70, fc="#ffffff"
        )  # White fill for the hole
        plt.gca().add_artist(center_circle)

        # Title added for clarity
        plt.title("Number of Hackers per API", fontsize=16, fontproperties=font, pad=20)

        # Save Image
        plt.tight_layout()
        plt.savefig(path_a, transparent=False, dpi=450)
        plt.close()


def visualize_api_hackers_ports_pie(df, path_a, color, top_n=5):
    """
    Visualize Number of Hackers (Unique IP Count) using a Pie Chart.
    Adds a small gap between pies, highlights the slice with the highest value, makes it transparent,
    and includes bigger, bold text for API names and percentages.
    """


    # Color Palette Setup
    color_pallete_a = "#0D1B2A"  # Dark Blue (Main colors for slices)
    highlight_color = "#D7C9AA"  # Light Crème (Highlight color for the highest slice)
    percent_font_color_light = "#D7C9AA"  # Light Crème for non-max percentage labels
    percent_font_color_default = "#000000"  # Default darker font for max percentage label

    # Compute Number of Hackers (Unique IP Count) for each API
    api_ips = (
        df.groupby("Api")["Public IP"].nunique().reset_index(name="Number of Hackers")
    )
    sorted_data = api_ips.sort_values(by="Number of Hackers", ascending=False).head(
        top_n
    )

    # Data for Chart
    labels = sorted_data["Api"]
    hacker_counts = sorted_data["Number of Hackers"]

    # Determine colors: Highlight the API with the highest count

    colors = [
        color if count == max(hacker_counts) else color_pallete_a
        for count in hacker_counts
    ]

    # Set small gap (explode) between slices
    explode = [
        0.1 if count == max(hacker_counts) else 0.01  # Larger gap for the maximum slice
        for count in hacker_counts
    ]

    # Font setup for annotations (bigger and bold)
    font = FontProperties(family="Futura", size=12)  # Font for the API labels
    percentage_font_size = 20  # Larger percentage text
    label_font_size = 25  # Larger API label text
    labels = sorted_data["Api"].replace({
        "Entersoft Business Suite": "EBS",
        "Slack Bolt": "SLACK"
    })

    # Figure Setup with Transparency
    plt.figure(figsize=(8, 8), dpi=450)  # Figure setup without background color

    # Calculate percentages
    percentages = (hacker_counts / np.sum(hacker_counts)) * 100

    # Find the index of the largest slice
    max_index = np.argmax(percentages)

    # Calculate rotation angle for the largest slice to start in the top-right
    offset = sum(percentages[:max_index]) + percentages[max_index] / 2
    startangle = 330 - offset  # Rotating to place it in the top-right

    # Create Pie Chart
    with plt.rc_context({"text.color": "#000000"}):  # Default text color for labels
        wedges, texts, autotexts = plt.pie(
            hacker_counts,
            labels=labels,
            explode=explode,  # Small gaps between slices + exploded max slice
            labeldistance=1.25,  # Distance for labels further away from the center
            colors=colors,
            autopct="%1.1f%%",  # Format percentage labels
            startangle=startangle,  # Start at a better angle
            textprops={
                "fontsize": label_font_size,
                # "fontweight": "bold",
            },  # Larger, bold API labels
        )

        # Configure the percentage text (inside the slices)
        for count, autotext in zip(hacker_counts, autotexts):
            # Larger, bold text for percentage annotation
            autotext.set_fontsize(percentage_font_size)
            # autotext.set_fontweight("bold")
            # Adjust font color
            if (count == max(hacker_counts)) and (color != "#0D1B2A"):
                autotext.set_color(
                    percent_font_color_default
                )  # Default for the max slice
            else:
                autotext.set_color(
                    percent_font_color_light
                )  # Light crème for non-max slices

        # Title with Bigger, Bold Font
        # plt.title(
        #     "Number of Hackers Per API",
        #     fontsize=20,  # Even larger title for prominence
        #     fontweight="bold",
        #     pad=20,
        # )

        # Save Image with Transparent Background
        plt.tight_layout()
        plt.savefig(path_a, transparent=True, dpi=450)  # Transparency added to output
        plt.close()


def visualize_api_hackers_ports_donut(df, path_a, color, top_n=5):
    """
    Visualize Number of Hackers (Unique IP Count) using a Donut Chart.
    Percent values follow the donut's curve with automatically calculated font colors for better visibility.
    """

    # Color Palette Setup
    color_pallete_a = "#0D1B2A"  # Dark Blue (Main color for slices)
    highlight_color = "#D7C9AA"  # Light Crème (Highlight color for the highest slice)


    # Compute Number of Hackers (Unique IP Count) for each API
    api_ips = ( df.groupby("Api")["Public IP"].nunique().reset_index(name="Number of Hackers"))
    sorted_data = api_ips.sort_values(by="Number of Hackers", ascending=False).head(top_n)

    # Data for Chart
    labels = sorted_data["Api"]
    hacker_counts = sorted_data["Number of Hackers"]

    # Determine colors: Highlight the API with the highest count
    colors = [
        color if count == max(hacker_counts) else color_pallete_a
        for count in hacker_counts
    ]

    # Font setup for annotations (bigger and bold)
    percentage_font_size = 18  # Adjusted for better visibility
    label_font_size = 18  # Label size adjusted for better alignment
    labels = sorted_data["Api"].replace(
        {"Entersoft Business Suite": "EBS", "Slack Bolt": "SLACK"}
    )

    # Figure Setup with Transparency
    plt.figure(figsize=(8, 8), dpi=450)  # Higher resolution

    # Calculate percentages
    percentages = (hacker_counts / np.sum(hacker_counts)) * 100

    # Find the index of the largest slice
    max_index = np.argmax(percentages)

    # Calculate rotation angle for the largest slice to start in the top-right
    offset = sum(percentages[:max_index]) + percentages[max_index] / 2
    startangle = 330 - offset  # Rotating to place it in the top-right
    
    # Create the donut chart with autopct to display percentages
    wedges, texts, autotexts = plt.pie(
        hacker_counts,
        labels=labels,
        explode=[0.01] * len(hacker_counts),  # Small gaps
        colors=colors,
        startangle=startangle,  # Start from top-center
        autopct="%1.1f%%",  # Automatically calculate and display percentages
        textprops={"fontsize": percentage_font_size},  # Font size for labels and percentages
        pctdistance=0.8,  # Adjust percentage text position closer to the center

    )
    # Configure the percentage text (inside the slices)
    for count, autotext in zip(hacker_counts, autotexts):
        # Larger, bold text for percentage annotation
        autotext.set_fontsize(percentage_font_size)
        # autotext.set_fontweight("bold")
        # Adjust font color
        if (count == max(hacker_counts)) and (color != "#0D1B2A"):
            autotext.set_color(color_pallete_a)  # Default for the max slice
        else:
            autotext.set_color(
                highlight_color
            )  # Light crème for non-max slices

    # Add a colored circle at the center to create a donut effect
    center_circle = plt.Circle((0, 0), 0.60, fc="#415a77")  # Custom color
    plt.gca().add_artist(center_circle)

    # Save Image
    plt.tight_layout()
    plt.savefig(path_a, transparent=True, dpi=450)  # Save as high-quality image
    plt.close()


def sankey_graph(i, df, path_a):
    colors = ["#0D1B2A", "#0D1B2A", "#778DA9", "#D7C9AA"]
    text_colors = [None, "#D7C9AA", "#0D1B2A", "#0D1B2A"]
    df["Api"] = df["Api"].replace(
        {"Entersoft Business Suite": "EBS", "Slack Bolt": "SLACK"}
    )

    # Ομαδοποίηση δεδομένων: Υπολογίζουμε το πλήθος επιθέσεων ανά Api και Port
    grouped_data = df.groupby(["Api", "Port"]).size().reset_index(name="Attacks")
    highlight_color = "#D7C9AA"

    # Δημιουργία λιστών Api και Ports (για τη μοναδική τιμή κάθε κόμβου)
    apis = grouped_data["Api"].unique().tolist()
    ports = (
        grouped_data["Port"].astype(str).unique().tolist()
    )  # Κάνουμε τις τιμές string

    # Δημιουργία λιστών για source-target-value
    sources = (
        grouped_data["Api"].apply(lambda x: apis.index(x)).tolist()
    )  # Index των Apis
    targets = (
        grouped_data["Port"]
        .astype(str)
        .apply(lambda x: len(apis) + ports.index(x))
        .tolist()
    )  # Κάνουμε string πριν το .apply
    values = grouped_data["Attacks"].tolist()  # Αριθμός επιθέσεων

    # Δημιουργία Sankey Diagram
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color=colors[0], width=0.5),
                    label=apis + ports,
                    # Προσδιορισμός χρωμάτων για κάθε κόμβο
                    color=colors[0],

                ),

                link=dict(
                    source=sources,  # Πηγές (θέσεις των Apis)
                    target=targets,  # Προορισμοί (θέσεις των Ports)
                    value=values,  # Τιμές, δηλαδή αριθμός επιθέσεων
                    color=colors[i],
                ),
            )
        ]
    )

    fig.update_layout(
        width=400,  # Προσαρμοσμένο πλάτος
        height=600,  # Προσαρμοσμένο ύψος
        paper_bgcolor="rgba(0,0,0,0)",  # Διαφάνεια φόντου
    )

    # Αποθήκευση ως εικόνα
    fig.write_image(path_a, scale=6)  # Αποθηκεύει το γράφημα στη θέση του script



