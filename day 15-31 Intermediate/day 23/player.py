from turtle import Turtle
START_XPOS=0
START_YPOS=-230
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.update()

    def forward(self):
        self.goto(0,self.ycor()+10)

    def update(self):
        self.goto(START_XPOS, START_YPOS)