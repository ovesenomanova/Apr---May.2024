class Passport:
    def __init__(self, FIO, date_of_Birth, country, number, series, issued_by, code):
        self.FIO = FIO
        self.date_of_Birth = date_of_Birth
        self.country = country
        self.number = number
        self.series = series
        self.issued_by = issued_by
        self.code = code

    def set_FIO(self, FIO_new):
        self.FIO = FIO_new

    def set_date_of_Birth(self, date_of_Birth_new):
        self.date_of_Birth = date_of_Birth_new

    def set_country(self, country_new):
        self.country = country_new

    def set_number(self, number_new):
        self.number = number_new

    def set_issued_by(self, issued_by_new):
        self.issued_by = issued_by_new

    def set_code(self, code_new):
        self.code = code_new

    def get_FIO(self):
        return self.FIO

    def get_date_of_Birth(self):
        return self.date_of_Birth

    def get_country(self):
        return self.country

    def get_number(self):
        return self.number

    def get_issued_by(self):
        return self.issued_by

    def get_code(self):
        return self.code


class Foreign_Passport (Passport):
    def __init__(self, FIO, date_of_Birth, country, number, series, issued_by, code, visa):
        super__init__(FIO, date_of_Birth, country, number, series, issued_by, code)
        self.visa = visa

    def set_visa(self, visa_new):
        self.visa = visa_new