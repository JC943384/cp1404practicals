print("calculation of price ")
# Number of items
num_items = int(input("Number of items: "))

# Initializing total price
total_price = 0

# Getting price of each item and calculating total price
for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

# Displaying total price
print(f"Total price for {num_items} items is ${total_price:.2f}")

