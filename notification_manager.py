from config import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(my_email, my_password)

            for email in emails:
                msg = MIMEText(f"{message}, {google_flight_link}".encode(
                    'utf-8'), 'plain', 'utf-8')
                msg["Subject"] = Header("Ódýr flugtilboð", "utf-8")
                msg["From"] = my_email
                msg["To"] = email

                connection.sendmail(msg["From"], msg["To"], msg.as_string())
