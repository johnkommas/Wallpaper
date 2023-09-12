#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import calendar
import os
import shutil
from Files import plot
from PIL import Image, ImageFont, ImageDraw
from dateutil.relativedelta import relativedelta
from datetime import datetime
from Private import stores_sensitive_info as ssi
import pandas as pd


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_rows", None)


def offline(emoji, path, offline_path):
    delete_all_files_inside_folder(offline_path)
    file = f"{emoji}/red.png"
    dir_list = os.listdir(path)
    for dfile in dir_list:
        my_image = Image.open(f"{path}/{dfile}")
        overlay = Image.open(file)
        width, height = overlay.size
        overlay = overlay.resize((width // 4, height // 4))
        my_image.paste(overlay, (550, 160), mask=overlay)
        # image_editable = ImageDraw.Draw(my_image)
        my_image.save(f"{offline_path}/{dfile}")
    delete_all_files_inside_folder(path)
    for dfile in os.listdir(offline_path):
        shutil.copy2(f"{offline_path}/{dfile}", f"{path}/{dfile}")
    delete_all_files_inside_folder(offline_path)


def run(df, file_in, specific_date, path, path_2, sales, timed, plot_df, flag, online_order,
        product_info, status_users_elounda,
        # status_users_lato,
        # customers, customers_month
        ):
    today = specific_date
    data = list(df.TurnOver.values)
    df_years = list(df.YEAR.values)

    years = []
    for i in df_years:
        years.append(str(i))

    my_image = Image.open(f"{path}/{file_in}.jpg")
    # title_font_year = ImageFont.truetype("Futura.ttc", 200)
    # numbers_font_year = ImageFont.truetype("Futura.ttc", 150)
    title_font_year = ImageFont.truetype("Avenir Next.ttc", 200)
    number_font_parse = ImageFont.truetype("DIN Condensed Bold.ttf", 250)
    dates_font_parse = ImageFont.truetype("DIN Condensed Bold.ttf", 80)
    store_info = ImageFont.truetype("25191766905.ttf", 120)
    store_info_small = ImageFont.truetype("25191766905.ttf", 100)
    image_editable = ImageDraw.Draw(my_image)

    # ΠΡΟΣΘΕΤΩ ΤΙΣ ΗΜΕΡΕΣ ΓΙΑ ΚΑΘΕ ΧΡΟΝΟ
    dates_for_every_year = get_date_for_every_year(specific_date)
    # grey = (44, 40, 41)
    white = (255, 255, 255)
    # blue = (26, 55, 110)
    # red = (238, 0, 0)
    pink = (255, 134, 179)
    # green = (68, 255, 115)
    orange = '#F25E49'

    # WRITING STORE INFO
    image_editable.text((520, 150), f"        ELOUNDA MARKET", white, font=store_info)
    image_editable.text((4000, 150), f"REFRESHING DATA EVERY MINUTE :  {timed}", white, font=store_info)
    image_editable.text((10000, 150), f"TODAY SALES:  {int(sales)}€", white, font=store_info)

    # WRITING CUSTOMERS DATA
    # x = 5812
    # for year in range(datetime.now().year - 5, datetime.now().year + 1):
    #     y_year = 490
    #     image_editable.text((x, y_year), str(year), white, font=store_info)
    #     x += 550
    #
    # x = 5812
    # for i, year in enumerate(customers.YEAR):
    #     # y_year = 490
    #     y = 640
    #     y_percent = 790
    #     color = pink if customers.COUNT.iloc[i] == customers.COUNT.min() else customers.COLOR.iloc[i]
    #     # image_editable.text((x, y_year), str(year), color, font=store_info)
    #     image_editable.text((x, y), str(customers.COUNT.iloc[i]), color, font=store_info)
    #     if customers.COUNT.iloc[i] != customers.COUNT.max():
    #         image_editable.text((x, y_percent), f'({(round(100 * customers.COUNT.iloc[i]/customers.COUNT.max())) - 100}%)', color, font=store_info_small)
    #     x += 550
    #
    # x = 5812
    # for i, year in enumerate(customers_month.YEAR):
    #     y = 1090
    #     y_percent = 1230
    #     color = (
    #         pink
    #         if customers_month.COUNT.iloc[i] == customers_month.COUNT.min()
    #         else customers_month.COLOR.iloc[i]
    #     )
    #     image_editable.text((x, y), str(customers_month.COUNT.iloc[i]), color, font=store_info)
    #     if customers_month.COUNT.iloc[i] != customers_month.COUNT.max():
    #         image_editable.text(
    #             (x, y_percent),
    #             f"({(round(100 * customers_month.COUNT.iloc[i]/customers_month.COUNT.max())) - 100}%)",
    #             color,
    #             font=store_info_small,
    #         )
    #     x += 550
    # END OF WRITING CUSTOMERS DATA

    # WRITING YEARS
    x = 500
    check_year = today.year - 11
    for i, year in enumerate(years):
        image_editable.text((x + 400, 900), dates_for_every_year[i], white, font=dates_font_parse)
        if year != str(check_year):
            image_editable.text((x, 400), str(check_year), (255, 255, 255), font=title_font_year)
            x += 660
            data.insert(i, 0)
        image_editable.text((x, 400), year, (255, 255, 255), font=title_font_year)
        x += 660
        check_year += 1

    # WRITING REVENUE VALUES
    x = [0, 310, 260, 215, 170, 120, 75]
    for i in range(len(data)):
        year = str(int(data[i]))
        if int(year) >= int(data[-1]):
            image_editable.text((x[len(year)] + 400, 700), year, white, font=number_font_parse)
        else:
            image_editable.text((x[len(year)] + 400, 700), year, orange, font=number_font_parse)

        x = [y + 660 for y in x]

    pda_data_list = [
        {"pda_data": "ΑΓΟΡΕΣ", "x": 500, "y": 6300, "text_prefix": "Agores"},
        {"pda_data": "ΕΠΙΣΤΡΟΦΕΣ", "x": 2500, "y": 6300, "text_prefix": "Epistrofes"},
        {"pda_data": "ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ", "x": 4600, "y": 6300, "text_prefix": "Endodiakinisi"},
        {"pda_data": "ΠΑΡΑΓΓΕΛΙΕΣ", "x": 6600, "y": 6300, "text_prefix": "Paraggelia"},
        {"pda_data": "ΡΑΦΙ ΤΙΜΕΣ", "x": 9000, "y": 6300, "text_prefix": "Times Rafi"},
    ]
    
    for data in pda_data_list:
        a, b = get_pda_data(online_order, data["pda_data"])
        image_editable.text(
            (data["x"], data["y"]),
            f"{data['text_prefix']}:  ({a} Docs) - ({b} Lines)",
            (255, 255, 255),
            font=store_info,
        )

    # WRITE PRODUCT INFO
    product_info_texts = [
        {'info_key': 'price_change', 'y': 400, 'text_prefix': 'Price Changes'},
        {'info_key': 'new_product', 'y': 550, 'text_prefix': 'New Products'},
        {'info_key': 'special_price', 'y': 850, 'text_prefix': 'Special Offers'}
    ]

    for info_text in product_info_texts:
        text = f"{info_text['text_prefix']}: {product_info.get(info_text['info_key'])}"
        image_editable.text((10000, info_text['y']), text, (255, 255, 255), font=store_info)

    if flag == 'a00':
        swift = 1650
        # WRITING PDA DATA
        a, b = get_pda_data(online_order, 'ΑΓΟΡΕΣ')
        image_editable.text((3400, 2000 + swift), f"{a}", (255, 255, 255), font=store_info)
        image_editable.text((2950, 1500 + swift), f"{b}", orange, font=store_info)

        a, b = get_pda_data(online_order, 'ΕΠΙΣΤΡΟΦΕΣ')
        if len(str(a)) == 1:
            image_editable.text((2200, 1200 + swift), f"{a}", (255, 255, 255), font=store_info)
        if len(str(b)) == 1:
            image_editable.text((1500, 1500 + swift), f"{b}", orange, font=store_info)
        elif len(str(b)) == 2:
            image_editable.text((1500, 1500 + swift), f"{b}", orange, font=store_info)

        a, b = get_pda_data(online_order, 'ΕΝΔΟΔΙΑΚΙΝΗΣΕΙΣ')
        if len(str(a)) == 1:
            image_editable.text((1550, 3450 + swift), f"{a}", (255, 255, 255), font=store_info)
        if len(str(b)) == 1:
            image_editable.text((2250, 3550 + swift), f"{b}", orange, font=store_info)
        elif len(str(b)) == 2:
            image_editable.text((2250, 3550 + swift), f"{b}", orange, font=store_info)
        elif len(str(b)) == 3:
            image_editable.text((2250, 3550 + swift), f"{b}", orange, font=store_info)

        a, b = get_pda_data(online_order, 'ΠΑΡΑΓΓΕΛΙΕΣ')
        if len(str(a)) == 1:
            image_editable.text((1050, 2100 + swift), f"{a}", (255, 255, 255), font=store_info)
        if len(str(b)) == 1:
            image_editable.text((1150, 2800 + swift), f"{b}", orange, font=store_info)
        elif len(str(b)) == 2:
            image_editable.text((1050, 2800 + swift), f"{b}", orange, font=store_info)

        a, b = get_pda_data(online_order, 'ΡΑΦΙ ΤΙΜΕΣ')
        image_editable.text((3000, 3350 + swift), f"{a}", (255, 255, 255), font=store_info)
        image_editable.text((3350, 2700 + swift), f"{b}", orange, font=store_info)

        # WRITE PRODUCT INFO
        image_editable.text((7800, 3300), f"{product_info.get('price_change')}", (255, 255, 255), font=store_info)
        image_editable.text((9350, 3300), f"{product_info.get('new_product')}", (255, 255, 255), font=store_info)
        image_editable.text((7650, 4700), f"{product_info.get('special_price')}", (255, 255, 255), font=store_info)
        image_editable.text((9400, 4700), f"{product_info.get('customer_prefer')}", (255, 255, 255),
                            font=store_info)
    elif flag == 'a01':
        calibrate_y = 700
        calibrate_x = 300
        potitions = [(9204 + 150 - calibrate_x, 5142 + calibrate_y),
                     (8469 - calibrate_x, 5322 - 20 - calibrate_y),
                     (4378 + 100 - calibrate_x, 5142 + calibrate_y),
                     (5816 - calibrate_x, 5142 + calibrate_y),
                     (5071 + 50 - calibrate_x, 5322 - 20 - calibrate_y),
                     (1908 + 120 - calibrate_x, 5322 - 20 - calibrate_y),
                     (7768 + 100 - calibrate_x, 5142 + calibrate_y)]

        lato_potitions = [(4410 - 250, 3080 + calibrate_y),
                          (5100 - 200, 3250 - 20 - calibrate_y),
                          (5840 - 200, 3080 + calibrate_y),
                          (7768 - 200, 3080 + calibrate_y),
                          (8469 - 250, 3250 - 20 - calibrate_y),
                          (9160 - 200, 3080 + calibrate_y)]

        # print()
        # print(status_users_elounda.UserID)
        for pot, user in zip(potitions, ssi.EM_users):
            data = status_users_elounda['elapsed_time'][status_users_elounda.UserID.str.startswith(user)].iloc[0]
            image_editable.text(pot, data, (255, 255, 255), font=store_info)

        # for pot, user in zip(lato_potitions, ssi.LATO_users):
        #     data = status_users_lato["elapsed_time"][status_users_lato.UserID.str.startswith(user)].iloc[0]
        #     image_editable.text(pot, data, (255, 255, 255), font=store_info)

    time = datetime.now().strftime("%d%m%Y%H%M%S")
    my_image.save(f"{path}/TEMP/{file_in}_{time}.jpg")
    glue_images(f"{path}/green.png", f"{path}/TEMP/{file_in}_{time}.jpg", xy=(550, 160), resize=4)

    #WRITE CALENDAR
    cwd = os.path.dirname(os.path.abspath(__file__))
    img_file = f"{cwd}/calendar.png"
    glue_images(img_file, f"{path}/TEMP/{file_in}_{time}.jpg", xy=(1200, 1150), resize=1)

    if flag in ('a0', 'a0_sierra', 'a01'):
        plot.run_daily(plot_df, specific_day=today, path_a=f"{path}/graph.png",
                       path_b=f"{path}/TEMP/{file_in}_{time}.jpg")
        potitions = [(9204, 5142), (8469, 5322), (4378, 5142), (5816, 5142), (5071, 5322), (1908, 5322), (7768, 5142)]
        # lato_potitions = [(4410, 3080), (5100, 3250), (5840, 3080), (7768, 3080), (8469, 3250), (9160, 3080)]
        my_image = Image.open(f"{path}/TEMP/{file_in}_{time}.jpg")
        for user, pots in zip(ssi.EM_users, potitions):
            color = status_users_elounda['COLOR'][status_users_elounda.UserID.str.startswith(user)].iloc[0]
            my_image = paste_image(my_image, f"{path}/{color}.png", xy=pots, resize=4)
        # for user, pots in zip(ssi.LATO_users, lato_potitions):
        #     color = status_users_lato["COLOR"][status_users_lato.UserID.str.startswith(user)].iloc[0]
        #     my_image = paste_image(my_image, f"{path}/{color}.png", xy=pots, resize=4)
        my_image.save(f"{path}/TEMP/{file_in}_{time}.jpg")
    elif flag == 'a00':
        glue_images(f"{path}/pda.png", f"{path}/TEMP/{file_in}_{time}.jpg", xy=(1200, 3000), resize=1)
        glue_images(f"{path}/product.png", f"{path}/TEMP/{file_in}_{time}.jpg", xy=(7500, 3000), resize=1)

    elif flag == 'a000':
        glue_images(f"{path}/words.png", f"{path}/TEMP/{file_in}_{time}.jpg", xy=(30, 1800), resize=1)
        glue_images(f"{path}/tree_map.png", f"{path}/TEMP/{file_in}_{time}.jpg", xy=(4500, 400), resize=3)

    delete_all_files_inside_folder(f"{path_2}/")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}.jpg", f"{path_2}/{file_in}_{time}.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}.jpg", f"{path_2}/{file_in}_{time}_2.jpg")


def get_pda_data(df, str_a):
    a = 0
    b = 0
    try:
        a = df[df.TYPE == str_a].DOCS.iloc[0]
        b = df[df.TYPE == str_a].LINES.iloc[0]
    except IndexError as e:
        pass
    finally:
        return a, b


def get_date_for_every_year(specific_date):
    english = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    greek = ["(ΔΕ)", "(ΤΡ)", "(ΤΕ)", "(ΠΕ)", "(ΠΑ)", "(ΣΑ)", "(ΚΥ)"]
    today = specific_date
    x = []
    for i in range(0, 12):
        a = today - relativedelta(years=i)
        eng = a.strftime("%a")
        x.append(greek[english.index(eng)])
    x.reverse()
    return x


def glue_images(pda_image, path, xy, resize):
    my_image = Image.open(path)
    overlay = Image.open(pda_image)
    width, height = overlay.size
    overlay = overlay.resize((width // resize, height // resize))
    my_image.paste(overlay, xy, mask=overlay)
    # image_editable = ImageDraw.Draw(my_image)
    my_image.save(path)


def paste_image(my_image, overlay_image, xy, resize):
    overlay = Image.open(overlay_image)
    width, height = overlay.size
    overlay = overlay.resize((width // resize, height // resize))
    my_image.paste(overlay, xy, mask=overlay)
    # image_editable = ImageDraw.Draw(my_image)
    return my_image


def delete_all_files_inside_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def create_calendar():

    # Define the current month
    today = datetime.now()
    next_month = today.month + 1 if today.month != 12 else 1
    next_year = today.year if today.month != 12 else today.year + 1

    # The colors for various elements
    color_month_and_day = "#F25E49"
    color_week_days = "grey"
    color_weekends = "grey"
    color_days = "white"

    # Define a new image with reduced width to make room for smaller gaps
    img = Image.new("RGBA", (10000, 2400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for month_diff in range(4):  # Update range from 2 to 4
        month = (today.month + month_diff - 1) % 12 + 1
        year = today.year + ((today.month + month_diff - 1) // 12)

        cal_month = calendar.monthcalendar(year, month)

        # Month title
        month_name = calendar.month_name[month]
        text_font = ImageFont.truetype("Arial.ttf", 120)

        # Decreased the multiplication factor to bring months closer
        x_start = 2500 * month_diff
        draw.text((x_start, 0), month_name, fill=color_month_and_day, font=text_font)

        # Weekday titles
        weekdays = list(calendar.day_abbr)
        for day_no, weekday in enumerate(weekdays):
            weekday_font = ImageFont.truetype("Arial.ttf", 80)
            draw.text((x_start + day_no * 280, 160), weekday, fill=color_week_days, font=weekday_font)

        # Days
        day_font = ImageFont.truetype("Arial.ttf", 80)
        for week_no, week in enumerate(cal_month):
            for day_no, day in enumerate(week):
                if day != 0:
                    fill_color = color_weekends if day_no >= 5 else color_days
                    if datetime(year, month, day).date() == today.date():
                        fill_color = color_month_and_day

                    text_width = draw.textlength(str(day), font=day_font)
                    centered_x = x_start + day_no * 280 + 40 - text_width // 2
                    draw.text((centered_x, week_no * 120 + 440), str(day), fill=fill_color, font=day_font)

    cwd = os.path.dirname(os.path.abspath(__file__))
    img_file = f"{cwd}/calendar.png"
    img.save(img_file)

