from turtle import Turtle, Screen, colormode
from random import choice


def make_row():
    for dot in range(15):
        # choose random color from list for each dot
        pen.color(choice(colors))
        pen.dot(20)
        pen.penup()
        pen.forward(50)
        pen.pendown()


# set starting location of each row, moving up the y axis for each row
def set_location(y):
    location = (-300, y)
    pen.penup()
    pen.setpos(location)
    

screen = Screen()

# colors in RGB
colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
          (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
          (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
          (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

pen = Turtle()
pen.hideturtle()
pen.speed("fastest")
colormode(255)

# y axis starting point
y = -200

# make 9 rows of dots
for num in range(9):
    set_location(y)
    make_row()
    y += 50

screen.exitonclick()
