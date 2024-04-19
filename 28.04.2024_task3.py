class Money:
    def __init__(self, type_whole, whole_part, type_fractional, fractional_part):
        self.type_whole = type_whole
        self.whole_part = whole_part
        self.type_fractional = type_fractional
        self.fractional_part = fractional_part

    def set_type_whole(self, type_whole_new):
        self.type_whole = type_whole_new

    def get_type_whole(self):
        return self.type_whole

    def set_type_fractional(self, type_fractional_new):
        self.type_fractional = type_fractional_new

    def get_type_fractional(self):
        return self.type_fractional

    def print(self):
        print(
            f'{self.type_whole}: {whole_part} и {type_fractional}: {fractional_part}')

    def __repr__(self):
        return f'{self.type_whole, self.whole_part, self.type_fractional, self.fractional_part}'


