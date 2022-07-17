from turtle import Turtle
import random

STARTING_ANGLE = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.starting_pos()
        self.move_speed = 0.085

    def starting_pos(self):
        angle = random.choice(STARTING_ANGLE)
        y = random.randint(-300, 300)
        self.goto(0, y)
        self.move_speed = 0.1
        self.setheading(angle)

    def move_ball(self):
        self.forward(20)
        if self.ycor() > 340 or self.ycor() < -340:
            if self.heading() == 45 or self.heading() == 225:
                self.setheading(self.heading() + 270)
            else:
                self.setheading(self.heading() + 90)

    def change_dir(self):
        if self.heading() == 135 or self.heading() == 315:
            self.setheading(self.heading() - 90)
            self.move_speed *= 0.9

        elif self.heading() == 45 or self.heading() == 225:
            self.setheading(self.heading() + 90)
            self.move_speed *= 0.9
