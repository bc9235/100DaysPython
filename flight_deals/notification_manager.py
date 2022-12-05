import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


class NotificationManager:

    def __init__(self):
        self.EMAIL_USER = os.environ["EMAIL_USER"]
        self.EMAIL_PASS = os.environ["EMAIL_PASS"]
        self.EMAIL_PROVIDER = os.environ["EMAIL_PROVIDER"]
        self.EMAIL_PORT = os.environ["EMAIL_PORT"]
        self.TWILIO_SID = os.environ["TWILIO_SID"]
        self.TWILIO_KEY = os.environ["TWILIO_KEY"]
        self.TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
        self.TWILIO_RECEIVER = os.environ["TWILIO_RECEIVER"]

    def send_message(self, message_content):
        """Send text messages"""
        client = Client(self.TWILIO_SID, self.TWILIO_KEY)

        message = client.messages \
            .create(
                    body=message_content,
                    from_=self.TWILIO_NUMBER,
                    to=self.TWILIO_RECEIVER,
                    )

    def send_emails(self, email_list, message_content):
        """Send emails to users"""
        for entry in email_list:
            with smtplib.SMTP(self.EMAIL_PROVIDER, int(self.EMAIL_PORT)) as connection:
                connection.starttls()
                connection.login(user=self.EMAIL_USER, password=self.EMAIL_PASS)
                connection.sendmail(
                    from_addr=self.EMAIL_USER,
                    to_addrs=entry,
                    msg=f"Subject: Low Prices on Airfare!\n\n{message_content}"
                )
