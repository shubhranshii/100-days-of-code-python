from turtle import Screen, Turtle


class DrawBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.draw()

    def draw(self):
        self.hideturtle()
        self.color(109,76,65)
        self.speed("fastest")
        self.penup()
        self.goto(-235, -235)
        self.pendown()
        for x in range(4):
            self.forward(460)
            self.left(90)

