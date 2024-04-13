"""
CP1404/CP5632 Practical
Car class
"""
class Taxi:
    def __init__(self, name, fuel, price_per_km, flagfall=0):
        self.name = name
        self.fuel = fuel
        self.price_per_km = price_per_km
        self.flagfall = flagfall
        self.odometer = 0
        self.current_fare_distance = 0

    def __str__(self):
        if self.flagfall > 0:
            return "{} - fuel={}, odometer={}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(self.name, self.fuel, self.odometer, self.current_fare_distance, self.price_per_km, self.flagfall)
        else:
            return "{} - fuel={}, odometer={}, {}km on current fare, ${:.2f}/km".format(self.name, self.fuel, self.odometer, self.current_fare_distance, self.price_per_km)


    def get_fare(self):
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        if distance <= self.fuel:
            self.odometer += distance
            self.fuel -= distance
            self.current_fare_distance += distance
            return distance
        else:
            distance_possible = self.fuel
            self.odometer += distance_possible
            self.fuel = 0
            self.current_fare_distance += distance_possible
            return distance_possible

