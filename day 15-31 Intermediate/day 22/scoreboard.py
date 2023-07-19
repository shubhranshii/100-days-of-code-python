from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score=0
        self.goto(x, y)
        self.display()


    def display(self):
        self.write(self.score, align="center", font=('Courier', 75, 'normal'))

    def update(self):
        self.clear()
        self.score+=1
        self.display()
