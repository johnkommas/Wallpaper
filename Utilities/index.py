def main_body(store_name, retail_point, complete_time):
    date, time = complete_time.split(" ")
    html_start = """
<!DOCTYPE html>
<html lang="el">
"""
    html_head = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Pay Notification</title>
</head>
"""

    html_body = f"""
<body style="font-family: 'SF UI Text', Arial, sans-serif; background-color: #f9f9f9; margin: 0; padding: 0;">
    <div style="max-width: 600px; background: #ffffff; margin: auto; padding: 40px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); position: relative;">
        <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/epay.png?raw=true" alt="e-Pay Logo" style="position: absolute; top: 20px; right: 20px; width: 80px;">
        <h2 style="color: #3c7458; text-align: center; font-size: 22px; margin-bottom: 20px;">Σημαντική Ειδοποίηση</h2>

        <p style="font-size: 16px; color: #333; line-height: 1.6;">Αγαπητή ομάδα,</p>
        <p style="font-size: 16px; color: #333; line-height: 1.6;">Έχει εντοπιστεί εγγραφή πληρωμής που περιέχει σφάλματα, τα οποία ενδέχεται να εμποδίσουν την ολοκλήρωση της διαδικασίας κλεισίματος (Ζ) από τον φορολογικό μηχανισμό το βράδυ.</p>

        <div style="display: flex; align-items: center; text-align: center; margin: 20px 0; font-weight: bold; color: #2cb543;">
            <div style="flex: 1; border-bottom: 1px solid #2cb543; margin: 0 10px;"></div>
            Ενέργειες
            <div style="flex: 1; border-bottom: 1px solid #2cb543; margin: 0 10px;"></div>
        </div>

        <div style="margin-bottom: 15px; display: flex; align-items: center;">
            <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/diamond.png?raw=true" alt="Diamond" style="margin-right: 8px; width: 16px; height: 16px;"> Διορθώστε την εγγραφή πληρωμής, ώστε να μην εμποδίζεται το κλείσιμο (Ζ).
        </div>
        <div style="margin-bottom: 15px; display: flex; align-items: center;">
            <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/diamond.png?raw=true" alt="Diamond" style="margin-right: 8px; width: 16px; height: 16px;"> Ενημερώστε για τις ενέργειες που πραγματοποιήσατε.
        </div>
        <div style="margin-bottom: 15px; display: flex; align-items: center;">
            <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/diamond.png?raw=true" alt="Diamond" style="margin-right: 8px; width: 16px; height: 16px;"> Προτείνετε λύσεις για την αποφυγή παρόμοιων προβλημάτων στο μέλλον.
        </div>

        <div style="display: flex; align-items: center; text-align: center; margin: 20px 0; font-weight: bold; color: #2cb543;">
            <div style="flex: 1; border-bottom: 1px solid #2cb543; margin: 0 10px;"></div>
            Στοιχεία για το ζήτημα
            <div style="flex: 1; border-bottom: 1px solid #2cb543; margin: 0 10px;"></div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border: 1px solid #2cb543; border-radius: 12px; padding: 10px; text-align: center;">
            <div style="flex: 1; text-align: center; font-weight: bold; color: #333;">
                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/calendar.png?raw=true" alt="Calendar Icon" style="width: 20px; height: 20px;"> DATE: {date}
            </div>
            <div style="flex: 1; text-align: center; font-weight: bold; color: #333;">
                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/wallclock.png?raw=true" alt="Clock Icon" style="width: 20px; height: 20px;"> TIME: {time}
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; margin: 20px 0;">
            <div style="text-align: center; width: 45%; display: flex; align-items: center; gap: 10px;">
                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/store.png?raw=true" alt="Store Image" style="max-width: 100px; height: auto;">
                <p style="margin-top: 10px; font-size: 14px; color: #333;">Κατάστημα:<br>{store_name}</p>
            </div>
            <div style="text-align: center; width: 45%; display: flex; align-items: center; gap: 10px;">
                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/retail.png?raw=true" alt="Tax Machine Image" style="max-width: 150px; height: auto;">
                <p style="margin-top: 10px; font-size: 14px; color: #333;">Φορολογικός Μηχανισμός:<br>{retail_point}</p>
            </div>
        </div>

        <p style="font-size: 16px; color: #333; line-height: 1.6;">Με εκτίμηση <br> Τμήμα Μηχανογράφησης</p>

        <div style="text-align: center; margin-top: 20px;">
            <img src="https://raw.githubusercontent.com/johnkommas/CodeCademy_Projects/master/img/mail/order/emb24.png" alt="Signature" style="height: 100px;">
        </div>

        <div style="text-align: center; font-size: 14px; color: #777; margin-top: 30px; padding-top: 15px; border-top: 1px solid #2cb543;">
            <p>&copy; 2025 Ioannis E. Kommas. All rights reserved.</p>
        </div>
    </div>
</body>
"""

    html_end = "</html>"

    html = html_start + html_head + html_body + html_end
    return html

