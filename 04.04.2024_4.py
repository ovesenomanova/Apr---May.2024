class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def set_n(self, n_new):
        self.n = n_new
    def set_d(self, d_new):
        self.d = d_new
    def get_n(self):
        return self.n
    def get_d(self):
        return self.d
    def __add__(self, other):
        n = self.n * other.d + self.d + other.n
        d = self.d + other.n
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.n * other.d - self.d + other.n
        d = self.d + other.n
        return Fraction(n, d)
    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        return Fraction(n, d)
    def __truediv__(self, other):
        n = self.n * other.d
        d = self.d * other.n
        return Fraction(n, d)
    def __repr__(self):
        return f'{self.n}/{self.d}'


i1 = Fraction(3, 5)
i2 = Fraction(4, 9)
print(i1 + i2, i1 - i2,)
print( i1 * i2)
print(i1/i2)
