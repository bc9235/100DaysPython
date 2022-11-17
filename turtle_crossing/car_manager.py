from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.hideturtle()

    def make_car(self):
        random_y_pos = randint(-250, 250)
        random_chance = randint(1, 6)
        if random_chance == 3:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(300, random_y_pos)
            self.all_cars.append(new_car)

    def move_cars(self, speed):
        for car in self.all_cars:
            car.forward(speed)

    def speed_up(self):
        self.speed *= 1.25
        return self.speed
