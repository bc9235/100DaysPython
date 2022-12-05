from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data = DataManager()
flight_search = FlightSearch()
notifications = NotificationManager()

while True:
    # Create user
    create = sheet_data.create_user()
    if create:
        break

# Get current location IATA code
here = flight_search.current_location_iata()

print("Please wait while we search...")

# Get destination from Google Sheet
destinations = sheet_data.get_destinations()

# Get IATA codes of destinations
codes = flight_search.get_iata_code(destination_list=destinations)

# Add IATA codes to Google Sheet
sheet_data.add_codes(iata_codes=codes)

# Pull flight data
price_data = flight_search.pull_flight_data(iata_codes=codes, current_location=here)

# Pull low prices from Google sheet
low_prices = sheet_data.get_low_prices()

# Pull email addresses from Google sheet
email_list = sheet_data.get_email_list()

# Compare current price to low price
for key in low_prices:
    # If current price lower than low price, send alert message
    if low_prices[key] < price_data[key]:
        message = f"Low price alert!\n{here} -> {key}: ${price_data[key]}"
        notifications.send_message(message_content=message)
        notifications.send_emails(email_list=email_list, message_content=message)
print("Success!  Notifications have been sent.")
