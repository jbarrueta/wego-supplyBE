import sys
sys.path.append("..")
from classes.fleet import Fleet
from bson.objectid import ObjectId
import unittest

class TestFleet(unittest.TestCase):
    def setUp(self):
        self.fleet = Fleet("test2service", "testfleet")

class TestInit(TestFleet):
    def test_init(self):
        self.assertEqual(self.fleet.service_type, "test2service")
        self.assertEqual(self.fleet._id, None)

# test for the method setId
class TestSetId(TestFleet):
    def test_setId(self):
        self.fleet.setId(ObjectId("6070a81d27d869d2d83ffeca"))
        self.assertEqual(self.fleet._id, ObjectId("6070a81d27d869d2d83ffeca"))
        self.assertRaises(ValueError, self.fleet.setId, " ")
        self.assertRaises(ValueError, self.fleet.setId, "1")
        self.assertRaises(ValueError, self.fleet.setId, "testId")

if __name__ == '__main__':
    unittest.main()