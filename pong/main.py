import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Make paddles, ball, scoreboard
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

# Move paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

play_game = True
while play_game:
    scoreboard.update_scoreboard()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    # Detect if right misses, add point to left
    if ball.xcor() > 380:
        scoreboard.l_score += 1
        ball.reset_ball()
        ball.bounce_x()

    # Detect if left misses, add point to right
    if ball.xcor() < -380:
        scoreboard.r_score += 1
        ball.reset_ball()
        ball.bounce_x()

screen.exitonclick()
