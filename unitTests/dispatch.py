from classes.dispatch import Dispatch
import unittest

class TestDispatch(unittest.TestCase):
    def setUp(self):
        self.dispatch= Dispatch("test@test.com", "Testf", "Testl", "testpass")
        #self.fleet = Fleet("The Fleet")

class TestInit(TestDispatch):
    def test_fleet_id(self):
        self.assertEqual(self.dispatch.fleet_id, "")
    
    def test_order_id(self):
        self.assertEqual(self.dispatch.order_id, "")
    
    def test_order_coords(self):
        self.assertEqual(self.dispatch.order_coords, "")
    
    def test_vehicle_id(self):
        self.assertEqual(self.dispatch.vehicle_id, "")
    
    def test_route(self):
        self.assertEqual(self.dispatch.route, "")




if __name__ == '__main__':
    unittest.main()