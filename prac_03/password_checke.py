"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
# Function to check if a password meets the required criteria
def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    # TODO: count each kind of character (use str methods like isdigit)
    for char in password:
        if char.isdigit():
            count_digit = True
        elif char.islower():
            count_lower = True
        elif char.isupper():
           count_upper = True
        elif not char.isalnum() and SPECIAL_CHARS_REQUIRED:
           count_special = 0
        # TODO: if any of the 'normal' counts are zero, return False
    return count_digit and count_lower and count_upper and (count_special or not SPECIAL_CHARS_REQUIRED)

# Get user input for password and validate it
while True:
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    password = input("Enter your password: ")

    if is_valid_password(password):
        print("Valid password!")


        count_digit = sum(1 for char in password if char.isdigit())
        count_lower = sum(1 for char in password if char.islower())
        count_upper = sum(1 for char in password if char.isupper())
        count_special_character = sum(1 for char in password if not char.isalnum())

        print(f"Number of digits: {count_digit}")
        print(f"Number of lowercase letters: {count_lower}")
        print(f"Number of uppercase letters: {count_upper}")
        print(f"Number of special characters: {count_special_character}")

        break
    else:
        print("Invalid password. Please make sure your password meets the requirements.")
