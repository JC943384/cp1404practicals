def main():
    filename = "wimbledon.csv"
    data = read_file(filename)
    champions, countries = process_data(data)

    display_champions(champions)
    display_countries(countries)


def read_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            line = line.strip().split(",")
            data.append(line)
    return data


def process_data(data):
    champions = {}
    countries = set()
    for entry in data:
        team = entry[2]
        country = entry[1]
        if team in champions:
            champions[team] += 1
        else:
            champions[team] = 1
            countries.add(country)
    return champions, sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions: ")
    for team, wins in champions.items():
        print(f"{team}: {wins} ")


def display_countries(countries):
    countries_str = ",".join(countries)
    countries_number = list(set(countries))
    count = len(countries_number)
    print(f"These {count} countries have won Wimbledon: ")
    print(countries_str)


if __name__ == "__main__":
    main()
