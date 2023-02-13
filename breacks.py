from turtle import Turtle as t
from constence import *


class Bobble(t):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(2)
        self.penup()
        self.goto(1000, 1000)


class MakeBobbles:

    def __init__(self):

        self.bobble_list = []
        for n in range(63):
            new = Bobble()
            self.bobble_list.append(new)
        self.x = 420
        self.start_y = 50
        self.give_color()

    def give_color(self):
        for item in self.bobble_list[:15]:
            item.color(colors[0])
        for item in self.bobble_list[15:31]:
            item.color(colors[1])
        for item in self.bobble_list[31:47]:
            item.color(colors[2])
        for item in self.bobble_list[47:]:
            item.color(colors[3])

    def build_row(self):

        for circle in self.bobble_list:

            if self.x > -450:
                circle.goto(self.x, self.start_y)
                self.x -= 60
            else:
                self.start_y += 50
                self.x = 420

