"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def get_celsius():
    global celsius
    celsius = float(input("Celsius: "))
    return celsius


def celsius_to_fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_fahrenheit():
    global fahrenheit
    fahrenheit = float(input("fahrenheit:"))
    return fahrenheit


def fahrenheit_to_celsius():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


while choice != "Q":
    if choice == "C":
        get_celsius()
        celsius_to_fahrenheit()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        get_fahrenheit()
        fahrenheit_to_celsius()
        print(f"Result:{celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
