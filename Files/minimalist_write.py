#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import calendar
import os
import shutil
from Files import plot, schedule_my_calendar
from PIL import Image, ImageFont, ImageDraw
from dateutil.relativedelta import relativedelta
from datetime import datetime
from Private import stores_sensitive_info as ssi
import pandas as pd


def get_date_for_every_year(today):
    english = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    greek = ["(ΔΕ)", "(ΤΡ)", "(ΤΕ)", "(ΠΕ)", "(ΠΑ)", "(ΣΑ)", "(ΚΥ)"]
    x = []
    y = []
    for i in range(0, 6):
        a = today - relativedelta(years=i)
        eng = a.strftime("%a")
        x.append(greek[english.index(eng)])
        y.append(a.year)
    x.reverse()
    # y.reverse()
    # print(*zip(x, y))
    return x


def delete_all_files_inside_folder(folder, exception_file=None):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if filename == exception_file:
                continue
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def write_revenue_values(image_editable, data, color_pallete_a, color_pallete_c, number_font_parse, counter):
    x_offsets = [0, 310, 260, 215, 170, 120, 75]
    for i in data:
        revenue = str(int(i))
        if i == max(data) and counter == 2:
            image_editable.text(
                (x_offsets[len(revenue)] + 400, 700),
                revenue,
                color_pallete_c,
                font=number_font_parse,
            )
        else:
            image_editable.text(
                (x_offsets[len(revenue)] + 400, 700),
                revenue,
                color_pallete_a,
                font=number_font_parse,
            )
        x_offsets = [y + 660 for y in x_offsets]


def write_years_and_days(image_editable, df_years, specific_date, dates_for_every_year, title_font_year,
                         dates_font_parse, color_pallete_a, color_pallete_b, timestamp_font_parse, time, counter):
    years = [str(i) for i in df_years]
    x = 500
    check_year = specific_date.year - 5
    if counter == 0:
        custom_color = color_pallete_a
    else:
        custom_color = color_pallete_b

    for i, year in enumerate(years):
        # Ελέγχει αν το year ταιριάζει με το check_year
        text_to_draw = (dates_for_every_year[i] if year == str(check_year) else dates_for_every_year[i])
        image_editable.text(
            (x, 900),
            text_to_draw,
            custom_color,
            font=dates_font_parse,
        )
        # Ενημερώνει το check_year αν χρειάζεται
        if year == str(check_year):
            check_year = int(year)
        image_editable.text((x, 400), year, custom_color, font=title_font_year)
        x += 660
        check_year += 1
    image_editable.text(
        (10100, 6300),
        time,
        custom_color,
        font=timestamp_font_parse,
    )


def run(df, path, path_2, file_in, specific_date, plot_df):
    # SETUP FONTS
    title_font_year = ImageFont.truetype("Avenir Next.ttc", 200)
    number_font_parse = ImageFont.truetype("DIN Condensed Bold.ttf", 250)
    dates_font_parse = ImageFont.truetype("DIN Condensed Bold.ttf", 80)
    timestamp_font_parse = ImageFont.truetype("Futura.ttc", 80)

    # SETUP COLORS
    color_pallete_a = "#0D1B2A"
    color_pallete_b = "#778DA9"
    color_pallete_c = "#D7C9AA"

    # INITIALIZE IMAGE
    my_image_1 = Image.open(f"{path}/{file_in}_1.jpg")
    my_image_2 = Image.open(f"{path}/{file_in}_2.jpg")
    my_image_3 = Image.open(f"{path}/{file_in}_3.jpg")
    image_editable_1 = ImageDraw.Draw(my_image_1)
    image_editable_2 = ImageDraw.Draw(my_image_2)
    image_editable_3 = ImageDraw.Draw(my_image_3)

    images = [my_image_1, my_image_2, my_image_3]
    editables = [image_editable_1, image_editable_2, image_editable_3]

    # ΠΡΟΣΘΕΤΩ ΤΙΣ ΗΜΕΡΕΣ ΓΙΑ ΚΑΘΕ ΧΡΟΝΟ
    dates_for_every_year = get_date_for_every_year(specific_date)

    # LIST DATA
    data = list(df.TurnOver.values)
    df_years = list(df.YEAR.values)

    # add timestamp
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    # WRITING YEARS
    counter = 0
    for image, editable in zip(images, editables):
        write_years_and_days(
            image_editable=editable,
            df_years=df_years,
            specific_date=specific_date,
            dates_for_every_year=dates_for_every_year,
            title_font_year=title_font_year,
            dates_font_parse=dates_font_parse,
            color_pallete_a=color_pallete_a,
            color_pallete_b=color_pallete_b,
            timestamp_font_parse=timestamp_font_parse,
            time=time,
            counter=counter
        )

        # WRITING REVENUE VALUES
        write_revenue_values(editable, data, color_pallete_a, color_pallete_c, number_font_parse, counter)
        counter += 1

    time = datetime.now().strftime("%d%m%Y%H%M%S")
    my_image_1.save(f"{path}/TEMP/{file_in}_{time}_1.jpg")
    my_image_2.save(f"{path}/TEMP/{file_in}_{time}_2.jpg")
    my_image_3.save(f"{path}/TEMP/{file_in}_{time}_3.jpg")

    for i in range(1, 4):
        plot.run_daily_smooth(
            plot_df,
            specific_day=specific_date,
            path_a=f"{path}/graph.png",
            path_b=f"{path}/TEMP/{file_in}_{time}_{i}.jpg",
            color_a= color_pallete_a,
            color_b = color_pallete_b,
            color_c = color_pallete_c,
            loop_counter = i
        )

    delete_all_files_inside_folder(f"{path_2}/", "kommas.png")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_1.jpg", f"{path_2}/{file_in}_1.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_2.jpg", f"{path_2}/{file_in}_2.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_3.jpg", f"{path_2}/{file_in}_3.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_2.jpg", f"{path_2}/{file_in}_4.jpg")
