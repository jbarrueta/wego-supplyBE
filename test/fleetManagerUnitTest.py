import sys
sys.path.append("..")
from classes.fleetManager import FleetManager
import unittest

class TestFleetManager(unittest.TestCase):
    def setUp(self):
        self.fleetManager = FleetManager("test@test.com", "Testf", "Testl", "Testpass123!")

class TestInit(TestFleetManager):
    def test_email(self):
        self.assertEqual(self.fleetManager.email, "test@test.com")

    def test_first_name(self):
        self.assertEqual(self.fleetManager.first_name, "Testf")

    def test_last_name(self):
        self.assertEqual(self.fleetManager.last_name, "Testl")

    def test_password(self):
        self.assertEqual(self.fleetManager.password, "Testpass123!")

class TestFirstLastName(TestFleetManager):
    # test get set first name
    def test_get_first_name(self):
        self.assertEqual(self.fleetManager.getFirstName(), "Testf")

    def test_set_first_name(self):
        self.fleetManager.setFirstName("newfirstName")
        self.assertEqual(self.fleetManager.getFirstName(), "newfirstName")
        self.assertRaises(ValueError, self.fleetManager.setFirstName, "incorrectFirstName1")
        self.assertRaises(ValueError, self.fleetManager.setFirstName, "")

    # test get set last name
    def test_get_last_name(self):
        self.assertEqual(self.fleetManager.getLastName(), "Testl")

    def test_set_last_name(self):
        self.fleetManager.setLastName("newlastName")
        self.assertEqual(self.fleetManager.getLastName(), "newlastName")
        self.assertRaises(ValueError, self.fleetManager.setLastName, "incorrectLastName2")
        self.assertRaises(ValueError, self.fleetManager.setLastName, " ")


class TestEmailPass(TestFleetManager):
    def test_get_email(self):
        self.assertEqual(self.fleetManager.getEmail(), "test@test.com")

    def test_set_email(self):
        self.fleetManager.setEmail("new@new.com")
        self.assertEqual(self.fleetManager.getEmail(), "new@new.com")
        self.assertRaises(ValueError, self.fleetManager.setEmail, "incorrectEmail.com")
        self.assertRaises(ValueError, self.fleetManager.setEmail, " ")

    def test_set_pass(self):
        self.fleetManager.setPassword("Newpass123!")
        self.assertEqual(self.fleetManager.password, "Newpass123!")
        self.assertRaises(ValueError, self.fleetManager.setPassword, "incorrectpassword")
        self.assertRaises(ValueError, self.fleetManager.setPassword, "1245")
        self.assertRaises(ValueError, self.fleetManager.setPassword, "")


class TestGetRegisterLoginData(TestFleetManager):
    def test_get_register_data(self):
        registerData = {'email': "test@test.com", 'first_name': "Testf",
                        "last_name": "Testl", "password": "Testpass123!"}
        self.assertEqual(self.fleetManager.get_register_data(), registerData)

    def test_get_login_data(self):
        self.assertEqual(self.fleetManager.get_login_data(),
                         ("test@test.com", "Testpass123!"))


if __name__ == '__main__':
    unittest.main()
