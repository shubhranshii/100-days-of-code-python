from turtle import Turtle


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.level = 1
        self.display_level()

    def display_level(self):
        self.goto(-200, 230)
        self.write(f"Level={self.level}", align="center", font=("Courier", 10, "normal"))

    def draw_line(self):
        for x in range(50):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)

    def finish_line(self):
        self.goto(-250, 220)
        self.color("red")
        self.setheading(0)
        self.draw_line()

    def draw_road(self):
        ycord= -220
        self.goto(-250, ycord)
        self.color("white")
        for y in range(11):
            self.goto(-250, ycord)
            self.setheading(0)
            self.draw_line()
            ycord+=40

    def end_game(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"Game Over. You score is {self.level-1}!", align="center", font=("Courier", 12, "normal"))


    def update(self):
        self.level+=1
        self.write(f"YAYY!LEVEL {self.level} COMPLETED!")
        self.clear()
        self.display_level()