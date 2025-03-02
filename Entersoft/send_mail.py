#  Copyright (c) Ioannis E. Kommas 2024. All Rights Reserved
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def a_gmail(email_send, subj, word):
    email_user = os.getenv("GMAIL_USER")
    email_password = os.getenv("GMAIL_PASS")
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subj
    body = word
    msg.attach(MIMEText(body, "html"))
    text = msg.as_string()

    # Sending the email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_send, text)
    server.quit()
    print("Το e-mail {} στάλθηκε επιτυχώς".format(email_send))


# ----------------MAIN PROGRAM--------------------
def send_mail(mail_lst, mail_names, word):
    for i in range(len(mail_lst)):
        c = "S: {}".format(mail_names[i])
        print("Αποστολή μηνύματος στον παραλήπτη {}".format(mail_names[i]))
        a_gmail(mail_lst[i], c, word)
