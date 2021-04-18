import sys
sys.path.append("..")
import classes.fleetManager
import unittest

class TestFleetManager(unittest.TestCase):
    def setUp(self):
        self.fleetManager = FleetManager("test@test.com", "Testf", "Testl", "testpass")

class TestInit(TestFleetManager):
    def test_email(self):
        self.assertEqual(self.fleetManager.email, "test@test.com")

    def test_first_name(self):
        self.assertEqual(self.fleetManager.first_name, "Testf")

    def test_last_name(self):
        self.assertEqual(self.fleetManager.last_name, "Testl")

    def test_password(self):
        self.assertEqual(self.fleetManager.password, "testpass")

class TestFirstLastName(TestFleetManager):
    # test get set first name
    def test_get_first_name(self):
        self.assertEqual(self.fleetManager.getFirstName(), "Testf")

    def test_set_first_name(self):
        self.fleetManager.setFirstName("newfirstName")
        self.assertEqual(self.fleetManager.getFirstName(), "newfirstName")

    # test get set last name
    def test_get_last_name(self):
        self.assertEqual(self.fleetManager.getLastName(), "Testl")

    def test_set_last_name(self):
        self.fleetManager.setLastName("newlastName")
        self.assertEqual(self.fleetManager.getLastName(), "newlastName")


class TestEmailPass(TestFleetManager):
    def test_get_email(self):
        self.assertEqual(self.fleetManager.getEmail(), "test@test.com")

    def test_set_email(self):
        self.fleetManager.setEmail("new@new.com")
        self.assertEqual(self.fleetManager.getEmail(), "new@new.com")

    def test_set_pass(self):
        self.fleetManager.setPassword("newpass")
        self.assertEqual(self.fleetManager.password, "newpass")


class TestGetRegisterLoginData(TestCustomer):
    def test_get_register_data(self):
        registerData = {'email': "test@test.com", 'first_name': "Testf",
                        "last_name": "Testl", "password": "testpass"}
        self.assertEqual(self.fleetManager.get_register_data(), registerData)

    def test_get_login_data(self):
        self.assertEqual(self.fleetManager.get_login_data(),
                         ("test@test.com", "testpass"))


if __name__ == '__main__':
    unittest.main()
