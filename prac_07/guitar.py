class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
def main():
    guitars = []
    with open("guitars.csv","r") as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    print("All guitars: ")
    for guitar in guitars:
        print(guitar)
if __name__ == "__main__":
    main()