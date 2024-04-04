class Country:
    def __init__(self, name_country, continent, population, city, capital, tel_code):
        self.name_country = name_country
        self.continent = continent
        self.population = population
        self.city = city
        self.capital = capital
        self.tel_code = tel_code
    def set_name_country(self, name_country_new):
        self.name_country = name_country_new
    def set_continent(self, continent_new):
        self.continent = continent_new
    def set_city(self, city_new):
        self.city = city_new
    def set_capital(self, capital_new):
        self.capital = capital_new
    def set_population(self, population_new):
        self.population = population_new
    def set_address(self, address_new):
        self.address = address_new
    def get_name_country(self):
        return self.name_country
    def get_continent(self):
        return self.continent
    def get_population(self):
        return self.population
    def get_city(self):
        return self.city
    def get_capital(self):
        return self.capital
    def get_address(self):
        return self.address
