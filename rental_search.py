import os
import time
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()

ZILLOW = os.environ["ZILLOW_URL"]
PROPERTY_LINK_PRE = "https://www.zillow.com"
FORM = os.environ["FORM"]
FORM_2 = os.environ["FORM_2"]
DRIVER = os.environ["DRIVER"]

# Set up request header for Zillow so they don't promt for CAPTCHA
header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                  "Safari/537.36",
}

# Use bs4 to scrape data from Zillow search
zillow_response = requests.get(url=ZILLOW, headers=header).text
soup = BeautifulSoup(zillow_response, "html.parser")

# Get property address, price, and links
properties = soup.find_all(class_="property-card-link")

property_links = [entry["href"] for entry in properties]

addresses = []
for entry in properties:
    address = entry.getText().split("|")
    if len(address) > 1:
        addresses.append(address[1])
    else:
        if address[0] != '':
            addresses.append(address[0])

all_prices = soup.find_all("span", {"data-test": "property-card-price"})
property_prices = [entry.getText().split()[0] for entry in all_prices]

# Put all corresponding property info into dictionary
property_info = {}
for i in range(len(addresses)):
    property_info[i] = {
        "address": addresses[i],
        "price": property_prices[i],
        "link": f"{PROPERTY_LINK_PRE}{property_links[i]}",
    }

# Use Selenium to enter data into form
service = Service(DRIVER)
options = Options()
options.add_experimental_option("detach", True)  # Keep window open
driver = webdriver.Chrome(service=service, options=options)

for entry in property_info.items():
    # Open browser to specified URL
    driver.get(FORM)
    # Locate text boxes
    address_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # Locate submit button
    submit_button = driver.find_element(By.CLASS_NAME, "uArJ5e")

    time.sleep(2)
    
    # Fill in data
    address_box.send_keys(entry[1]["address"])
    price_box.send_keys(entry[1]["price"])
    link_box.send_keys(entry[1]["link"])
    submit_button.click()

    time.sleep(2)

    # Get next page
    driver.get(FORM_2)
    new_form = driver.find_element(By.TAG_NAME, "a")
    new_form.click()

driver.quit()
