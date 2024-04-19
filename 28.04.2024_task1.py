class Device:
    def __init__(self, type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price):
        self.type_device = type_device
        self.dimensions = dimensions
        self.safety_class = safety_class
        self.energy_consumption = energy_consumption
        self.manufacturer = manufacturer
        self.country = country
        self.warranty_period = warranty_period
        self.price = price

    def print(self):
        print(
            f'Тип устройства: {self.type_device}, габариты: {self.dimensions}, класс безопасности {self.safety_class}, энергопотребление: {self.energy_consumption}'
            f' производитель: {self.manufacturer}, страна: {self.country}, гарантийный срок эксплуатации {self.warranty_period}, цена: {self.price}')

    def __repr__(self):
        return f'{self.type_device, self.dimensions, self.safety_class, self.energy_consumption, self.manufacturer,
        self.country, self.warranty_period, self.price}


class CoffeeMachine (Device):
    def __init__(self, type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price, degree_grinding, product_range):
        super().__init__(type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price)
        self.degree_grinding = degree_grinding
        self.product_range = product_range

    def print(self):
        print(
            f'Кофемашина {self.type_device}, габариты: {self.dimensions}, класс безопасности {self.safety_class}, энергопотребление: {self.energy_consumption}'
            f' производитель: {self.manufacturer}, страна: {self.country}, гарантийный срок эксплуатации {self.warranty_period}, цена: {self.price}, '
            f'степень помола:  {self.degree_grinding}, ассортимент продукта: {self.product_range}')

    def set_name(self, type_device_new):
        self.type_device = type_device_new

    def get_type_device(self):
        return self.type_device


class Blender (Device):
    def __init__(self, type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price, weight, type):
        super().__init__(type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price)
        self.weight = weight
        self.type = type

    def print(self):
        print(
            f'Блендер {self.type_device}, габариты: {self.dimensions}, класс безопасности {self.safety_class}, энергопотребление: {self.energy_consumption}'
            f' производитель: {self.manufacturer}, страна: {self.country}, гарантийный срок эксплуатации {self.warranty_period}, цена: {self.price}, '
            f'вес:  {self.weight}, тип: {self.type}')

    def set_name(self, type_device_new):
        self.type_device = type_device_new

    def get_type_device(self):
        return self.type_device


class MeatGrinder (Device, Blender):
    def __init__(self, type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price, power, type):
        super().__init__(type_device, dimensions, safety_class, energy_consumption, manufacturer, country, warranty_period, price)
        Blender.__init__(self, type)
        self.power = power

    def print(self):
        print(
            f'Мясорубка {self.type_device}, габариты: {self.dimensions}, класс безопасности {self.safety_class}, энергопотребление: {self.energy_consumption}'
            f' производитель: {self.manufacturer}, страна: {self.country}, гарантийный срок эксплуатации {self.warranty_period}, цена: {self.price}, '
            f'мощность:  {self.power}, тип: {self.type}')

    def set_name(self, type_device_new):
        self.type_device = type_device_new

    def get_type_device(self):
        return self.type_device




