import pandas as pd
import datetime as dt
import smtplib
import random

# SMTP Credentials
MY_EMAIL = "USERNAME@EMAIL.COM"
MY_PASSWORD = "PASSWORD"


def mod_template(name):
    """Choose letter and modify letter templates with recipient name."""
    chosen_letter = random.randint(1, 3)
    file_path = f"letter_templates/letter_{chosen_letter}.txt"

    default = "[NAME]"

    with open(file_path) as letter:
        lines = letter.read()
        new_lines = lines.replace(default, name)
    return new_lines


def send_email(body, email):
    """Send modified template to email address."""
    with smtplib.SMTP("smtp.YOURPROVIDER.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:HAPPY BIRTHDAY!\n\n{body}"
        )


# Get current date
now = dt.datetime.now()
now_month = now.month
now_day = now.day

# Read birthdays CSV and convert to dictionary
birthdays = pd.read_csv("birthdays.csv")
birthday_list = birthdays.to_dict(orient="records")

# Determine if there are any birthdays on current date
for entry in birthday_list:
    if entry["month"] == now_month and entry["day"] == now_day:
        recipient = entry["name"]
        address = entry["email"]
        message = mod_template(recipient)
        send_email(message, address)
