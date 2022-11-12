from turtle import Turtle, Screen
from random import randint

race = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("grey")
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?  Enter a color: ")
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
turtles = []
y_start = -180

for num in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_start)
    y_start += 70
    turtles.append(new_turtle)

if user_bet:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner.lower() == user_bet.lower():
                turtle.home()
                turtle.write(f"You won!  {winner} won the race!", align="center", font=("Arial", 20, "normal"))
            else:
                turtle.home()
                turtle.write(f"You lose.  {winner} won the race.", align="center", font=("Arial", 20, "normal"))
        else:
            move = randint(0, 10)
            turtle.forward(move)

screen.exitonclick()
