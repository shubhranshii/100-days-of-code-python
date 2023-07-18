import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from drawBoard import DrawBoard


turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor(173,213,129)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
board = DrawBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 235 or snake.head.xcor() < -235 or snake.head.ycor() > 235 or snake.head.ycor() < -235:
        game_is_on = False
        score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
