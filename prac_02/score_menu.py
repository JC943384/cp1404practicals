# cp1404 JiahaoSong 14310531
menu = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result 
(S)how stars 
(Q)uit
"""


def main():
    score = get_valid_score()

    print("Valid score obtained:", score)
    while True:
        print(menu)
        choice = input("Please enter a choice: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = print_result(score)
            print(f"Print {score} result is:", result)
        elif choice == "S":
            print("The score show stars:")
            show_star(score)
        elif choice == "Q":
            print("Thank you!")
            break
        else:
            print("Error choice, please enter again.")


def get_valid_score():
    while True:
        try:
            score = int(input("Please enter a score(between 0 to 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error,please enter a score 0-100.")
        except ValueError:
            print("Invalid input, please enter a valid integer score(0-100).")


def print_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_star(score):
    print("*" * score)


if __name__ == "__main__":
    main()
