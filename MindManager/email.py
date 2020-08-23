import os
import smtplib

EMAIL_ADDRESS = "eduassistant32@gmail.com"
EMAIL_PASS = input("Enter Password: ")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

    subject = "EduAssistant: Your friend reported being sad"
    body = "Fill this in later, this is a test."

    msg = f'Subject: {subject}\n\n{body}'

    # format is sender, reciever, msg
    smtp.sendmail(EMAIL_ADDRESS, "quentinromero@outlook.com", msg)