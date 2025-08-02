import os
import sys

from SQL_FOLDER import fetch_data

def set_today_changes(images, editables, store_info):
    color = os.getenv("COLOR_A")

    def get_count(temp_df):
        return int(temp_df.COUNT.iloc[0]) if not temp_df.empty else 0

    SQL_FILES = [
        "ESFIItem_a.sql",
        "ESFIItem_b.sql",
        "ESFIPricelistItem_a.sql",
        "ESFIItemEntry_ESFIItemPeriodics_d.sql",
        "today_transactions.sql"
    ]

    price_change = fetch_data.get_sql_data(SQL_FILES[0])
    new_product = fetch_data.get_sql_data(SQL_FILES[1])
    special_price = fetch_data.get_sql_data(SQL_FILES[2])
    customer_prefer = fetch_data.get_sql_data(SQL_FILES[3])
    transactions = fetch_data.get_sql_data(SQL_FILES[4])

    product_info = {
        "price_change": get_count(price_change),
        "new_product": get_count(new_product),
        "special_price": get_count(special_price),
        "customer_prefer": get_count(customer_prefer),
        "transactions": get_count(transactions),
    }

    product_info_texts = [
        {"info_key": "", "y": 1300, "text_prefix": "Today Live Changes"},
        {"info_key": "price_change", "y": 1450, "text_prefix": "Price Changes"},
        {"info_key": "new_product", "y": 1600, "text_prefix": "New Products"},
        {"info_key": "customer_prefer", "y": 1750, "text_prefix": "Unique Sold Products"},
        {"info_key": "transactions", "y": 1900, "text_prefix": "Transactions"},
        {"info_key": "special_price", "y": 2050, "text_prefix": "Special Offers"},
    ]

    for image, image_editable in zip(images, editables):
        for info_text in product_info_texts:
            position = (150, info_text["y"])
            text = f"{info_text['text_prefix']}: {product_info.get(info_text['info_key'], '')}"
            if info_text['info_key'] == "":
                # Γράφει το κύριο τίτλο
                image_editable.text(position, text, color, font=store_info)
                # Υπολογίζει το "κουτί" του κειμένου (Pillow 8.0+)
                if hasattr(image_editable, "textbbox"):
                    bbox = image_editable.textbbox(position, text, font=store_info)
                    underline_y = bbox[3] + 2
                    image_editable.line(
                        [(bbox[0], underline_y), (bbox[2], underline_y)],
                        fill=color, width=6
                    )
                else:
                    # Για παλαιότερη έκδοση Pillow
                    text_size = image_editable.textsize(text, font=store_info)
                    underline_y = position[1] + text_size[1] + 2
                    image_editable.line(
                        [ (position[0], underline_y), (position[0]+text_size[0], underline_y) ],
                        fill=color, width=6
                    )
            else:
                image_editable.text(position, text, color, font=store_info)