"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    user_score = float(input("Enter your score: "))
    result = calculate_score(user_score)
    print(f"Your enter score result is: ", result)

    random_score = random.randint(0, 100)
    random_result = calculate_score(random_score)
    print(f"Random score: {random_score}, Result: {random_result}.")


def calculate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()
