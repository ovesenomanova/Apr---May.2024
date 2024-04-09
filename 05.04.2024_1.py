class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        x = self.x ** 2
        y = self.y ** 2
        v = (x + y) ** 0.5
        return v


va = Vector(5, 4)
print(len(va))
