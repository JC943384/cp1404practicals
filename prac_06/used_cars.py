"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, name="my_car")
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, name="limo")
    limo.add_fuel(20)
    print(f"The amount of fuel in {limo.name} is: {limo.fuel}")
    limo.drive(115)
    print(limo)

    limo.add_fuel(199)
    limo.drive(162)
    print(limo)


main()
