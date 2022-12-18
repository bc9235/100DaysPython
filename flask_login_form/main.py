from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASS = os.environ["PASS"]

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ["WTF_CSRF_SECRET_KEY"]


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Invalid Email Address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if request.method == "POST":
        if login_form.email.data == EMAIL and login_form.password.data == PASS:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
