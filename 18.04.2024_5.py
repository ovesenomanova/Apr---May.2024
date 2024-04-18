class Wheels:
    def __init__(self, radius, width):
        self.radius = radius
        self.width = width


class Engine:
    def __init__(self, gradation, transmission):
        self.gradation = gradation
        self.transmission = transmission


class Doors:
    def __init__(self, color):
        self.door_color = color


class Auto (Wheels, Engine, Doors):
    def __init__(self, model, year, brand, capacity, mileage, color):
        self.model = model
        self.year = year
        self.brand = brand
        self.capacity = capacity
        self.mileage = mileage
        self.color = color
        Wheels.__init__(self, radius, width)
        Engine.__init__(self, gradation, transmission)
        Doors.__init__(self, door_color)

    def drive(self, miles):
        self.mileage += miles
