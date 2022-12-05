import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:

    def __init__(self):
        self.TWILIO_SID = os.environ["TWILIO_SID"]
        self.TWILIO_KEY = os.environ["TWILIO_KEY"]
        self.TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
        self.TWILIO_RECEIVER = os.environ["TWILIO_RECEIVER"]

    def send_message(self, message_content):
        """Send text message"""
        client = Client(self.TWILIO_SID, self.TWILIO_KEY)

        message = client.messages \
            .create(
                    body=message_content,
                    from_=self.TWILIO_NUMBER,
                    to=self.TWILIO_RECEIVER,
                    )
