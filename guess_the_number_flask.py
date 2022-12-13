from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def guess_a_number():
    # Flask will accept HTML in return statements
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:guess>")
def check_guess(guess):
    if guess == rand_num:
        page = "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif guess > rand_num:
        page = "<h1 style='color: red'>Too high!  Guess again.</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        page = "<h1 style='color: blue'>Too low!  Guess again.</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    return page


rand_num = randint(0, 9)

if __name__ == "__main__":
    app.run()
