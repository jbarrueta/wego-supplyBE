from controllers.fleet import getFleetId
from utils.mapboxUtils import getRoute
import re


class Dispatch:
    def __init__(self, service_type, order_id, order_coords, vehicle_id=None, route=None, fleet_id=None):
        if fleet_id == None:
            fleet_id = getFleetId(service_type)
        if not re.match("^[0-9a-fA-F]{24}$", fleet_id):
            raise ValueError("fleet_id must be type ObjectId")
        else:
            self.fleet_id = fleet_id
        if not re.match("^[0-9a-fA-F]{24}$", order_id):
            raise ValueError("order_id must be type ObjectId")
        else:
            self.order_id = order_id
        self.order_coords = order_coords
        if vehicle_id != None:
            self.vehicle_id = vehicle_id
        if route != None:
            self.route = route

    def assignVehicle(self, vehicle_id):
        if not re.match("/^[0-9a-fA-F]{24}$/", vehicle_id):
            raise ValueError("vehicle_id must be type ObjectId")
        else:
            self.vehicle_id = vehicle_id

    def setOrderCoords(self, order_coords):
        if not re.match("[-?[0-9]+\.[0-9]+,\s-?[0-9]+\.[0-9]+]$", order_coords):
            raise ValueError("order_coords is not in the correct format")
        else:
            self.order_coords = order_coords

    def setRoute(self, orderRoute):
        self.route = orderRoute 

    def getCurrentRoute(self):
        return self.route

    def getOrderCoordinates(self):
        return self.order_coords

    def getAssignedVehicle(self):
        return self.vehicle_id

    def getFleetId(self):
        return self.fleet_id
