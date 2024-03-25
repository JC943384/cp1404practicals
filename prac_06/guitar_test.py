from guitar import Guitar


def test_guitar_methods():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000.00)

    expected_age_gibson = 100
    expected_age_another = 9
    print(f"{gibson.name} get_age() - Expected {expected_age_gibson}. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {expected_age_another}. Got {another_guitar.get_age()}")

    expected_vintage_gibson = True
    expected_vintage_another = False
    print(f"{gibson.name} is_vintage() - Expected {expected_vintage_gibson}. Got {gibson.is_vintage()}")
    print(f"{gibson.name} is_vintage() - Expected {expected_vintage_another}. Got {another_guitar.is_vintage()}")


if __name__ == "__main__":
    test_guitar_methods()