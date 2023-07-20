from turtle import Turtle

class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()

    def write_state(self, state_name,x,y):
        self.goto(x,y)
        self.write(state_name)
