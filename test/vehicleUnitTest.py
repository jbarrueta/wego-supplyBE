import sys
sys.path.append("..")
from classes.vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("testmodel", "588TST", "available", "6070a81d27d869d2d83ffeca")

class TestInit(TestVehicle):
    def test_vehicleStatus(self):
        self.assertEqual(self.vehicle.vehicle_status, "available")

    def test_license_plate(self):
        self.assertEqual(self.vehicle.license_plate, "588TST")

    def test_vehicle_model(self):
        self.assertEqual(self.vehicle.vehicle_model, "testmodel")

    def test_fleet_id(self):
        self.assertEqual(self.vehicle.fleet_id, "6070a81d27d869d2d83ffeca")

class TestVehicle(TestVehicle):
    def test_getVehicleStatus(self):
        self.assertEqual(self.vehicle.getVehicleStatus(), "available")

    def test_getLicensePlate(self):
        self.assertEqual(self.vehicle.getLisensePlate(), "588TST")

    def test_getVehicleModel(self):
        self.assertEqual(self.vehicle.getVehicleModel(), "testmodel")

class TestIdService(TestVehicle):
    def test_getID(self):
        self.assertEqual(self.vehicle.getID(), "1")
    
    def test_getFleetID(self):
        self.assertEqual(self.vehicle.getFleetID(), "6070a81d27d869d2d83ffeca")

class TestGetRegisterData(TestVehicle):
    def test_get_register_data(self):
        registerData = {"vehicle_model": "testmodel",
                        "license_plate": "588TST",
                        "vehicle_status": "available",
                        "fleet_id": "6070a81d27d869d2d83ffeca",
                        'current_location': [-97.758911, 30.23176]}
        self.assertEqual(self.vehicle.get_register_data(), registerData)

if __name__ == '__main__':
    unittest.main()  