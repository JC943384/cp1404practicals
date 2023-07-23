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
def start(score):
    print("*" * score)

def get_score():
    while True:
        try:
            score = int(input("Enter a score need between 0 to 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("error,please enter score 0-100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")
import random

def calculate_sandard(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 90 > score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"

def start(score):
    print("*" * score)


def get_score():
    while True:
        try:
            score = int(input("Enter a score need between 0 to 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("error,please enter score 0-100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")
def main_menu():
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def main():
    user_score = get_score()
    print("Valid score obtained:", user_score)

    while True:
          main_menu()
          select = input("please select a word:").upper()

          if  select == "G":
              user_score = get_score()
          elif select == "P":
              sandard = calculate_sandard(user_score)
              print("result:", sandard)
          elif select =="S":
              print("start")
              start(user_score)
          elif select =="Q":
              print("Thank you!")
          else:
              print("error select, please enter again.")

if __name__ == "__main__":
    main()












