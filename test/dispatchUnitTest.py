import sys
sys.path.append("..")
from classes.dispatch import Dispatch
import unittest

class TestDispatch(unittest.TestCase):
    def setUp(self):
        self.dispatch= Dispatch("test2service", "7070a81d27d869d2d83ffecb", "[-97.758911, 30.231760]", "8070a81d27d869d2d83ffecc", 
                                "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]", "6070a81d27d869d2d83ffeca")

# This class tests all the init 
class TestInit(TestDispatch):
    def test_fleet_id(self):
        self.assertEqual(self.dispatch.fleet_id, "6070a81d27d869d2d83ffeca")
    
    def test_order_id(self):
        self.assertEqual(self.dispatch.order_id, "7070a81d27d869d2d83ffecb")
        
    def test_order_coords(self):
        self.assertEqual(self.dispatch.order_coords, "[-97.758911, 30.231760]")
    
    def test_vehicle_id(self):
        self.assertEqual(self.dispatch.vehicle_id, "8070a81d27d869d2d83ffecc")
    
    def test_route(self):
        self.assertEqual(self.dispatch.route, "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]")

# Tests the functions that are related to vehicle 
class TestVehicle(TestDispatch):
    def test_assignVehicle(self):
        self.assertEqual(self.dispatch.vehicle_id, "8070a81d27d869d2d83ffecc")
        self.assertRaises(ValueError, self.dispatch.assignVehicle, " ")
        self.assertRaises(ValueError, self.dispatch.assignVehicle, "test124")

    def test_getAssignedVehicle(self):
        self.assertEqual(self.dispatch.getAssignedVehicle(), "8070a81d27d869d2d83ffecc")

# Tests the functions that are related to route
class TestRoute(TestDispatch):
    def test_setRoute(self):
        self.dispatch.setRoute("[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374]]")
        self.assertEqual(self.dispatch.route, "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374]]")

    def test_getCurrentRoute(self):
        self.assertEqual(self.dispatch.route, "[[-97.758917, 30.231775], [-97.758166, 30.232976], [-97.757988,30.232891], [-97.757622, 30.232621], [-97.757501, 30.232374], [-97.757427, 30.23205]]")

# Tests the functions that are related to order
class TestOrder(TestDispatch):
    def test_setOrderId(self):
        self.dispatch.setOrderId("9070a81d27d869d2d83ffecd")
        self.assertEqual(self.dispatch.order_id, "9070a81d27d869d2d83ffecd")
        self.assertRaises(ValueError, self.dispatch.setOrderId, " ")
        self.assertRaises(ValueError, self.dispatch.setFleetId, "2")
        self.assertRaises(ValueError, self.dispatch.setFleetId, "testOrderId")


    def test_setOrderCoords(self):
        self.dispatch.setOrderCoords("[-97.758911, 30.231760]")
        self.assertEqual(self.dispatch.order_coords, "[-97.758911, 30.231760]")
        self.assertRaises(ValueError, self.dispatch.setOrderCoords, "[]")
        self.assertRaises(ValueError, self.dispatch.setOrderCoords, "testCoords")
        self.assertRaises(ValueError, self.dispatch.setOrderCoords, "")

    def test_getOrderCoordinates(self):
        self.assertEqual(self.dispatch.order_coords, "[-97.758911, 30.231760]")

# Tests the functions that are related to fleet
class TestFleetId(TestDispatch):
    def test_setFleetId(self):
        self.dispatch.setFleetId("6070a81d27d869d2d83ffeca")
        self.assertEqual(self.dispatch.fleet_id, "6070a81d27d869d2d83ffeca")
        self.assertRaises(ValueError, self.dispatch.setFleetId, " ")
        self.assertRaises(ValueError, self.dispatch.setFleetId, "1")
        self.assertRaises(ValueError, self.dispatch.setFleetId, "testfleet")

    def test_getFleetId(self):
        self.assertEqual(self.dispatch.getFleetId(), "6070a81d27d869d2d83ffeca")
        #self.assertRaises(ValueError, self.dispatch.getFleetId(), " ")


if __name__ == '__main__':
    unittest.main()