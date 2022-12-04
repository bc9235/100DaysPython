from datetime import datetime
import os
import requests

EXERCISE_ID = os.environ["EXERCISE_ID"]
EXERCISE_KEY = os.environ["EXERCISE_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

# Set up user info
GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT KG
HEIGHT_CM = YOUR HEIGHT CM
AGE = YOUR AGE

# Get date and time info
now = datetime.now()
today = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M")

# # Set up exercise API call
exercise_text = input("What exercise did you do? ")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_header = {
    "x-app-id": EXERCISE_ID,
    "x-app-key": EXERCISE_KEY,
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Call API to pull exercise data
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_header)
exercise_results = exercise_response.json()["exercises"]


# # Set up Sheety data
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# # Pull data to add to sheet
for entry in exercise_results:
    exercise = entry["user_input"]
    duration = entry["duration_min"]
    calories = entry["nf_calories"]

    sheety_params = {
        "workout":
            {
                "date": today,
                "time": time,
                "exercise": exercise,
                "duration": str(duration),
                "calories": calories,
             }
    }

#     # Make API call to enter data to sheet
    enter_data = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
