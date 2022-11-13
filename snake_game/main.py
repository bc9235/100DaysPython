from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# create screen and set screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# create snake, food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen for arrows to command direction of snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

in_progress = True
while in_progress:
    scoreboard.display()
    # update screen to make snake segments appear to move as one
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # detect collision with wall, top wall at bottom of scoreboard
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        in_progress = False
        scoreboard.game_over()

    # detect collision with tail
    # start with index 1
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            in_progress = False
            scoreboard.game_over()

screen.exitonclick()
