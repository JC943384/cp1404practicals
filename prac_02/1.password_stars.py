def main():
    password = get_password()
    the_password(password)

def get_password():
    password = input("Refactor password check program to use functions: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Refactor password check program to use functions: ")
    return password
def the_password(password):
    print("*" * len(password))
main()
