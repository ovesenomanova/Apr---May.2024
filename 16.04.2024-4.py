class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_full(self):
        return self.day + self.month * 30 + self.year * 365

    def set_full(self, date_new):
        self.year = date_new // 365
        date_new = date_new % 365
        self.month = date_new // 30
        date_new = date_new % 30
        self.day = date_new // 30

    def __add__(self, other):
        day_new = self.get_full() + other.get_full()
        new_date = Date(0, 0, 0)
        new_date.set_full(day_new)
        return new_date

    def __sub__(self, other):
        day_new = self.get_full() - other.get_full()
        new_date = Date(0, 0, 0)
        new_date.set_full(day_new)
        return new_date

    def __repr__(self):
        return f'{self.day, self.month, self.year}'


i1 = Date(12, 11, 2000)
i2 = Date(1, 3, 2010)
print(i1 + i2)


