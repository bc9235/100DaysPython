import os
from dotenv import load_dotenv
import requests

load_dotenv()


class DataManager:

    def __init__(self):
        self.SHEETY_PRICES = os.environ["SHEETY_PRICES"]
        self.SHEETY_USERS = os.environ["SHEETY_USERS"]
        self.SHEETY_AUTH = os.environ["SHEETY_AUTH"]
        self.header = {
            "Authorization": f"Bearer {self.SHEETY_AUTH}"
        }

    def get_destinations(self):
        """Get destinations from Google Sheet, return as list"""
        response = requests.get(url=self.SHEETY_PRICES, headers=self.header).json()["prices"]

        destinations = [entry["city"] for entry in response]
        return destinations

    def get_low_prices(self):
        """Get low prices from Google Sheet, return as dictionary"""
        response = requests.get(url=self.SHEETY_PRICES, headers=self.header).json()["prices"]
        low_prices = {entry["city"]: entry["lowestPrice"] for entry in response}
        return low_prices

    def add_codes(self, iata_codes):
        """Add IATA codes to Google Sheet"""
        id = 2  # Google sheet row number
        for entry in iata_codes:
            data = {
                "price": {
                    "iataCode": entry,
                }
            }
            requests.put(url=f"{self.SHEETY_PRICES}/{id}", headers=self.header, json=data)
            id += 1

    def create_user(self):
        """Create new user.  Return True for success, False for failure."""
        print("Welcome to Brendan's Flight Club!  Please create an account.")
        first = input("What is your first name?\n")
        last = input("What is your last name?\n")
        email1 = input("What is your email address?\n")
        email2 = input("Please re-enter your email address.\n")

        if email1 == email2:
            new_user = {
                "user": {
                    "firstName": first,
                    "lastName": last,
                    "email": email1,
                }
            }

            response = requests.post(url=self.SHEETY_USERS, headers=self.header, json=new_user)
            print("Welcome to the Flight Club!")
            return True

        else:
            print("Email does not match, please retry.")
            return False

    def get_email_list(self):
        """Return list of email addresses of users"""
        response = requests.get(url=self.SHEETY_USERS, headers=self.header).json()["users"]
        email_list = [entry["email"] for entry in response]
        return email_list
