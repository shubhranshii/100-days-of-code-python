import turtle
import random

turtle.colormode(255)
my_screen = turtle.Screen()
my_screen.setup(width=500, height=400)
y_pos = [-75, -45, -15, 15, 45, 75]
turtles = []
race = False

colours=["pink","turquoise","magenta","cyan","violet","green"]


for index in range(0, 6):
    my_turtle = turtle.Turtle(shape="turtle")
    my_turtle.color(colours[index])
    my_turtle.speed("fastest")
    my_turtle.penup()
    my_turtle.goto(-230, y_pos[index])
    turtles.append(my_turtle)

user_bet = my_screen.textinput(title="make a bet", prompt="which turtle will win? choose a colour!")
if user_bet:
    race = True

while race:
    for index in range(0, 6):
        cr_turtle = turtles[index]
        turtle_at_pos = list(cr_turtle.position())
        if turtle_at_pos[0] >= 210:
            winner = cr_turtle.pencolor()
            race = False
            break
        else:
            cr_turtle.forward(random.randint(1, 10))

if winner == user_bet:
     print(f"You've won. {winner} is the winner!")
else:
    print(f"You've lost. {winner} is the winner! ")
my_screen.exitonclick()
