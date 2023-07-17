import colorgram
import random
import turtle

my_turtle=turtle.Turtle()
my_screen=turtle.Screen()
my_screen.title("This turtle is a painter!")
my_turtle.speed("fastest")
my_turtle.hideturtle()
turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 6)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

y_pos=-80

for x in range(10):
    my_turtle.penup()
    my_turtle.setposition(-80,y_pos)
    y_pos += 20
    for y in range (10):
        my_turtle.pencolor(random.choice(rgb_colors))
        my_turtle.pendown()
        my_turtle.dot(10)
        my_turtle.penup()
        my_turtle.forward(20)


my_screen.exitonclick()