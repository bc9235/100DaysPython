from turtle import Turtle

POSITION = (0, 240)
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)
        self.color("white")
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}          {self.r_score}", align=ALIGNMENT, font=FONT)
