import requests
from datetime import datetime, timezone
import smtplib
import time

MY_LAT = "YourLatitude"
MY_LONG = "YourLongitude"

MY_EMAIL = "YourEmail"
MY_PASSWORD = "YourPassword"


def iss_overhead():
    """Determine if the ISS is overhead."""
    # Get current ISS location
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Compare ISS location to current location.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


def is_night():
    """Determine if it is night."""
    # Build dictionary containing parameters to pass to sunrise/sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # Get sunrise/sunset times (times from API in UTC) for current location
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Get hour of sunrise/sunset
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current UTC hour
    utc_hour = datetime.now(tz=timezone.utc).hour

    # Compare current UTC hour to local sunrise/sunset hours
    if utc_hour >= sunset or utc_hour <= sunrise:
        return True


def send_email():
    """Send email."""
    with smtplib.SMTP("smtp.PROVIDER.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="another_email",
            msg="Subject:Look Up!\n\nThe ISS is above you!"
        )


while True:
    # Run once per hour
    time.sleep(3600)
    if iss_overhead() and is_night():
        send_email()
