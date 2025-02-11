from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from divider import Divider
import time

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
screen.listen()

# objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
divider = Divider()

# inputs
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

speed = 0.07
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # ball bounces when collided with bounds
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball bounces when collided with paddle and increases speed
    if right_paddle.distance(ball) < 50 and ball.xcor() > 320 or left_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed -= 0.01
        if speed <= 0.02:
            speed = 0.02

    # when player leaves the ball, update score and reset ball speed
    if ball.xcor() > 380:
        score.increase_score_l()
        time.sleep(1)
        ball.home()
        speed = 0.07
        ball.bounce_x()
    elif ball.xcor() < -380:
        score.increase_score_r()
        time.sleep(1)
        ball.home()
        speed = 0.07
        ball.bounce_x()

screen.exitonclick()