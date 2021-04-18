import sys
sys.path.append("..")
from classes.dispatch import Dispatch
import unittest

class TestDispatch(unittest.TestCase):
    def setUp(self):
        self.dispatch= Dispatch("test2service", "1", "[-97.758911, 30.231760]", "2", 
                                "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]")

class TestInit(TestDispatch):
    def test_fleet_id(self):
        self.assertEqual(self.dispatch.fleet_id, "test2service")
    
    def test_order_id(self):
        self.assertEqual(self.dispatch.order_id, "1")
    
    def test_order_coords(self):
        self.assertEqual(self.dispatch.order_coords, "[-97.758911, 30.231760]")
    
    def test_vehicle_id(self):
        self.assertEqual(self.dispatch.vehicle_id, "2")
    
    def test_route(self):
        self.assertEqual(self.dispatch.route, "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]")

class TestVehicle(TestDispatch):
    def test_assignVehicle(self):
        self.assertEqual(self.dispatch.vehicle_id, "2")

    def test_getAssignedVehicle(self):
        self.assertEqual(self.dispatch.getAssignedVehicle, "2")

class TestRoute(TestDispatch):
    def test_setRoute(self):
        self.assertEqual(self.dispatch.route, "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]")

    def test_getCurrentRoute(self):
        self.assertEqual(self.dispatch.route, "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]")

class TestCoordinates(TestDispatch):
    def test_getOrderCoordinates(self):
        self.assertEqual(self.dispatch.order_coords, "[-97.758911, 30.231760]")

class TestFleetId(TestDispatch):
    def test_getFleetId(self):
        self.assertEqual(self.dispatch.getFleetId, "test2service")


if __name__ == '__main__':
    unittest.main()