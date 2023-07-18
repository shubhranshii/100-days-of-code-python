import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


def forward():
    my_turtle.forward(10)

def backward():
    my_turtle.backward(10)

def rotate_counter():
    my_turtle.left(10)

def rotate_clock():
    my_turtle.right(10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=forward)
my_screen.onkey(key="s", fun=backward)
my_screen.onkey(key="a", fun=rotate_counter)
my_screen.onkey(key="d", fun=rotate_clock)
my_screen.onkey(key="c", fun=clear)

my_screen.exitonclick()
