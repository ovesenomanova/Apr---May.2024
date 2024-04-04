class index:
    def __init__(self, name, region, population, index, country, tel_code):
        self.name = name
        self.region = region
        self.population = population
        self.index = index
        self.country = country
        self.tel_code = tel_code

    def set_name(self, name_new):
        self.name = name_new

    def set_region(self, region_new):
        self.region = region_new

    def set_index(self, index_new):
        self.index = index_new

    def set_country(self, country_new):
        self.country = country_new

    def set_population(self, population_new):
        self.population = population_new

    def set_tel_code(self, tel_code_new):
        self.tel_code = tel_code_new

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_population(self):
        return self.population

    def get_index(self):
        return self.index

    def get_country(self):
        return self.country

    def get_tel_code(self):
        return self.tel_code


