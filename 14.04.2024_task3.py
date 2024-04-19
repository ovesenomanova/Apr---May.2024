class Stadium:
    # Реализуйте класс «Стадион».Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость.
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
                    # Реализуйте методы класса для ввода данных, вывода данных
    def print(self):
        print(
            f'Стадион {self.name} открыт {self.opening_date} в стране {self.country} в городе {self.city} с вместимостью {self.capacity}')

    def input(self):
        input(f'Стадион {self.name} открыт {self.opening_date} в стране {self.country} в городе {self.city} с вместимостью {self.capacity}')
                                                # Реализуйте доступ к отдельным полям через методы класса
    def set_name(self, name_new):
        self.name = name_new

    def get_name(self):
        return self.name

    def set_opening_date(self, opening_date_new):
        self.opening_date = opening_date_new

    def get_opening_date(self):
        return self.opening_date

    def set_country(self, country_new):
        self.country = country_new

    def get_country(self):
        return self.country

    def set_city(self, city_new):
        self.city = city_new

    def get_city(self):
        return self.city

    def set_capacity(self, capacity_new):
        self.capacity = capacity_new

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f'{self.name, self.opening_date, self.country, self.city, self.capacity}'
                        # Реализуйте доступ к отдельным полям через методы класса
    def __lt__(self, other):
        if type(other) == int:
            return self.capacity < other
        if type(other) == Stadium:
            return self.capacity < other.capacity

    def __gt__(self, other):
        if type(other) == int:
            return self.capacity > other
        if type(other) == Stadium:
            return self.capacity > other.capacity

    def __le__(self, other):
        if type(other) == int:
            return self.capacity <= other
        if type(other) == Stadium:
            return self.capacity <= other.capacity

    def __ge__(self, other):
        if type(other) == int:
            return self.capacity >= other
        if type(other) == Stadium:
            return self.capacity >= other.capacity

    def __eq__(self, other):
        if type(other) == int:
            return self.capacity == other
        if type(other) == Stadium:
            return self.capacity == other.capacity

    def __ne__(self, other):
        if type(other) == int:
            return self.capacity != other
        if type(other) == Stadium:
            return self.capacity != other.capacity

