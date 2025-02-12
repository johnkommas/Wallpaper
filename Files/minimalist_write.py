#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import time as ctime
import os
import shutil
from Files import plot
from PIL import Image, ImageFont, ImageDraw
from dateutil.relativedelta import relativedelta
from datetime import datetime
from mikrotik import app
from Youtrack import youtrack_app


def offline(emoji, path, offline_path, word):
    # Ορισμός χρωμάτων
    color = os.getenv("COLOR_A")
    box = (10000, 500)  # Αρχική θέση για το κείμενο πάνω στην εικόνα
    if word == "VPN OFFLINE":
        box = (10000, 700)
    delete_all_files_inside_folder(offline_path)  # Διαγραφή όλων των αρχείων στον φάκελο offline_path
    dir_list = os.listdir(path)
    for dfile in dir_list:
        my_image = Image.open(f"{path}/{dfile}")
        image_editable = ImageDraw.Draw(my_image)

        # Χρησιμοποιούμε διαφορετικά χρώματα για κάθε γράμμα σύμφωνα με τα palettes
        font = ImageFont.truetype(os.getenv("FONT_POIRET_ONE"), 200)  # Αλλαγή font αν χρειάζεται
        x, y = box  # Ξεκινάμε από την προκαθορισμένη θέση

        # Διαχωρισμός γραμμάτων και χρωμάτων

        image_editable.text((x, y), word, font=font, fill=color)

        # Αποθηκεύουμε την τροποποιημένη εικόνα στο offline_path
        my_image.save(f"{offline_path}/{dfile}")

    # Διαγραφές και αντιγραφές αρχείων
    delete_all_files_inside_folder(path)
    for dfile in os.listdir(offline_path):
        shutil.copy2(f"{offline_path}/{dfile}", f"{path}/{dfile}")
    delete_all_files_inside_folder(offline_path)


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


def write_revenue_values(image_editable, data, number_font_parse, counter):
    x_offsets = [0, 310, 260, 215, 170, 120, 75]
    for i in data:
        revenue = str(int(i))
        if i == max(data) and counter == 2:
            image_editable.text(
                (x_offsets[len(revenue)] + 400, 700),
                revenue,
                os.getenv("COLOR_C"),
                font=number_font_parse,
            )
        else:
            image_editable.text(
                (x_offsets[len(revenue)] + 400, 700),
                revenue,
                os.getenv("COLOR_A"),
                font=number_font_parse,
            )
        x_offsets = [y + 660 for y in x_offsets]


def write_years_and_days(image_editable, df_years, specific_date, dates_for_every_year, title_font_year,
                         dates_font_parse, timestamp_font_parse, time, counter):
    years = [str(i) for i in df_years]
    x = 500
    check_year = specific_date.year - 5
    colors = [os.getenv("COLOR_A"), os.getenv("COLOR_B"), os.getenv("COLOR_C")]
    custom_color = colors[counter]

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

    # write timestamp refreshed data
    image_editable.text((10100, 6300), time, custom_color, font=timestamp_font_parse)


def paste_image(my_image, overlay_image, xy, resize):
    overlay = Image.open(overlay_image)
    width, height = overlay.size
    overlay = overlay.resize((width // resize, height // resize))
    my_image.paste(overlay, xy, mask=overlay)
    # image_editable = ImageDraw.Draw(my_image)
    return my_image


def run(df, path, path_2, file_in, specific_date, plot_df, multiple_data, status_users_elounda, monthly_turnover_df):
    start = ctime.perf_counter()

    # SETUP FONTS
    title_font_year = ImageFont.truetype(os.getenv("FONT_AVENIR_NEXT"), 200)
    number_font_parse = ImageFont.truetype(os.getenv("FONT_DIN_CONDENSED_BOLD"), 250)
    dates_font_parse = ImageFont.truetype(os.getenv("FONT_DIN_CONDENSED_BOLD"), 80)
    timestamp_font_parse = ImageFont.truetype(os.getenv("FONT_FUTURA"), 80)

    # INITIALIZE IMAGE
    my_image_1 = Image.open(f"{path}/{file_in}_1.jpg")
    my_image_2 = Image.open(f"{path}/{file_in}_2.jpg")
    my_image_3 = Image.open(f"{path}/{file_in}_3.jpg")
    image_editable_1 = ImageDraw.Draw(my_image_1)
    image_editable_2 = ImageDraw.Draw(my_image_2)
    image_editable_3 = ImageDraw.Draw(my_image_3)

    images = [my_image_1, my_image_2, my_image_3]
    editables = [image_editable_1, image_editable_2, image_editable_3]



    # add timestamp
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    c1 = ctime.perf_counter()
    print(f"🟢DONE IN: {round(c1 - start)} sec WALLPAPER INITIALIZED || ", end="")

    if multiple_data == 3:
        # ENTERSOFT ONLINE OFFLINE USERS
        calibrate_y = 280
        calibrate_x = 300
        potitions = [
            (8500, 4100 - calibrate_y),  # GIOTA 5Days
            (7500, 3680 - calibrate_y),  # KOUTOULAKI 9h.29m
            (8500, 2250 - calibrate_y),  # KYRIAKOS 4h.1m
            (8500, 1400 - calibrate_y),  # M.KOUTOULAKIS 12h.52m
            (7500, 1800 - calibrate_y),  # M.RAPANAKI 3h.52m
            (7500, 950 - calibrate_y),  # RADMIN 13h.57m
            (8500, 3250 - calibrate_y),  # XNARAKI 3h.58m
        ]

        image_potitions = [
            (8080, 3980 - calibrate_y),  # GIOTA
            (8230, 3550 - calibrate_y),  # KOUTOULAKI
            (8080, 2100 - calibrate_y),  # KYRIAKOS
            (8080, 1250 - calibrate_y),  # M.KOUTOULAKIS
            (8230, 1670 - calibrate_y),  # M.RAPANAKI
            (8230, 830 - calibrate_y),  # RADMIN
            (8080, 3130 - calibrate_y),  # XNARAKI
        ]
        EM_Users = os.getenv("EMUSERS").split(",")
        for image, editable in zip(images, editables):
            for pot, user in zip(potitions, EM_Users):
                filtered_data = status_users_elounda["elapsed_time"][
                    status_users_elounda.UserID.str.startswith(user)
                ]

                if not filtered_data.empty:
                    data = filtered_data.iloc[0]
                    # print(user, data)
                else:
                    data = "ERROR"
                # print(user, data)
                editable.text(pot, data, os.getenv("COLOR_A"), font=timestamp_font_parse)

        for image in images:
            for user, pots in zip(EM_Users, image_potitions):
                filtered_data = status_users_elounda["COLOR"][
                    status_users_elounda.UserID.str.startswith(user)
                ]
                if not filtered_data.empty:
                    color = filtered_data.iloc[0]
                else:
                    color = "red"
                # print(color)

                image = paste_image(image, f"{path}/{color}.png", xy=pots, resize=4)

    if multiple_data in (0, 3):
        # run mikrotik get dataframe
        print("Reading E-mail Mikrotik || ", end='')
        dataframe = app.run()

        for image, editable in zip(images, editables):
            # Υπολογισμός πλάτους και ύψους για το κείμενο και τον αριθμό
            daily_attacks = dataframe.groupby(dataframe["Date"]).size()
            mean_attacks = daily_attacks.mean()
            daily = f"{int(mean_attacks)}-{len(dataframe)}"

            editable.text((5080 + 500, 600), daily, os.getenv("COLOR_A"), font=number_font_parse)
            editable.text((4950 + 500, 800), "Daily vs Total Penetration Attempts", os.getenv("COLOR_A"),
                          font=timestamp_font_parse)  # Σχεδίαση του αριθμού

    c2 = ctime.perf_counter()
    print(f"🟢DONE IN: {round(c2 - c1)} sec Mikrotik - Youtrack || ", end="")

    c1 = ctime.perf_counter()
    # WRITING YEARS
    counter = 0
    if multiple_data in (2, 3):
        # ΠΡΟΣΘΕΤΩ ΤΙΣ ΗΜΕΡΕΣ ΓΙΑ ΚΑΘΕ ΧΡΟΝΟ
        dates_for_every_year = get_date_for_every_year(specific_date)

        # LIST DATA
        data = list(df.TurnOver.values)
        df_years = list(df.YEAR.values)

        for image, editable in zip(images, editables):
            write_years_and_days(
                image_editable=editable,
                df_years=df_years,
                specific_date=specific_date,
                dates_for_every_year=dates_for_every_year,
                title_font_year=title_font_year,
                dates_font_parse=dates_font_parse,
                timestamp_font_parse=timestamp_font_parse,
                time=time,
                counter=counter
            )

            # WRITING REVENUE VALUES
            write_revenue_values(editable, data, number_font_parse, counter)
            counter += 1

    time = datetime.now().strftime("%d%m%Y%H%M%S")
    my_image_1.save(f"{path}/TEMP/{file_in}_{time}_1.jpg")
    my_image_2.save(f"{path}/TEMP/{file_in}_{time}_2.jpg")
    my_image_3.save(f"{path}/TEMP/{file_in}_{time}_3.jpg")

    c2 = ctime.perf_counter()
    print(f"🟢DONE IN: {round(c2 - c1)} sec WRITING YTD || ", end="")

    if multiple_data in (0, 3):
        youtrack_df = youtrack_app.main()
        vpn_status = app.connect_via_ssh()
        youtrack_image = f"{path}/youtrack.png"
        Vpn_Online = f"{path}/Vpn_Online.png"
        Vpn_Offline = f"{path}/Vpn_Offline.png"
        for i in range(1, 4):
            plot.plot_run_mikrotik(i, dataframe,
                                   path_b=f"{path}/TEMP/{file_in}_{time}_{i}.jpg",
                                   path=path)
            plot.plot_run_youtrack(i, path, youtrack_df, youtrack_image,
                                   path_b=f"{path}/TEMP/{file_in}_{time}_{i}.jpg")



            vpn_X = 5600
            step = 200
            vpn_Y = 200
            vpn_users = os.getenv("VPNUSERS").split(",")

            # Βρόχος για κάθε χρήστη
            for index, user in enumerate(vpn_users):
                # Υπολογισμός του box_ δυναμικά
                box = (vpn_X + step * index, vpn_Y)

                # Έλεγχος αν το όνομα υπάρχει και καθορισμός της κατάστασης
                try:
                    vpn_status_result = (Vpn_Online if (vpn_status["name"] == user).any() else Vpn_Offline)
                except KeyError:

                    vpn_status_result = Vpn_Offline

                # Δημιουργία του path και σύνδεση της εικόνας
                plot.glue_image_general(
                    vpn_status_result, path_b=f"{path}/TEMP/{file_in}_{time}_{i}.jpg", box_=box, resize=.5
                )

    if multiple_data == 3:
        for i in range(1, 4):
            # Call PLOT for Donut Monthly TurnOver
            plot.plot_run_monthly_turnover(i,
                                           monthly_turnover_df,
                                           path_b=f"{path}/TEMP/{file_in}_{time}_{i}.jpg",
                                           path=path)
            plot.run_daily_smooth(
                plot_df,
                specific_day=specific_date,
                path_a=f"{path}/graph.png",
                path_b=f"{path}/TEMP/{file_in}_{time}_{i}.jpg",
                loop_counter=i
            )

    delete_all_files_inside_folder(f"{path_2}/", "kommas.png")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_1.jpg", f"{path_2}/{file_in}_1.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_2.jpg", f"{path_2}/{file_in}_2.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_3.jpg", f"{path_2}/{file_in}_3.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_2.jpg", f"{path_2}/{file_in}_4.jpg")
    c3 = ctime.perf_counter()
    print(f" 🟢DONE IN: {round(c3 - c2)} sec PLOTTING GRAPH ", end="")
    ctime.sleep(2)
