"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random

def calculate_socre(score):
    if score < 0 or score > 100:
       return "Invalid score"
    elif 90 >score > 50:
        return "Passable"
    elif score > 90:
       return "Excellent"
    else:
       return "Bad"

def main():
    user_score = float(input("Enter your score: "))
    user_result = calculate_socre(user_score)
    print("You score:", user_result)

    random_score = random.randint(0, 100)
    random_result = calculate_socre(random_score)
    print(f"Random score:{random_score}, Result: {random_result}")
if __name__ == "__main__":
    main()