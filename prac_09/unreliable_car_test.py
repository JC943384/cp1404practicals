from unreliable_car import UnreliableCar

# Create an UnreliableCar with 50% reliability
car1 = UnreliableCar("Car1", fuel=50, reliability=50.0)

# Drive the car 10 kilometers
distance_driven = car1.drive(10)

# Check if the car moved and the distance driven
if distance_driven > 0:
    print(f"{car1.name} drove {distance_driven} kilometers.")
else:
    print(f"{car1.name} failed to start.")

# Create another UnreliableCar with 90% reliability
car2 = UnreliableCar("Car2", fuel=30, reliability=90.0)

# Drive the car 20 kilometers
distance_driven = car2.drive(20)

# Check if the car moved and the distance driven
if distance_driven > 0:
    print(f"{car2.name} drove {distance_driven} kilometers.")
else:
    print(f"{car2.name} failed to start.")
