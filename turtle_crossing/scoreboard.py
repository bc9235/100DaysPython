from turtle import Turtle

POSITION = (-235, 270)
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def change_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
