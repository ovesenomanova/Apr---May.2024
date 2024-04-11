from math import pi, sin, cos

class Geometric_formulas:

    @staticmethod
    def triangle(a, b):
        S = a * b / 2
        return S

    @staticmethod
    def triangle_v1(a, b, angle):
        S = a * b * sin(angle) / 2
        return S

class MathUtils:

    @staticmethod
    def max(a, b, c, d):
        max_arg = a
        for arg in [a, b, c, d]:
            if max_arg < arg:
                max_arg = arg
        return max_arg

    @staticmethod
    def min(a, b, c, d):
        min_arg = a
        for arg in [a, b, c, d]:
            if min_arg > arg:
                min_arg = arg
        return min_arg

    @staticmethod
    def aver(a, b, c, d):
        return (a+b+c+d)/4

    @staticmethod
    def factorial(a):
        if a == 0:
            return 1
        else:
            return a * MathUtils.factorial(a-1)

print(MathUtils.factorial(8))
print(MathUtils.aver(1, 2, 6, 8))
print(MathUtils.min(5, 10, 15, 20))
print(MathUtils.max(1, 2, 6, 8))

class Human:
    def __init__(self, name):
        self.name = name

    def get_x(self):
        return self.name

    def set_x(self, value):
        self.name = value
