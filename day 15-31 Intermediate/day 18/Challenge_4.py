
import random
import turtle

turtle.colormode(255)

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_turtle.shape("turtle")
my_turtle.pensize(8)
my_turtle.speed("fastest")

sides = 3


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_segment():
    colour = my_turtle.pencolor(random_color())
    direction = random.choice([0, 90, 180, 270])
    my_turtle.right(direction)
    my_turtle.forward(40)


for x in range(100):
    draw_segment()

my_screen.exitonclick()
