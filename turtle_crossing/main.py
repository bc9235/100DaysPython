import time
from turtle import Screen
from player import Player, FinishLine
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.title("Turtle Crossing")
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player, car manager, car speed scoreboard, finish line
player = Player()
car_manager = CarManager()
car_speed = car_manager.speed
scoreboard = Scoreboard()
finish_line = FinishLine()

# Capture player input
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_cars(car_speed)

    # Detect player crossing finish line
    if player.ycor() > 275:
        scoreboard.change_level()
        player.go_to_start()
        # Speed up cars
        car_speed = car_manager.speed_up()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
