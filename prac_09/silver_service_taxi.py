from taxi import Taxi  # Assuming the Taxi class is defined in a file named taxi.py


class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        base_price_per_km = 1.23  # Set your default base price_per_km here
        price_per_km = base_price_per_km * fanciness
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return super().__str__() + f" plus flagfall of ${self.flagfall:.2f}"








