import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class FlightSearch:

    def __init__(self):
        self.FLIGHT_ENDPOINT = os.environ["FLIGHT_ENDPOINT"]
        self.FLIGHT_TOKEN = os.environ["FLIGHT_TOKEN"]
        self.header = {
            "apikey": self.FLIGHT_TOKEN
        }

    def current_location_iata(self):
        """Get IATA code for current location"""
        current_location = input("What is your current location? ").title()
        search_params = {
            "term": current_location,
            "location_types": "city",
        }
        response = requests.get(url=f"{self.FLIGHT_ENDPOINT}/locations/query", headers=self.header,
                                params=search_params).json()["locations"][0]["code"]
        return response

    def get_iata_code(self, destination_list):
        """Get IATA codes for destination cities."""
        codes = []
        for city in destination_list:
            search_params = {
                "term": city,
                "location_types": "city",
            }

            response = requests.get(url=f"{self.FLIGHT_ENDPOINT}/locations/query", headers=self.header,
                                    params=search_params).json()["locations"]
            codes.append(response[0]["code"])
        return codes

    def pull_flight_data(self, iata_codes, current_location):
        """Make API call to pull flight price data.  Return dictionary."""
        # Get date information to add to search parameters
        today = datetime.now()
        six_months_later = today + timedelta(days=180)
        today_format = datetime.now().strftime('%d/%m/%Y')
        six_months_format = six_months_later.strftime('%d/%m/%Y')

        # Empty dictionary to store prices pulled from API
        dest_prices = {}

        for entry in iata_codes:
            search_params = {
                "fly_from": current_location,
                "fly_to": entry,
                "date_from": today_format,
                "date_to": six_months_format,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": True,
                "curr": "USD",
            }

            try:
                response = requests.get(url=f"{self.FLIGHT_ENDPOINT}/search", headers=self.header,
                                        params=search_params).json()["data"][0]
            except IndexError:
                print(f"No flights found for {entry}.")
            else:
                destination = response["cityTo"]
                price = response["price"]
                # Store city name as key and price as value to dictionary
                dest_prices[destination] = price

        return dest_prices

