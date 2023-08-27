from car import Car

limo = Car(100, "Limo")
limo.add_fuel(20)
print(f"Fuel in the car: {limo.fuel}")
distance = 115
limo.drive(distance)
print(limo)
