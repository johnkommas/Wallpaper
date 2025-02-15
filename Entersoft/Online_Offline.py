import os
from Files import minimalist_write


def online_offline(images, editables, status_users_elounda, path, timestamp_font_parse, i=0, path_b=None,):
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

            image = minimalist_write.paste_image(image, f"{path}/{color}.png", xy=pots, resize=4)
