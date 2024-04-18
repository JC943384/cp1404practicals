from silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 4.0)
    distance = 0

    hummer.drive(distance)

    print(hummer)
    print("Current fare: ${:.2f}".format(hummer.get_fare()))

    hummer = SilverServiceTaxi("Hummer", 200, 2.0)
    distance = 18

    hummer.drive(distance)

    print(hummer)
    print("Current fare: ${:.2f}".format(hummer.get_fare()))


if __name__ == "__main__":
    main()
