from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 275


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


class FinishLine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setheading(180)
        self.goto(-300, FINISH_LINE_Y - 5)
        self.pendown()
        self.width(5)
        self.goto(300, FINISH_LINE_Y - 5)
