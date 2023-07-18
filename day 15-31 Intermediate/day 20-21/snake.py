import turtle
import random

START_POS = [(0, 0), (-20, 0), (-40, 0)]
COLOURS=[(248, 187, 208),(244, 143, 177),(240, 98, 146)]
MOVE_DIST=20
UP=90
LEFT=180
DOWN=270
RIGHT=0

class Snake:


    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head= self.segments[0]
        self.head_mod()

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def head_mod(self):
        self.head.color("pink")
        self.head.shape("circle")
        self.head.shapesize(1.0, 1.3)
    def add_segment(self,pos):
        new_seg = turtle.Turtle()
        new_seg.shape("square")
        new_seg.color(COLOURS[random.randint(0,2)])
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)



    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)