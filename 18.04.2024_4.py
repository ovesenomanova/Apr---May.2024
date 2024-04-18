import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle_inscribed(Circle, Square):
    def __init__(self, radius, side):
        Circle.__init__(self, radius)
        Square.__init__(self, side)

    def area(self):
        return Square.area(self)

