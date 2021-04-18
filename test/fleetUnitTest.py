import sys
sys.path.append("..")
from classes.fleet import Fleet
import unittest

class TestFleet(unittest.TestCase):
    def setUp(self):
        self.fleet = Fleet("test2service", "1")

class TestInit(TestFleet):
    def test_init(self):
        self.assertEqual(self.fleet.service_type, "test2service")
        self.assertEqual(self.fleet._id, "1")

# test for the method setId
class TestSetId(TestFleet):
    def test_setId(self):
        self.assertEqual(self.fleet.setId(), "1")


if __name__ == '__main__':
    unittest.main()