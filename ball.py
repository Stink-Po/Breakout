import random
from turtle import Turtle as t
from constence import *

class Ball(t):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1.5)
        self.penup()
        self.goto(0, -248)
        self.start = False
        self.x_move = 10
        self.y_move = 10
        self.x = self.xcor()
        self.y = self.ycor()
        self.speed = 0.1

    def start_move(self):
        if not self.start:
            moves = [10, -10]
            random_move = random.randint(0, 1)
            self.x_move = moves[random_move]
            self.start = True
        new_x = self.x + self.x_move
        new_y = self.y + self.y_move
        self.x, self.y = new_x, new_y
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.speed = 0.1
        self.goto(ball_place)
        self.start = False
        self.x = self.xcor()
        self.y = self.ycor()
        self.x_move = 10
        self.y_move = 10
        self.start_move()

    def bounce_wall(self):
        self.x_move *= -1

    def bounce_top(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.y_move = 10
        self.speed *= 0.9

    def positive_x_move(self):
        self.x_move = 10
        self.y_move = 10

    def negative_x_move(self):
        self.x_move = -10

    def negative_y_move(self):
        self.y_move *= -1

    def bounce_bobble(self, left, right, top):
        if not left or not right or not top:
            self.y_move *= -1
        if left:
            self.negative_x_move()

        if right:
            self.positive_x_move()

        if top:
            self.negative_y_move()

