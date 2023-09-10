#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import numpy as np
import pandas as pd
import squarify
from matplotlib import pyplot as plt
from PIL import Image
from datetime import timedelta, datetime
from wordcloud import WordCloud, ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude


def run_daily(all_years, specific_day, path_a, path_b):
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

    with plt.rc_context(
        {"axes.edgecolor": "white", "xtick.color": "white", "ytick.color": "white"}
    ):
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["FreeMono"]
        plt.figure(figsize=(22, 5), dpi=450, facecolor="#1a376e")
        plt.subplot()
    colors = "#FF5732"
    plt.bar(X, Y, alpha=0.9, color=colors)
    plt.plot(X, Y_all, alpha=0.9, color="red")
    plt.fill_between(X, Y_all, alpha=0.1, color="white")
    for (
        a,
        b,
    ) in zip(X, Y):
        label = f"{b}\nEUR"
        # this method is called for each point
        plt.annotate(
            label,  # this is the text
            (a, b),  # this is the point to label
            textcoords="offset points",  # how to position the text
            xytext=(0, 10),  # distance from text to points (x,y)
            ha="center",
            color="white",
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
    glue_images_2(path_a, path_b)


def glue_images_2(path_a, path_b):
    img_file = f"{path_a}"
    my_image = Image.open(f"{path_b}")
    overlay = Image.open(img_file)
    width, height = overlay.size
    overlay = overlay.resize((width * 1, height * 1))
    my_image.paste(overlay, (343, 4000), mask=overlay)
    # image_editable = ImageDraw.Draw(my_image)
    my_image.save(f"{path_b}")


def randar_chart(categories, sales, path):
    with plt.rc_context(
        {"axes.edgecolor": "white", "xtick.color": "white", "ytick.color": "white"}
    ):
        plt.figure(figsize=(7, 7), dpi=120)
        plt.subplot()
    plt.barh(categories, sales, alpha=0.9, color="white")
    for (
        a,
        b,
    ) in zip(sales, categories):
        label = f"{a}\nEUR"
        # this method is called for each point
        plt.annotate(
            label,  # this is the text
            (a, b),  # this is the point to label
            textcoords="offset points",  # how to position the text
            xytext=(50, 0),  # distance from text to points (x,y)
            ha="center",
            color="white",
        )  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.1)
    plt.box(False)
    plt.tight_layout()
    img_file = f"{path}/sales_bar.png"
    plt.savefig(img_file, transparent=True)
    plt.close()
    glue_images_3(path)


def glue_images_3(path):
    img_file = f"{path}/tree_map.png"
    my_image = Image.open(f"{path}/semi_final.jpg")
    overlay = Image.open(img_file)
    width, height = overlay.size
    overlay = overlay.resize((width * 3, height * 3))
    my_image.paste(overlay, (5000, 50), mask=overlay)
    # image_editable = ImageDraw.Draw(my_image)
    my_image.save(f"{path}/roll/finale.jpg")

    my_image.save(f"{path}/roll/finale.jpg")
    my_image.save(f"{path}/roll/finale_a.jpg")
    my_image.save(f"{path}/roll/finale_b.jpg")
    my_image.save(f"{path}/roll/finale_c.jpg")
    my_image.save(f"{path}/roll/finale_d.jpg")
    my_image.save(f"{path}/roll/finale_e.jpg")


def tree_map(df, path):
    # Prepare Data
    all_ = df
    df = df.head(10)
    try:
        labels = df.apply(
            lambda x: f'{x[0]} ({round(int(x[2]) * 100 / all_["SALES"].sum())}%)\n{int(x[1])}{"T" if x[1] - int(x[1]) == 0 else "Κ"}/{int(x[2])}€',
            axis=1,
        )

        sizes = df["SALES"].values.tolist()
        colors = [plt.cm.viridis(i / float(len(labels))) for i in range(len(labels))]

        # Draw Plot
        plt.figure(figsize=(50, 10), dpi=340)
        squarify.plot(
            sizes=sizes,
            label=labels,
            color=colors,
            alpha=1,
            text_kwargs={"color": "#FFFFFF", "size": 60},
            pad=True,
        )
        plt.axis("off")
        plt.tight_layout()
        img_file = f"{path}/tree_map.png"
        plt.savefig(img_file, transparent=True)
    except ZeroDivisionError:
        print("ΣΦΑΛΜΑ ZeroDivisionError ΣΤΟ TREE MAP")
    except Exception:
        print("ΑΛΛΟ ΣΦΑΛΜΑ ΣΤΟ TREE MAP")
    finally:
        plt.close()


def make_wordcloud(df, path):
    # load wikipedia text on rainbow
    # text = open(os.path.join(d, 'wiki_rainbow.txt'), encoding="utf-8").read()
    df.dropna(inplace=True)
    df.category = df.category.replace(" ", "-", regex=True)
    # text = " ".join(df.category)
    # load image. This has been modified in gimp to be brighter and have more saturation.
    parrot_color = np.array(Image.open(f"{path}/basket_2.png"))
    # subsample by factor of 3. Very lossy but for a wordcloud we don't really care.
    parrot_color = parrot_color[::3, ::3]

    # create mask  white is "masked out"
    parrot_mask = parrot_color.copy()
    parrot_mask[parrot_mask.sum(axis=2) == 0] = 255

    # some finesse: we enforce boundaries between colors, so they get less washed out.
    # For that we do some edge detection in the image
    edges = np.mean(
        [
            gaussian_gradient_magnitude(parrot_color[:, :, i] / 255.0, 2)
            for i in range(3)
        ],
        axis=0,
    )
    parrot_mask[edges > 0.08] = 255

    # create wordcloud. A bit sluggish, you can subsample more strongly for quicker rendering
    # relative_scaling=0 means the frequencies in the data are reflected less
    # accurately, but it makes a better picture
    wc = WordCloud(
        mode="RGBA",
        background_color=None,
        font_path="Avenir Next.ttc",
        scale=7,
        width="1920",
        height="1080",
        max_words=2000,
        mask=parrot_mask,
        max_font_size=180,
        random_state=42,
        relative_scaling=0.5,
    )

    # generate word cloud
    d = {}
    for a, b in zip(df.category, df.SALES):
        d[a] = int(b)
    wc.generate_from_frequencies(d)
    # wc.generate(text)
    # plt.imshow(wc)

    # create coloring from image
    image_colors = ImageColorGenerator(parrot_color)
    wc.recolor(color_func=image_colors)
    plt.figure(figsize=(10, 10), dpi=320)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    wc.to_file(f"{path}/words.png")
    plt.close()
    #
    # plt.figure(figsize=(10, 10))
    # plt.title("Original Image")
    # plt.imshow(parrot_color)
    #
    # plt.figure(figsize=(10, 10))
    # plt.title("Edge map")
    # plt.imshow(edges)
    # plt.show()
    # return d


def pda():
    """
    https://www.freeject.net/2019/12/color-palette-png-6-color-combinations.html?m=1

    :return:
    """
    data = [1, 1, 1, 1]
    # labels = ["ΑΓΟΡΕΣ", "ΕΠΙΣΤΡΟΦΕΣ", "ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ", "ΠΑΡΑΓΓΕΛΙΕΣ", "ΡΑΦΙ_ΤΙΜΕΣ"]
    fig, ax = plt.subplots(figsize=(6, 6), dpi=160)
    color_4 = ["#EB4A04", "#FE8E36", "#265158", "#63A99E", "#9FDDD2", "#CC222B"]
    plt.pie(
        data,
        # pctdistance=0.85,
        # labels=mylabels,
        colors=color_4,
        # labeldistance=-1.2,
        # textprops={'color': "white"},
        # labels=labels
    )
    # plt.title(f'{title}', color='white')
    centre_circle = plt.Circle((0, 0), 0.65, fc="#27282C")
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # plt.text(0, 0, f'{percent}%', ha='center', va='center', fontsize=82, color='white')
    ax.axis("equal")
    plt.tight_layout()
    plt.savefig("kommas.png", transparent=True)
    # plt.show()
    plt.close()


# pda()


def customers_graph(df):
    df_live = df[df.YEAR == datetime.now().year]
    df_past = df[df.YEAR == datetime.now().year - 1]

    # def add_numbers(X, Y):
    #     for (
    #         a,
    #         b,
    #     ) in zip(X, Y):
    #         label = f"{b}\nEUR"
    #         # this method is called for each point
    #         plt.annotate(
    #             label,  # this is the text
    #             (a, b),  # this is the point to label
    #             textcoords="offset points",  # how to position the text
    #             xytext=(0, 10),  # distance from text to points (x,y)
    #             ha="center",
    #             color="white",
    #         )  # horizontal alignment can be left, right or center

    with plt.rc_context(
        {"axes.edgecolor": "white", "xtick.color": "white", "ytick.color": "white"}
    ):
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["FreeMono"]
        plt.figure(figsize=(22, 5), dpi=450, facecolor="#1a376e")
        plt.subplot()
    # colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    colors = ["#FF5732", "#00F059"]

    X = df_past["HOUR"].to_list()
    Y = df_past["COUNT"].to_list()
    plt.plot(X, Y, alpha=0.9, color=colors[0])
    # add_numbers(X, Y)

    X = df_live["HOUR"].to_list()
    Y = df_live["COUNT"].to_list()
    plt.plot(X, Y, alpha=0.9, color=colors[1])
    # add_numbers(X, Y)
    plt.box(False)
    plt.tight_layout()
    img_file = f"test.png"
    plt.savefig(img_file, transparent=True)
    plt.close()


