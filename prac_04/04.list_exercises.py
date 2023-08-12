def get_numbers():
    numbers = []
    for n in range(5):
        try:
            num = float(input(f"Please Enter number {n+1}: "))
            numbers.append(num)
        except ValueError:
            print("error,please enter a valid number.")
            return get_numbers()
    return numbers
def main():
    numbers = get_numbers()
    average = sum(numbers)/5

    print("The first number is:", numbers[0])
    print("The last number is: ",numbers[-1])
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))
    print("The average of the numbers is:", (average))

if __name__ == "__main__":
    main()

def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_input = input("Please enter your username: ")

    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")
if __name__ == "__main__":
    main()







