import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

    def __int__(self):
        return self.area()

    def show(self):
        print("Shape")

    def save(self):
        with open('shape.txt', 'w') as f:
            f.write(f'{self.x, self.y}')

    def load(self):
        with open('shape.txt', 'r') as f:
            f.readline()



class Square (Shape):
    def __init__(self, x, y, a):
        super().__init__(x, y)
        self.a = a

    def area(self):
        return self.a * self.a

    def show(self):
        return f'Площадь квадрата равна {self.area()}'

    def save(self):
        with open('file.txt', 'w') as f:
            f.write(f'{self.x, self.y, self.a}')

    def load(self):
        with open('file.txt', 'r') as f:
            ls = f.readline()
            print(ls)

    def __repr__(self):
        return f'{self.area()}'


class Rectangle (Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def print(self):
        print(f'Площадь прямоугольника равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'


class Circle (Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def print(self):
        print(f'Площадь окружности равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'


class Ellipse(Rectangle):
    def __init__(self, a, b):
        super().__init__(a, b)

    def area(self):
        return math.pi * self.a * self.b

    def print(self):
        print(f'Площадь эллипса равна {self.area()}')

    def __repr__(self):
        return f'{self.area()}'

class ShapeList:
    def __init__(self):
        pass


lst = [Shape(1, 2), Square()]

print(lst[0].show())

# i1 = Square(2, 5, 10)
# i1.save()
# i1.load()

