class Rectangle:
    def __init__(self, *coords):
        self.__width = abs(coords[0][0] - coords[1][0])
        self.__height = abs(coords[0][1] - coords[1][1])

    def perimeter(self):
        return round(2 * (self.__width + self.__height), 2)

    def area(self):
        return round(self.__width * self.__height, 2)

rec1 = Rectangle((1, 2), (3, 4))
print(rec1.area())
print(rec1.perimeter())