# T4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PatchedPoint(Point):
    def __init__(self, *args):
        print(args)
        print("Размер:", len(args))
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                # ((0, 1))
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)


# Размер 0. args = ()
point1 = PatchedPoint()
# Размер 1. args = ((0, 1))
point2 = PatchedPoint((0, 1))
# Размер 2. args = (4, 2)
point3 = PatchedPoint(4, 2)
# Размер 2. args = ((0, 1), (1, 0)) -> (0, 1), (1, 0)
point4 = PatchedPoint((0, 1), (1, 0))
print(point1.x, point1.y)
print(point2.x, point2.y)
print(point3.x, point3.y)
print(point4.x, point4.y)