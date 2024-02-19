"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion"""


def celsius_to_fahrenheit():
    celsius = float(input("Please enter a Celsius temperature: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius():
    fahrenheit = float(input("Please enter a Fahrenheit temperature: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        result = celsius_to_fahrenheit()
        print(f"Result: {result:.2f} F")
    elif choice == "F":
        result = fahrenheit_to_celsius()
        print(f"Result: {result:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
