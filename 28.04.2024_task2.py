class Ship:
    def __init__(self, buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching, displacement, load_capacity,
                 cargo_passenger_capacity, speed, autonomy_navigation):
        self.buoyancy = buoyancy
        self.stability = stability
        self.unsinkability = unsinkability
        self.propulsion = propulsion
        self.manageability = manageability
        self.smoothness_pitching = smoothness_pitching
        self.displacement = displacement
        self.load_capacity = load_capacity
        self.cargo_passenger_capacity = cargo_passenger_capacity
        self.speed = speed
        self.autonomy_navigation = autonomy_navigation

    def print(self):
        print(
            f' Плавучесть: {self.buoyancy},устойчивость: {self.stability}, непотопляемость: {self.unsinkability}, '
            f'ходкость {self.propulsion}, управляемость {self.manageability}, плавность качки: {self.smoothness_pitching},
            f' водоизмещение: {self.displacement}, грузоподьемность: {self.load_capacity}, грузо- и пассажировместимость: {self.cargo_passenger_capacity},
            f' скорость хода: {self.speed}, автономность плавания: {self.autonomy_navigation}')

    def __repr__(self):
        return f'{self.buoyancy, self.stability, self.unsinkability, 
            self.propulsion, self.manageability, self.smoothness_pitching,
            self.displacement, self.load_capacity, self.cargo_passenger_capacity,
            self.speed, self.autonomy_navigation}'


class Frigate (Ship):
    def __init__(self, buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching, displacement, load_capacity,
                 cargo_passenger_capacity, speed, autonomy_navigation, feature):
        super().__init__(buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching, displacement, load_capacity,
                 cargo_passenger_capacity, speed, autonomy_navigation)
        self.feature = feature

    def set_displacement(self, displacement_new):
        self.displacement = displacement_new

    def get_displacement(self):
        return self.displacement


class Destroyer (Ship):
    def __init__(self, buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching, displacement, load_capacity,
             cargo_passenger_capacity, speed, autonomy_navigation, type):
        super().__init__(buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching, displacement, load_capacity,
                         cargo_passenger_capacity, speed, autonomy_navigation)
        self.type = type

    def set_type(self, type_new):
        self.type = type_new

    def get_type(self):
        return self.type


class Cruiser (Ship, Destroyer):
    def __init__(self, buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching, displacement,
                 load_capacity, cargo_passenger_capacity, speed, autonomy_navigation, type):
        super().__init__(buoyancy, stability, unsinkability, propulsion, manageability, smoothness_pitching,
            displacement, load_capacity, cargo_passenger_capacity, speed, autonomy_navigation)
        Destroyer.__init__(self, type)

