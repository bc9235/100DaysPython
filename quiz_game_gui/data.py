import requests

# Set parameters for API call
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Make API Call, store response data to question_data
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
