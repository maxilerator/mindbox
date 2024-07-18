import math
from typing import List

from baseclass import Figure


class Triangle(Figure):
    def __init__(self, sides: List[float]):
        if len(sides) != 3:
            raise ValueError("Triangle must have exactly three sides")
        sides = sorted(sides)
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Bad parameters")
        self.sides = sides

    def __half_meter(self):
        return self.sides[0] * 0.5 + self.sides[1] * 0.5 + self.sides[2] * 0.5

    def area(self):
        half_meter = self.__half_meter()
        return math.sqrt(half_meter * (half_meter - self.sides[0]) * (half_meter - self.sides[1]) * (half_meter - self.sides[2]))

    def is_rectangular(self):
        return math.isclose(self.sides[0]**2 + self.sides[1]**2, self.sides[2]**2)