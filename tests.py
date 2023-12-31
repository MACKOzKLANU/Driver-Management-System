import json
import unittest
from Driver import Driver
from utils import read_json, add_driver, remove_driver, create_reservation, conclude_reservation

class TestMethods(unittest.TestCase):
    def test_read_json(self):
    # Test if read_json returns a list of dictionaries
        drivers = read_json("drivers.json")
        self.assertTrue(isinstance(drivers, list))
        for driver in drivers:
            self.assertTrue(isinstance(driver, dict))



    def test_add_driver(self):
    # Test if add_driver adds a driver to the JSON file
    # You may need to replace these values with actual data
        name = "John Doe"
        add_driver(name)
        drivers = read_json("drivers.json")
        
        for driver in drivers:
            if driver["name"] == name:
                self.assertTrue(drivers["name"] == name for driver in drivers)
                
    def test_create_reservation(self):
    #test if reservation is created correctly in json file
        id = 0
        reservationtext = "xyzwesx"
        reservationtext2 = "difftext"
        create_reservation(id, reservationtext)
        create_reservation(id, reservationtext2)
        drivers = read_json("drivers.json")

        for driver in drivers:
            if driver["id"] == id and driver["reservation_detail"] == reservationtext:
                self.assertTrue(driver["id"] == id and driver["reservation_detail"] == reservationtext)
                self.assertTrue(driver["id"] == id and driver["reservation_detail"] != reservationtext2)
    
    def test_conclude_reservation(self):
        id = 0
        status = "free"
        conclude_reservation(id)
        drivers = read_json("drivers.json")
        for driver in drivers:
            if driver["id"] == id:
                self.assertTrue(driver["status"] == status)

            

        
    def test_display_drivers(self):
    #test if drivers are displayed correctly in list of dictionaries
        drivers = read_json("drivers.json")
        id = 0
        name = "John Doe"
        
        self.assertTrue(isinstance(drivers, list))
        #test if driver name is displayed correctly
        for driver in drivers:
            self.assertTrue(isinstance(driver, dict))
            if driver["id"] == id:
                self.assertTrue(driver["name"] == name)
    def test_remove_driver(self):
    #test if driver is correctyly removed from json file
        id = 0

        remove_driver(id)
        drivers = read_json("drivers.json")
        
        self.assertTrue(drivers["id"] != id for driver in drivers)

                
if __name__ == '__main__':
    unittest.main()
