#  Copyright (c) Ioannis E. Kommas 2022. All Rights Reserved
import time as ctime
import os
import shutil
from Files import plot
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from mikrotik import mikrotik_app
from Youtrack import youtrack_app
from Entersoft import PoS, Online_Offline, compare_years, entersoft_plot, daily_bar_plot, PDA
from MyNetwork import network_devices
from dotenv import load_dotenv

def offline(emoji, path, offline_path):
    delete_all_files_inside_folder(offline_path)
    file = f"{emoji}/switch-off.png"
    dir_list = os.listdir(path)
    for dfile in dir_list:
        my_image = Image.open(f"{path}/{dfile}")
        overlay = Image.open(file)
        width, height = overlay.size
        overlay = overlay.resize((width // 3, height // 3))
        my_image.paste(overlay, (11000, 6975), mask=overlay)
        # image_editable = ImageDraw.Draw(my_image)
        my_image.save(f"{offline_path}/{dfile}")
    delete_all_files_inside_folder(path)
    for dfile in os.listdir(offline_path):
        shutil.copy2(f"{offline_path}/{dfile}", f"{path}/{dfile}")
    delete_all_files_inside_folder(offline_path)


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


def paste_image(my_image, overlay_image, xy, resize=1):
    overlay = Image.open(overlay_image)
    width, height = overlay.size
    overlay = overlay.resize((width // resize, height // resize))
    my_image.paste(overlay, xy, mask=overlay)
    # image_editable = ImageDraw.Draw(my_image)
    return my_image


def run(df, path, path_2, file_in, specific_date, plot_df, multiple_data, status_users_elounda, monthly_turnover_df, df_customers):
    start = ctime.perf_counter()
    load_dotenv()
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

    print("🟢SETUP ONLINE BUTTON || ", end='')
    for image in images:
        paste_image(image, f"{path}/switch-on.png", (11000, 6975), 3)

    PoS.get_Pos(path=path, images=images, editables=editables, font=dates_font_parse, multiple_data=multiple_data)  # Entersoft PoS
    print("🟢Entersoft PoS || ", end="")

    if multiple_data == 3:
        # PoS.get_Pos(path=path, images=images, editables=editables, font=dates_font_parse)  # Entersoft PoS
        # print("🟢Entersoft PoS || ", end="")
        network_devices.run(images, path)
        entersoft_plot.plot_run_monthly_turnover(monthly_turnover_df, path, images)  # Entersoft Monthly TurnOver Donut
        print("🟢Entersoft Donut Monthly TurnOver || ", end='')
        daily_bar_plot.run_daily_smooth(plot_df, specific_date, f"{path}/graph.png", path, images)     # Entersoft Daily TurnOver Bar
        print("🟢Entersoft Bar Plot Daily Turn Over|| ", end='')
        Online_Offline.online_offline(images, editables, status_users_elounda, path, timestamp_font_parse)  # ENTERSOFT ONLINE OFFLINE USERS
        print("🟢Entersoft Online Offline Users || ", end="")
        # PDA.run(f"{path}/sankey_pda.png", images)

    if multiple_data in (0, 3):
        youtrack_df = youtrack_app.main()
        dataframe = mikrotik_app.run()
        vpn_status = mikrotik_app.connect_via_ssh()

        youtrack_image = f"{path}/youtrack.png"
        Vpn_Online = f"{path}/Vpn_Online.png"
        Vpn_Offline = f"{path}/Vpn_Offline.png"
        # run mikrotik get dataframe

        mikrotik_app.write(dataframe, images, editables, number_font_parse, timestamp_font_parse)
        print("🟢Mikrotik Total Attacks || ", end="")

        for i, image in enumerate(images, start=1):
            plot.plot_run_mikrotik(i, dataframe,
                                   path_b=image,
                                   path=path)
            print("🟢Mikrotik Plotting || ", end="")
            # plot.plot_run_youtrack(i, path, youtrack_df, youtrack_image,
            #                        path_b=image)
            # print("🟢Youtrack Plotting || ", end="")

            vpn_X = 5600
            step = 200
            vpn_Y = 350
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
                image = paste_image(image,vpn_status_result, box, 2)

    c1 = ctime.perf_counter()
    if multiple_data in (2, 3):
        # Entersoft Years To Date
        compare_years.run(specific_date, df, images, editables, title_font_year, dates_font_parse, timestamp_font_parse,
                          time, number_font_parse)
        print("🟢Entersoft Compare Years|| ", end="")
    if multiple_data == 2:
        # Customers
        compare_years.customers(specific_date, images,editables,df_customers, number_font_parse, title_font_year, dates_font_parse,timestamp_font_parse, time)
        PoS.cancelled_transactions(images=images, editables=editables, font=timestamp_font_parse, placement=(5_000, 7000))
        PoS.cash_credit(images=images, editables=editables, font=timestamp_font_parse, placement=(1_50, 7000))

    time = datetime.now().strftime("%d%m%Y%H%M%S")
    my_image_1.save(f"{path}/TEMP/{file_in}_{time}_1.jpg")
    my_image_2.save(f"{path}/TEMP/{file_in}_{time}_2.jpg")
    my_image_3.save(f"{path}/TEMP/{file_in}_{time}_3.jpg")

    c2 = ctime.perf_counter()
    print(f"🟢DONE IN: {round(c2 - c1)} sec WRITING YTD || ", end="")

    delete_all_files_inside_folder(f"{path_2}/", "kommas.png")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_1.jpg", f"{path_2}/{file_in}_1.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_2.jpg", f"{path_2}/{file_in}_2.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_3.jpg", f"{path_2}/{file_in}_3.jpg")
    shutil.copy2(f"{path}/TEMP/{file_in}_{time}_2.jpg", f"{path_2}/{file_in}_4.jpg")
    c3 = ctime.perf_counter()
    print(f" 🟢DONE IN: {round(c3 - c2)} sec PLOTTING GRAPH ", end="")
    ctime.sleep(2)
