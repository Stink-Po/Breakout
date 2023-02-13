from turtle import Turtle as t
from constence import *


class Paddle(t):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(paddle_place)
        self.x = self.xcor()
        self.y = self.ycor()

    def move_left(self):
        if self.x >= -400:
            new_x = self.x - 40
            self.x = new_x
            self.goto(new_x, self.y)

    def move_right(self):
        if self.x <= 400:
            new_x = self.x + 40
            self.x = new_x
            self.goto(new_x, self.y)
