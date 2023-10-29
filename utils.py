import json
from Driver import Driver
from datetime import datetime
import time

def read_json(filename):
    try:
        # Attempt to read JSON data from the given file
        with open(filename, "r") as file:
            drivers = json.load(file)
        return drivers
    except FileNotFoundError:
        # Handle the case when the file is not found
        raise FileNotFoundError(f"File not found: {filename}")
    except json.JSONDecodeError:
        # Handle the case when the JSON data in the file is invalid
        raise json.JSONDecodeError(f"Invalid JSON in the file: {filename}")


def display_drivers(filename):
    # Read and display the list of drivers from the JSON file
    drivers = read_json(filename)

    print("Drivers:\n")
    for driver in drivers:
        print("ID:", driver["id"])
        print("Name:", driver["name"])
        print("Status:", driver["status"])
        print("Reservation Detail:", driver["reservation_detail"])
        print("Time spent on last reservation:", driver["time_spent_on_reservation"])


def add_driver(name):
    # Add a new driver to the JSON file with the given name
    drivers = read_json("drivers.json")
    current_id = 0
    for driver in drivers:
        if int(current_id) == driver["id"]:
            current_id += 1
    new_driver = Driver(current_id, name)
    drivers.append(new_driver.to_dict())
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)


def remove_driver(id):
    # Remove a driver with the specified ID from the JSON file

    drivers = read_json("drivers.json")

    for driver in drivers:
        if driver.get("id") == id:
            drivers.remove(driver)
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)

def create_reservation(id, reservation_detail):
    # Create a reservation for a driver with the specified ID

    drivers = read_json("drivers.json")

    for driver in drivers:
        if driver.get("id") == id:
            if driver["status"] == "free":
                driver["reservation_detail"] = reservation_detail
                driver["status"] = "busy"
                start_time = datetime.now()
                formatted_date = start_time.strftime("%Y-%m-%d %H:%M:%S")

                driver["reservation_start_time"] = formatted_date
            else:
                print("This driver is busy")
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)


def conclude_reservation(id):
    # Conclude a reservation for a driver with the specified ID

    drivers = read_json("drivers.json")
    for driver in drivers:
        if driver.get("id") == id:
            if driver["status"] == "busy":
                driver["reservation_detail"] = None
                driver["status"] = "free"
                end_time = datetime.now()
                formatted_date = end_time.strftime("%Y-%m-%d %H:%M:%S")
                date_format = "%Y-%m-%d %H:%M:%S"
                driver["reservation_end_time"] = formatted_date
                parsed_datetime = datetime.strptime(driver["reservation_start_time"], date_format)
                time_spent_on_reservation = end_time- parsed_datetime
                driver["time_spent_on_reservation"] = str(time_spent_on_reservation)
            else:
                print("Driver is already free")
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)
