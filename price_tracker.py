import os
import requests
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# Set URL and User Agent
URL = os.environ["PRODUCT_URL"]
USER_AGENT = os.environ["USER_AGENT"]

EMAIL = os.environ["EMAIL"]
PASS = os.environ["PASS"]
PROVIDER = os.environ["PROVIDER"]
PORT = int(os.environ["PORT"])
RECIPIENT = os.environ["RECIPIENT"]

# Set header to send with request
header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.9",
}

# Make request
response = requests.get(url=URL, headers=header).text

# Input content to BS and specify parser
soup = BeautifulSoup(response, "html.parser")

# Get item name and price
name = soup.find(name="span", id="productTitle").getText()
whole_num = soup.find(name="span", class_="a-price-whole").getText()
fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = float(f"{whole_num}{fraction}")

# Set threshold price
threshold = 70

if price < threshold:
    # Send email alert
    with smtplib.SMTP(PROVIDER, PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject:Low price alert!\n\n{name} for ${price}!\n{URL}"
        )
