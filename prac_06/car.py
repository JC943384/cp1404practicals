class Car:
    def __init__(self, fuel, name="Car"):
        self.fuel = fuel
        self.odometer = 162
        self.name = name

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        fuel_needed = distance * (78/115)
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.odometer += distance
        else:
            print("Not enough fuel to drive that far!")

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer} "

