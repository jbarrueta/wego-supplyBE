import classes.vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("testavailable", "588TST", "testmodel", "test2service", "1")

class TestInit(TestVehicle):
    def test_vehicleStatus(self):
        self.assertEqual(self.vehicle.vehicle_status, "testavailable")

    def test_license_plate(self):
        self.assertEqual(self.vehicle.license_plate, "588TST")

    def test_vehicle_model(self):
        self.assertEqual(self.vehicle.vehicle_model, "testmodel")

    def test_fleet_id(self):
        self.assertEqual(self.vehicle.fleet_id, "test2service")

class TestVehicle(TestVehicle):
    def test_getVehicleStatus(self):
        self.assertEqual(self.vehicle.getVehicleStatus, "testavailable")

    def test_getLicensePlate(self):
        self.assertEqual(self.vehicle.getLisensePlate, "588TST")

    def test_getVehicleModel(self):
        self.assertEqual(self.vehicle.getVehicleModel, "testmodel")

class TestIdService(TestVehicle):
    def test_getID(self):
        self.assertEqual(self.vehicle.getID, "1")

    def test_getServiceType(self):
        self.assertEqual(self.vehicle.getServiceType, "test2service")
    
    def test_getFleetID(self):
        self.assertEqual(self.vehicle.getFleetID, "1")

class TestGetRegisterData(self):
    def test_get_register_data(self):
        registerData = {"vehicleModel": "testmodel",
                        "licensePlate": "588TST",
                        "vehicleStatus": "testavailable"}
        self.assertEqual(self.vehicle.get_register_data(), registerData)

if __name__ == '__main__':
    unittest.main()