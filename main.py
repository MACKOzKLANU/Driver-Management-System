from utils import read_json, display_drivers, add_driver, remove_driver, create_reservation, conclude_reservation

def main_menu():
    while True:
        print("Menu:")
        print("1. Display Drivers")
        print("2. Add Driver")
        print("3. Remove Driver")
        print("4. Create Reservation")
        print("5. Conclude Reservation")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_drivers("drivers.json")
        elif choice == "2":
            name = input("Enter the driver's name: ")
            add_driver(name)
        elif choice == "3":
            try:
                id = int(input("Enter the driver's ID to remove: "))
                remove_driver(id)
            except ValueError:
                # If it cannot be converted to an integer, it's a string
                print("Input is a string., it must be a number")
        elif choice == "4":
            try:
                id = int(input("Enter the driver's ID for the reservation: "))
                reservation_detail = input("Enter the reservation details: ")
                create_reservation(id, reservation_detail)
            except ValueError:
                # If it cannot be converted to an integer, it's a string
                print("Input is a string., it must be a number")
        elif choice == "5":
            try:
                id = int(input("Enter the driver's ID to conclude the reservation: "))
                conclude_reservation(id)
            except ValueError:
                # If it cannot be converted to an integer, it's a string
                print("Input is a string., it must be a number")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main_menu()
