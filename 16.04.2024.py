class Number:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if type(other) == int:
            return Number(self.x + other)
        if type(other) == Number:
            return Number(self.x + other.x)


    def __sub__(self, other):
        x = self.x - other
        return Number(x)


    def __mul__(self, other):
        x = self.x * other
        return Number(x)


    def __truediv__(self, other):
        x = self.x / other
        return Number(x)

    def __repr__(self):
        return f'{self.x}'


x = Number(5)
print(x + 3, x + Number(9))


