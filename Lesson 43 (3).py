# Polymorphism Полиморфизм
import math


class Shape:
    def cal_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return math.pi * pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def cal_area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(10, 5), Circle(15), Rectangle(25, 15)]

for shape in shapes:
    print(shape.cal_area())