import math
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass


class Rectangle (Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def print(self):
        print(f'Площадь прямоугольника равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'


class Circle (Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def print(self):
        print(f'Площадь окружности равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'


class Triangle_right (Shape, Rectangle):
    def __init__(self, a, b):
        super().__init__()
        Rectangle.__init__(self, a, b)

    def area(self):
        return self.a * self.b * 0.5

    def print(self):
        print(f'Площадь прямоугольного треугольника равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'

class Trapezoid (Shape, Rectangle):
    def __init__(self, a, b, h):
        super().__init__()
        Rectangle.__init__(self, a, b)
        self.h = h

    def area(self):
        return (self.a + self.b * self.h)/2

    def print(self):
        print(f'Площадь трапеции равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'
