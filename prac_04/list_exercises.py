def main():
    numbers = get_number()
    average = sum(numbers)/len(numbers)
    print("The first number is: ", numbers[0])
    print("The last number is: ", numbers[-1])
    print("The smallest number is: ", min(numbers))
    print("The largest number is: ", max(numbers))
    print("The average of the numbers is: ", average)


def get_number():
    numbers = []
    for i in range(5):
        try:
            number = float(input(f"Enter number {i + 1}: "))
            numbers.append(number)
        except ValueError:
            print("Error, please enter a valid number.")
            return get_number()
    return numbers


if __name__ == "__main__":
    main()


def main():
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_input = input("Please enter your name: ")
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()




