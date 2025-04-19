#  Copyright (c) Ioannis E. Kommas 2024. All Rights Reserved
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def a_gmail(email_send, subj, word):
    email_user = os.getenv("GMAIL_USER")
    email_password = os.getenv("GMAIL_PASS")
    msg = MIMEMultipart()
    msg["From"] = formataddr((os.getenv("GMAIL_FROM"), email_user))
    msg.set_charset("utf-8")
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
    print(f"Το e-mail {email_send} στάλθηκε επιτυχώς")


# ----------------MAIN PROGRAM--------------------
def send_mail(mail_lst, mail_names, word):
    """
    Στέλνει email σε μια λίστα παραληπτών με τα αντίστοιχα ονόματα και το κείμενο.

    :param mail_lst: Λίστα με τις διευθύνσεις email των παραληπτών.
    :param mail_names: Λίστα με τα ονόματα ή τους τίτλους των παραληπτών.
    :param word: Το μήνυμα που θέλετε να στείλετε.
    """
    if len(mail_lst) != len(mail_names):
        raise ValueError("Οι λίστες mail_lst και mail_names πρέπει να έχουν ίδιο μήκος.")

    for email, name in zip(mail_lst, mail_names):
        subject = f"S: {name}"  # Δημιουργία του subject για κάθε email
        print(f"Αποστολή μηνύματος στον παραλήπτη ({email}) με θέμα: {subject}")
        a_gmail(email, subject, word)



