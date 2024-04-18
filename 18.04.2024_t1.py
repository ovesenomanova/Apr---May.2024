class Human:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Builder(Human):
    def __init__(self, name, age, address, qualification):
        super().__init__(name, age, address)
        self.qualification = qualification


class Sailor(Human):
    def __init__(self, name, age, address, seaworthiness):
        super().__init__(name, age, address)
        self.seaworthiness = seaworthiness


class Pilot(Human):
    def __init__(self, name, age, address, rank):
        super().__init__(name, age, address)
        self.rank = rank


