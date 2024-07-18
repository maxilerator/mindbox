import math

from baseclass import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi
