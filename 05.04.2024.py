class Human:
    counter = 0

    @staticmethod
    def total_amount():
        return Human.counter

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Human.counter += 1

    def __len__(self):
        return self.height

    def __add__(self, other):
        return Human(self.name, self.age + other, self.height)

    def __repr__(self):
        return f'HUMAN {self.name}'

    def get_x(self):
        return self.name

    def set_x(self, value):
        self.name = value


h = Human('Petre', 20, 180)
h1 = Human('Jon', 15, 170)
h2 = Human('Olga', 17, 160)
print( len(h) )
h = h + 5
print(h.age, h.name)
print(Human.total_amount())







