from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game!")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
l_score = Scoreboard(-100, 200)
r_score = Scoreboard(100, 200)

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()
        ball.update_speed()

    if ball.xcor() < -350:
        ball.change_dir()
        r_score.update()

    if ball.xcor() > 350:
        ball.change_dir()
        l_score.update()

screen.exitonclick()
