from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

my_turtle = Turtle()
my_screen = Screen()

my_turtle.shape("turtle")

sides = 3

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(sides):
    colour = my_turtle.pencolor(random_color())
    for y in range(sides):
        angle = 360 / sides
        my_turtle.forward(100)
        my_turtle.right(angle)

for x in range(8):
    draw_shape(sides)
    sides += 1


my_screen.exitonclick()
