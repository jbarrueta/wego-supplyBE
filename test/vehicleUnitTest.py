import sys
sys.path.append("..")
from classes.vehicle import Vehicle
from bson.objectid import ObjectId
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("testmodel", "588TST", "available", ObjectId("6070a81d27d869d2d83ffeca"))

class TestInit(TestVehicle):
    def test_vehicleStatus(self):
        self.assertEqual(self.vehicle.vehicle_status, "available")

    def test_license_plate(self):
        self.assertEqual(self.vehicle.license_plate, "588TST")

    def test_vehicle_model(self):
        self.assertEqual(self.vehicle.vehicle_model, "testmodel")
        #self.assertRaises(ValueError, self.vehicle.vehicle_model, " ")

    def test_fleet_id(self):
        self.assertEqual(self.vehicle.fleet_id, ObjectId("6070a81d27d869d2d83ffeca"))


class TestVehicleStatus(TestVehicle):
    def test_setVehicleStatus(self):
        self.vehicle.setVehicleStatus("available")
        self.assertEqual(self.vehicle.vehicle_status, "available")
        self.vehicle.setVehicleStatus("busy")
        self.assertEqual(self.vehicle.vehicle_status, "busy")
        self.vehicle.setVehicleStatus("inactive")
        self.assertEqual(self.vehicle.vehicle_status, "inactive")
        self.vehicle.setVehicleStatus("maintenance")
        self.assertEqual(self.vehicle.vehicle_status, "maintenance")
        self.assertRaises(ValueError, self.vehicle.setVehicleStatus, "")
        self.assertRaises(ValueError, self.vehicle.setVehicleStatus, "Ready")
        self.assertRaises(ValueError, self.vehicle.setVehicleStatus, "123")       

    def test_getVehicleStatus(self):
        self.assertEqual(self.vehicle.getVehicleStatus(), "available")
        self.vehicle.setVehicleStatus("busy")
        self.assertEqual(self.vehicle.getVehicleStatus(), "busy")
        self.vehicle.setVehicleStatus("inactive")
        self.assertEqual(self.vehicle.getVehicleStatus(), "inactive")
        self.vehicle.setVehicleStatus("maintenance")
        self.assertEqual(self.vehicle.getVehicleStatus(), "maintenance")

class TestVehicleLicensePlate(TestVehicle):
    def test_setLicensePlate(self):
        self.vehicle.setLicensePlate("588TST")
        self.assertEqual(self.vehicle.license_plate, "588TST")
        self.vehicle.setLicensePlate("TESTS")
        self.assertEqual(self.vehicle.license_plate, "TESTS")
        self.assertRaises(ValueError, self.vehicle.setLicensePlate, "")
        self.assertRaises(ValueError, self.vehicle.setLicensePlate, "test")
        self.assertRaises(ValueError, self.vehicle.setLicensePlate, "test12")
        self.assertRaises(ValueError, self.vehicle.setLicensePlate, "TEsT")

    def test_getLicensePlate(self):
        self.assertEqual(self.vehicle.getLicensePlate(), "588TST")

class TestVehicleModel(TestVehicle):
    def test_setVehicleModel(self):
        self.vehicle.setVehicleModel("testmodel")
        self.assertEqual(self.vehicle.vehicle_model, "testmodel")
        self.assertRaises(ValueError, self.vehicle.setVehicleModel, "")
        self.assertRaises(ValueError, self.vehicle.setVehicleModel, "model20")
        self.assertRaises(ValueError, self.vehicle.setVehicleModel, "123")

    def test_getVehicleModel(self):
        self.assertEqual(self.vehicle.getVehicleModel(), "testmodel")

class TestIdService(TestVehicle):
    # def test_getID(self):
    #     self.assertEqual(self.vehicle.getID(), "7070a81d27d869d2d83ffecb")

    def test_setFleetId(self):
        self.vehicle.setFleetId(ObjectId("6070a81d27d869d2d83ffeca"))
        self.assertEqual(self.vehicle.fleet_id, ObjectId("6070a81d27d869d2d83ffeca"))
        self.assertRaises(ValueError, self.vehicle.setFleetId, " ")
        self.assertRaises(ValueError, self.vehicle.setFleetId, "1")
        self.assertRaises(ValueError, self.vehicle.setFleetId, "testFleetId")
    
    def test_getFleetID(self):
        self.assertEqual(self.vehicle.getFleetID(), ObjectId("6070a81d27d869d2d83ffeca"))

class TestCoordinates(TestVehicle):
    def test_setCurrentLocation(self):
        self.vehicle.setCurrentLocation([-97.758911, 30.231760])
        self.assertEqual(self.vehicle.current_location, [-97.758911, 30.231760])
        self.assertRaises(ValueError, self.vehicle.setCurrentLocation, [])
        self.assertRaises(ValueError, self.vehicle.setCurrentLocation, "")
        self.assertRaises(ValueError, self.vehicle.setCurrentLocation, [-97.758911,])
        self.assertRaises(ValueError, self.vehicle.setCurrentLocation, [30.231760])

class TestGetRegisterData(TestVehicle):
    def test_get_register_data(self):
        registerData = {"vehicle_model": "testmodel",
                        "license_plate": "588TST",
                        "vehicle_status": "available",
                        "fleet_id": ObjectId("6070a81d27d869d2d83ffeca"),
                        'current_location': [-97.758911, 30.23176]}
        self.assertEqual(self.vehicle.get_register_data(), registerData)

if __name__ == '__main__':
    unittest.main()  