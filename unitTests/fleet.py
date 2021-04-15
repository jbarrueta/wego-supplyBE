from classes.fleet import Fleet
import unittest

class TestFleet(unittest.TestCase):
    def setUp(self):
        self.fleet = Fleet("test@test.com", "Testf", "Testl", "testpass")
        #self.fleet = Fleet("The Fleet")

class TestInit(TestFleet):
    def test_setId(self):
        self.assertEqual(self.fleet.service_type, "test@test.com")
        self.assertEqual(self.fleet._id, "test@test.com")

# test for the method setId
class TestSetId(TestFleet):
    def test_setId(self):
        self.assertEqual(self.fleet.setId(), "_id object")


if __name__ == '__main__':
    unittest.main()