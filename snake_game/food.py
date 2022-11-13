from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Inherit from Turtle Class"""
        super().__init__()
        # set food attributes
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Make food appear at random points on the screen."""
        # 260 x & y coordinates so that food doesn't appear on scoreboard and within boundaries
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
