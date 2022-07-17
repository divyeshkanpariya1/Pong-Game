from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1)
        self.penup()
        self.speed(10)
        self.goto(xcor, 0)

    def up(self):
        if self.ycor() < 310:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -310:
            self.goto(self.xcor(), self.ycor() - 20)
