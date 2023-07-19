import turtle
import time
from player import Player
from write import Write
from car import Car

turtle.colormode(255)
screen= turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor(119, 122, 128)
screen.title("Road Crossing Game")
screen.tracer(0)

player = Player()
writer = Write()
cars= Car()
writer.finish_line()
writer.draw_road()

screen.listen()
screen.onkeypress(player.forward, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    cars.create_cars()
    cars.move_cars()
    time.sleep(0.1)

    for car in cars.cars_list:
        if car.distance(player)<20:
            writer.end_game()
            game_is_on= False

    if player.ycor()>220:
        winner= True
        writer.update()
        player.update()
        cars.update()
        writer.finish_line()
        writer.draw_road()


screen.exitonclick()
