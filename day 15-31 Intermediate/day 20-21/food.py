from turtle import Turtle
import random
import turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        # add a new shape
        turtle.register_shape('flowers.gif')
        # setting the image as cursor
        self.shape('flowers.gif')
        #self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomx= random.randint(-210,210)
        randomy = random.randint(-210, 210)
        self.goto(randomx,randomy)


