from turtle import Turtle

# create constants for scoreboard properties
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Initialize Scoreboard"""
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")

    def display(self):
        """Display scoreboard."""
        self.clear()
        self.setposition(-100, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.setposition(100, 270)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        """Add to score and update scoreboard."""
        self.score += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER =[", align=ALIGNMENT, font=FONT)
        
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display()
