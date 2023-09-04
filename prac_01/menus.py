MENU = """          
      (H)ello
      (G)oodbye
      (Q)uit
               """
name = input("Please enter name  ")
print(MENU)

choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("hello " + str(name) + MENU)
        choice = input(">>>").upper()

    elif choice == "G":
        print("Goodbye " + str(name) + MENU)
        choice = input(">>>").upper()
    else:
        print(MENU)
        print("Invalid choice")

        choice = input(">>> ").upper()
        print("Finished")
