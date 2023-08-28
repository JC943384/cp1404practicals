from guitar import Guitar


def main():
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    guitars.sort()
    print("All guitars: ")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
