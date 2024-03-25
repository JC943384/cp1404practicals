from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    try:
        while True:
            name = input("Nane: ")
            if name == " ":
                break
            year = int(input("Year: "))
            cost = float(input("Cost: $"))

            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar}  added.\n")

        print("\nThese are my guitars: ")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
