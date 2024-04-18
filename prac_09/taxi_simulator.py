from taxi import Taxi

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

def main():
    taxis = [
        Taxi("Prius", 100, 1.23),
        Taxi("Limo", 100, 2.46, 4.50),
        Taxi("Hummer", 200, 4.92, 4.50)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("Bill to date: ${:.2f}".format(total_bill))
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print("Total trip cost: ${:.2f}".format(total_bill))
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                current_taxi.start_fare()
                print("Bill to date: ${:.2f}".format(total_bill))
            else:
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                distance_driven = current_taxi.drive(distance)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                total_bill += current_taxi.get_fare()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()



