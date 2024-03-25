class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"year:({self.year}) {self.name}: $ {self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        current_year = 2022
        return current_year -self.year

    def is_vintage(self):
        return self.get_age() >= 50