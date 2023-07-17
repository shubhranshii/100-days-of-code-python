
import random
import turtle

turtle.colormode(255)

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_turtle.shape("turtle")
my_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph(size):
    for x in range (int(360/size)):
        my_turtle.pencolor(random_color())
        current_heading = my_turtle.heading()
        my_turtle.circle(50)
        my_turtle.setheading(current_heading - 10)

draw_spirograph(5)
my_screen.exitonclick()
