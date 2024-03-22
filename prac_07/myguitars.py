from guitar import Guitar


def main():
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            name, year, cost = parts
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
        guitars.sort()

        print("sorted guitars by year: ")
        for guitar in guitars:
            print(guitar)

    while True:
        try:

            name = input("Enter the information to add guitar or Enter to exit the save file \nname: ")
            if not name:
                break

            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar} added.\n")

        except ValueError:
            print("Invalid input, please enter the correct information ")
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")
    print("Guitars saved to guitars.csv")


if __name__ == "__main__":
    main()
