from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASS = os.environ["PASS"]
PROVIDER = os.environ["PROVIDER"]
PORT = int(os.environ["PORT"])

app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def home():
    return render_template("index.html", content=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for entry in posts:
        if entry["id"] == index:
            requested_post = entry
    return render_template("post.html", content=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(PROVIDER, PORT) as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(EMAIL, EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
