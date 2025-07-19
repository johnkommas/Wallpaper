import os
from dateutil.relativedelta import relativedelta


def write_years_and_days(image_editable, df_years, specific_date, dates_for_every_year, title_font_year,
                         dates_font_parse, timestamp_font_parse, time, counter, c=1, x = 500, y=900):
    years = [str(i) for i in df_years]
    check_year = specific_date.year - 5
    colors = [os.getenv("COLOR_A"), os.getenv("COLOR_B"), os.getenv("COLOR_C")]
    custom_color = colors[counter]

    for i, year in enumerate(years):
        # Ελέγχει αν το year ταιριάζει με το check_year
        text_to_draw = (dates_for_every_year[i] if year == str(check_year) else dates_for_every_year[i])
        image_editable.text(
            (x, y),
            text_to_draw,
            custom_color,
            font=dates_font_parse,
        )
        # Ενημερώνει το check_year αν χρειάζεται
        if year == str(check_year):
            check_year = int(year)
        image_editable.text((x, y-500), year, custom_color, font=title_font_year)
        x += 660
        check_year += 1
    if c == 1:
        # write timestamp refreshed data
        image_editable.text((10100, 7000), time, custom_color, font=timestamp_font_parse)


def write_revenue_values(image_editable, data, number_font_parse, counter, x_offsets, y_offsets=700):
    for i in data:
        revenue = str(int(i))
        if i == max(data) and counter == 2:
            image_editable.text(
                (x_offsets[len(revenue)] + 400, y_offsets),
                revenue,
                os.getenv("COLOR_C"),
                font=number_font_parse,
            )
        else:
            image_editable.text(
                (x_offsets[len(revenue)] + 400, y_offsets),
                revenue,
                os.getenv("COLOR_A"),
                font=number_font_parse,
            )
        x_offsets = [y + 660 for y in x_offsets]


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


def run(specific_date, df, images, editables, title_font_year, dates_font_parse, timestamp_font_parse, time, number_font_parse):
    counter = 0
    # ΠΡΟΣΘΕΤΩ ΤΙΣ ΗΜΕΡΕΣ ΓΙΑ ΚΑΘΕ ΧΡΟΝΟ
    dates_for_every_year = get_date_for_every_year(specific_date)
    x_offsets = [0, 310, 260, 215, 170, 120, 75]

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
        write_revenue_values(editable, data, number_font_parse, counter, x_offsets)
        counter += 1


def customers(specific_date, images, editables, df_cs, number_font_parse, title_font_year, dates_font_parse,timestamp_font_parse, time, x_offsets, y_offset=700, x=7200):
    # WRITING CUSTOMERS DATA
    # x_offsets = [6700, 7010, 6960, 6915, 6870, 6820, 6775]
    counter = 0
    # ΠΡΟΣΘΕΤΩ ΤΙΣ ΗΜΕΡΕΣ ΓΙΑ ΚΑΘΕ ΧΡΟΝΟ
    dates_for_every_year = get_date_for_every_year(specific_date)
    data = list(df_cs.COUNT.values)
    df_years = list(df_cs.YEAR.values)
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
            counter=counter,
            c =0,
            x=x,
            y = y_offset+200
        )
        # WRITING CUSTOMER VALUES
        write_revenue_values(editable, data, number_font_parse, counter, x_offsets, y_offset)
        counter += 1

    # END OF WRITING CUSTOMERS DATA