from turtle import Turtle as t
from constence import *


class Score(t):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.score = 0
        self.penup()
        self.hideturtle()

    def add_score(self, color):
        if color == colors[0]:
            self.score += 10
            self.write_score()
        elif color == colors[1]:
            self.score += 20
            self.write_score()
        elif color == colors[2]:
            self.score += 50
            self.write_score()
        elif color == colors[3]:
            self.score += 100
            self.write_score()

    def write_score(self):
        self.clear()
        self.goto(score_place)
        self.color("white")
        self.pendown()
        message = f"lives :  {self.lives}     Score : {self.score}   High Score : {score_data.record}"
        self.write(message, font=font, align="left")

    def write_final(self):
        if self.lives == 0:
            self.penup()
            self.goto(-80, 0)
            self.pendown()
            self.clear()
            self.write("Game Over", font=font)
