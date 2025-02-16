import os
from datetime import timedelta

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, font_manager
from scipy.ndimage import gaussian_filter1d
from Files import plot
from Files import minimalist_write


def run_daily_smooth(all_years, specific_day, path_a, path, images):
    year = specific_day.year
    # df = all_years[all_years.YEAR == year].sort_values(by='DATE')
    df = all_years[all_years.YEAR == year]
    first_day = specific_day.replace(day=1)
    current_month = specific_day.month
    if current_month == 12:
        last_day = specific_day.replace(day=31)
    else:
        next_month = specific_day.replace(day=1).replace(month=current_month + 1)
        last_day = next_month - timedelta(days=1)

    date_range = pd.date_range(first_day, last_day, freq="D")
    date = [i.strftime("%d/%m/%Y") for i in date_range]
    x = df["DATE"].to_list()
    x_all = list(all_years["DAY"].unique())
    y = df["TurnOver"].to_list()
    y_all = []
    for day in all_years.DAY.unique():
        y_all.append(round(all_years["TurnOver"][all_years.DAY == day].mean(), 2))
    X = date
    Y = []
    Y_all = []
    counter = 0
    counter_all = 0
    for i in date:
        Y_all.append(0)
        if i in x:
            Y.append(int(y[counter]))
            counter += 1
        else:
            Y.append(0)
    for i in x_all:
        try:
            Y_all[i - 1] = y_all[counter_all]
            counter_all += 1
        except Exception:
            pass

    for loop_counter, image in enumerate(images, start=1):
        with plt.rc_context(
                {"axes.edgecolor": os.getenv("COLOR_A"), "xtick.color": os.getenv("COLOR_A"),
                 "ytick.color": os.getenv("COLOR_A")}
        ):
            # plt.rcParams["font.family"] = "Poiret One"
            plt.rcParams["font.family"] = "Futura"
            # DIN Condensed Bold.ttf
            # plt.rcParams["font.monospace"] = ["FreeMono"]
            plt.figure(figsize=(22, 5), dpi=450, facecolor="#1a376e")
            plt.subplot()
        font = font_manager.FontProperties(family="Futura")
        median = np.median(Y_all)
        mean_val = np.mean(Y_all)
        current_max = np.max(Y)
        if loop_counter == 0:
            print(f"🟢MEDIAN = {median}€", end="")
        if loop_counter == 1:
            colors = [os.getenv("COLOR_A") for _ in Y]
        elif loop_counter == 2:
            colors = [os.getenv("COLOR_B") for _ in Y]
        elif loop_counter == 3:
            colors = [os.getenv("COLOR_C") if i >= current_max else os.getenv("COLOR_A") for i in Y]

        plt.bar(X, Y, alpha=0.9, color=colors)
        line_color = [os.getenv("COLOR_B"), os.getenv("COLOR_A"), os.getenv("COLOR_B"), os.getenv("COLOR_C")]
        ysmoothed = gaussian_filter1d(Y_all, sigma=2)
        plt.plot(
            X,
            Y_all,
            # ysmoothed if loop_counter in (1, 3) else Y_all,
            alpha=0.9,
            color=line_color[loop_counter],
        )
        for a, b in zip(X, Y):
            label = f"{b}€" if b > 0 else ""
            # this method is called for each point
            plt.annotate(
                label,  # this is the text
                (a, b),  # this is the point to label
                textcoords="offset points",  # how to position the text
                xytext=(0, 10),  # distance from text to points (x,y)
                ha="center",
                fontproperties=font,
                color=os.getenv("COLOR_A"),
            )  # horizontal alignment can be left, right or center
        plt.xticks(
            ticks=date,
            labels=[f"{i.strftime('%a')}\n{i.strftime('%d/%m')}" for i in date_range],
        )
        plt.box(False)
        plt.tight_layout()
        img_file = f"{path_a}"
        plt.savefig(img_file, transparent=True)
        plt.close()
        image = minimalist_write.paste_image(image, path_a, (100, 4200))
