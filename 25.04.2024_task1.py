class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def lenght (self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)

    def __repr__(self):
        return f'{self.x}, {self.y}'


point = Point(3, 5)
print(point.x, point.y)



class PatchedPoint (Point):
    def __init__(self, *args):
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)