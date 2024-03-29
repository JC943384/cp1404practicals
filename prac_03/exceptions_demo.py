"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ValueError occurs when I enter something other than a number.

2. When will a ZeroDivisionError occur?
ZeroDivisionError occurs when I enter the denominator is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:  # 3.improve code
        print("please Enter number cannot be equal 0")  # 3.improve code
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
