import requests
from datetime import date, timedelta
from twilio.rest import Client

NEWS_KEY = "YOURKEY"
STOCK_KEY = "YOURKEY"
STOCK = "COMPANYTICKER"
COMPANY_NAME = "COMPANYNAME"
TWILIO_SID = "YOURSID"
TWILIO_KEY = "YOURKEY"
TWILIO_NUM = "YOURNUMBER"

# Get yesterday date and day prior
yesterday = date.today() - timedelta(1)
day_prior = date.today() - timedelta(2)

# Set up Stock API Parameters
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_KEY,
}

# Make stock API call
stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()

# Closing prices for yesterday and the day before
yesterday_close = stock_response.json()["Time Series (Daily)"][str(yesterday)]["4. close"]
day_prior_close = stock_response.json()["Time Series (Daily)"][str(day_prior)]["4. close"]

# Calculate change in price between two dates close
price_change = round(((float(yesterday_close) - float(day_prior_close)) / float(day_prior_close)) * 100)

# Set up News API parameters
news_url = "https://newsapi.org/v2/everything"
news_params = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME,
    "searchIn": "description",
    "from": day_prior,
    "to": yesterday,
    "pageSize": 3,
}

# If price change greater than 1%, pull news articles, send text messages
if price_change > 1:
    # Make News API call
    news_response = requests.get(url=news_url, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    # Pull title, description from response for messages
    messages = [f"{article['title']}\n{article['description']}" for article in news_data]

    # Send messages using Twilio API
    for entry in messages:
        client = Client(TWILIO_SID, TWILIO_KEY)
        message = client.messages \
            .create(body=f"{STOCK} {price_change}%\n{entry}", from_=TWILIO_NUM, to="YOURNUMBER")
