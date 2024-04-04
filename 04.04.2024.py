
class Car:
    def __init__(self, speed):
        self.speed = speed

obj = Car(100)
print(obj.speed)

crates = []
class Crate:
    def __init__(self, pos, size, health):
        self.pos = pos
        self.health = health
        self.size = size
        self.is_broken = False
        crates.append(self)
    def get_damage(self, amount):
        self.health -= amount
    def set_pos(self, new_pos):
        self.pos = new_pos
    def get_pos(self):
        return self.pos

c1 = Crate([0, 0], 10, 10)
c2 = Crate([10, 8], 8, 8)
c1.set_pos( input() )
c2.get_damage(3)
print(c1.health)

class Human:
    def __init__(self, FIO, data_of_birth, tel, city, country, address):
        self.FIO = FIO
        self.data_of_birth = data_of_birth
        self.tel = tel
        self.city = city
        self.country = country
        self.address = address
    def set_FIO(self, FIO_new):
        self.FIO = FIO_new
    def set_data_of_birth(self, data_of_birth_new):
        self.data_of_birth = data_of_birth_new
    def set_city(self, city_new):
        self.city = city_new
    def set_country(self, country_new):
        self.country = country_new
    def set_tel(self, tel_new):
        self.tel = tel_new
    def set_address(self, address_new):
        self.address = address_new
    def get_FIO(self):
        return self.FIO
    def get_data_of_birth(self):
        return self.data_of_birth
    def get_tel(self):
        return self.tel
    def get_city(self):
        return self.city
    def get_country(self):
        return self.country
    def get_address(self):
        return self.address

