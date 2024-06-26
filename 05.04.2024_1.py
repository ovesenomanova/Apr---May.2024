class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        x = self.x ** 2
        y = self.y ** 2
        v = (x + y) ** 0.5
        return int(v)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def normalize(self):
        v = len(self)
        x = self.x / v
        y = self.y / v

    def __len__(self):
        ln = (self.x ** 2 + self.y ** 2) ** 0.5
        return int(ln)


    def __repr__(self):
        return f'{self.x, self.y}'


va = Vector(5, 4)
va1 = Vector(6, 8)
print(len(va))
print(va * 2)
print(va + va1)
va1.normalize()
print(va1)


def vector(a, b):
    x = (a.x - b.x)**2
    y = (a.y - b.y)**2
    v = (x + y) ** 0.5
    return v


print(vector(va, va1))

def min_len(vecs):
    minn_vec = vecs[0]
    for vec in vecs:
        if len(vec) < len(minn_vec):
            minn_vec = vec
    return minn_vec


print(min_len(vecs_))


