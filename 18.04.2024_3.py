class Animal:
    def __init__(self, weight, habitat_halo, number, frugivory):
        self.weight = weight
        self.habitat_halo = habitat_halo
        self.number = number
        self.frugivory = frugivory

    def move(self, speed):
        self.speed = speed


class Tiger(Animal):
    def __init__(self, weight, habitat_halo, number, frugivory, spotting):
        super().__init__(weight, habitat_halo, number, frugivory)
        self.spotting = spotting


class Сrocodile(Animal):
    def __init__(self, weight, habitat_halo, number, frugivory, tail_length):
        super().__init__(weight, habitat_halo, number, frugivory)
        self.tail_length = tail_length


class Kangaroo(Animal):
    def __init__(self, weight, habitat_halo, number, frugivory, jumping_ability):
        super().__init__(weight, habitat_halo, number, frugivory)
        self.jumping_ability = jumping_ability
