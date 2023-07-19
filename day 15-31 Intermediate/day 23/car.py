import turtle
import random

X_CORD = 200
START_MOVE_DIST=10


class Car:
    def __init__(self):
        self.cars_list = []
        self.create_cars()
        self.car_speed= START_MOVE_DIST

    def create_cars(self):
        x_cord = 200
        y_cord = [-200,-160,-120,-80,-40,0,40,80,120,160,200]
        chance = random.randint(1, 3)
        if chance == 1:
            new_car = turtle.Turtle()
            r = random.randint(1, 255)
            g = random.randint(1, 255)
            b = random.randint(1, 255)
            color = (r, g, b)
            new_car.color(color)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=-1, stretch_len=2)
            new_car.penup()
            new_car.goto(x_cord, y_cord[random.randint(0,10)])
            new_car.setheading(180)
            self.cars_list.append(new_car)


    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.car_speed)

    def update(self):
        self.car_speed+=2