from config import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message):
        message = MIMEText(message, "plain", "utf-8")
        message["Subject"] = Header("Ódýr flugtilboð", "utf-8")
        message["From"] = my_email
        message["To"] = yahoo_email
        
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(message["From"], message["To"], message.as_string())
