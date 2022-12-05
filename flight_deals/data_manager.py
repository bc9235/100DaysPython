import os
from dotenv import load_dotenv
import requests

load_dotenv()


class DataManager:

    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
        self.SHEETY_AUTH = os.environ["SHEETY_AUTH"]
        self.header = {
            "Authorization": f"Bearer {self.SHEETY_AUTH}"
        }

    def get_destinations(self):
        """Get destinations from Google Sheet, return as list"""
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.header).json()["prices"]

        destinations = [entry["city"] for entry in response]
        return destinations

    def get_low_prices(self):
        """Get low prices from Google Sheet, return as dictionary"""
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.header).json()["prices"]
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
            requests.put(url=f"{self.SHEETY_ENDPOINT}/{id}", headers=self.header, json=data)
            id += 1
