def main():
    password = get_password()
    the_password(password)


def get_password():
    password = input("Refactor password check program to use functions, please enter your password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Refactor password check program to use functions, please enter your password:: ")
    return password


def the_password(password):
    print(f"The password is: {'*' * len(password)}")


main()
