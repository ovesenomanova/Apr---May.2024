class Auto:
                                            #     Реализуйте класс «Автомобиль». Необходимо хранить
                                            # в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
    def __init__(self, model, year, brand, capacity, color, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.capacity = capacity
        self.color = color
        self.price = price
                                                # Реализуйте методы класса для ввода данных, вывода данных
    def print(self):
        print(
            f'Модель{self.model}, марка автомобиля {self.brand} {self.year} год выпуска с объемом двигателя {self.capacity} литров, цвет {self.color} и стоимостью {self.price} рублей')

    def input(self):
        input(f' Заполните поля для автомобиля. '
               f'Модель{self.model}, марка автомобиля {self.brand} {self.year} год выпуска с объемом двигателя {self.capacity} литров, цвет {self.color} и стоимостью {self.price} рублей ')
                                                # Реализуйте доступ к отдельным полям через методы класса
    def set_model(self, model_new):
        self.model = model_new

    def set_year(self, year_new):
        self.year = year_new

    def set_brand(self, brand_new):
        self.brand = brand_new

    def set_capacity(self, capacity_new):
        self.capacity = capacity_new

    def set_color(self, color_new):
        self.color = color_new

    def set_price(self, price_new):
        self.price = price_new

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_brand(self):
        return self.brand

    def get_capacity(self):
        return self.capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def __repr__(self):
        return f'{self.model, self.year, self.brand, self.capacity, self.color, self.price}'
                                        # Добавьте конструктор, а также необходимые перегруженные методы
    def __add__(self, other):
        if type(other) == int:
            return Auto(self.model, self.year, self.brand, self.capacity, self.color, self.price + other)
        if type(other) == Auto:
            return Auto(self.model, self.year, self.brand, self.capacity, self.color, self.price + other.price)

    def __sub__(self, other):
        if type(other) == int:
            return Auto(self.model, self.year, self.brand, self.capacity, self.color, self.price - other)
        if type(other) == Library:
            return Auto(self.model, self.year, self.brand, self.capacity, self.color, self.price - other.price)

    def __lt__(self, other):
        if type(other) == int:
            return self.price < other
        if type(other) == Auto:
            return self.price < other.price

    def __gt__(self, other):
        if type(other) == int:
            return self.book_price > other
        if type(other) == Auto:
            return self.price > other.price

    def __le__(self, other):
        if type(other) == int:
            return self.price <= other
        if type(other) == Auto:
            return self.price <= other.price

    def __ge__(self, other):
        if type(other) == int:
            return self.price >= other
        if type(other) == Auto:
            return self.price >= other.price

    def __eq__(self, other):
        if type(other) == int:
            return self.price == other
        if type(other) == Auto:
            return self.price == other.price

    def __ne__(self, other):
        if type(other) == int:
            return self.price != other
        if type(other) == Auto:
            return self.price != other.price
