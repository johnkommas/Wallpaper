def main_body(store_name, retail_point, time):
    html_start = """
<!DOCTYPE html>
<html>
"""
    html_head = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Pay Notification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4; /* Light gray background */
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            background: #ffffff; /* White container */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        .logo {
            position: absolute;
            top: 15px;
            right: 15px;
            width: 100px;
        }
        h2 {
            color: #d9534f;
            text-align: center;
        }
        p {
            font-size: 16px;
            color: #333;
            line-height: 1.5;
        }
        ul {
            padding-left: 20px;
        }
        ul li {
            font-size: 16px;
            margin-bottom: 8px;
        }
        .highlight {
            font-weight: bold;
            color: #555; /* Grey instead of blue */
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #777;
            margin-top: 20px;
        }
        .signature {
            text-align: center;
            margin-top: 20px;
        }
        .signature img {
            height: 120px;
            border: 0;
        }
    </style>
</head>
"""

    html_body = f"""
<body>
    <div class="container">
        <!-- e-Pay Logo -->
        <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/epay.png?raw=true" alt="e-Pay Logo" class="logo">

        <h2>🚨 Σημαντική Ειδοποίηση: <br> Προβληματική Εγγραφή Πληρωμής</h2>

        <p>Αγαπητή ομάδα,</p>

        <p>Έχει εντοπιστεί εγγραφή πληρωμής που περιέχει σφάλματα, τα οποία ενδέχεται να εμποδίσουν την ολοκλήρωση της διαδικασίας κλεισίματος (Ζ) από τον φορολογικό μηχανισμό.</p>

        <p>Για να επιλύσετε το ζήτημα, παρακαλώ προβείτε στις ακόλουθες ενέργειες:</p>
        <ul>
            <li>🛠️ <strong>Διορθώστε</strong> την εγγραφή πληρωμής, ώστε να μην εμποδίζεται το κλείσιμο (Ζ) από τον φορολογικό μηχανισμό.</li>
            <li>📑 <strong>Ενημερώστε</strong> για τις ενέργειες που πραγματοποιήσατε και προκάλεσαν το συγκεκριμένο ζήτημα.</li>
            <li>🚀 <strong>Προτείνετε</strong> λύσεις για την αποφυγή παρόμοιων προβλημάτων στο μέλλον.</li>
        </ul>

        <p>Στοιχεία για το ζήτημα:</p>
        <ul>
        <li><span class="highlight">📌 Κατάστημα:</span> {store_name}</li>
        <li><span class="highlight">🖨️ Φορολογικός Μηχανισμός:</span> {retail_point}</li>
        <li><span class="highlight">⏰ Χρόνος Εντοπισμού:</span> {time}</li>
        </ul>
        <p>Για οποιαδήποτε απορία ή τεχνική υποστήριξη, μπορείτε να επικοινωνήσετε μαζί μας στο <a href="mailto:johnkommas@gmail.com">johnkommas@gmail.com</a>.</p>

        <div class="signature">
            <img alt="Signature" src="https://raw.githubusercontent.com/johnkommas/CodeCademy_Projects/master/img/mail/order/emb24.png">
        </div>

        <div class="footer">
            <p style="margin: 0; text-align: center;">
                <span style="font-size: 14px; line-height: 24px;">Copyright© Ioannis E. Kommas. All rights reserved.</span>
            </p>
        </div>
    </div>
</body>
"""

    html_end = "</html>"

    html = html_start + html_head + html_body + html_end
    return html

