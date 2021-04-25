from controllers.fleet import getFleetId
from utils.mapboxUtils import getRoute
import re


class Dispatch:
    def __init__(self, service_type, order_id, order_coords, vehicle_id=None, route=None, fleet_id=None):
        if fleet_id == None:
            fleet_id = getFleetId(service_type)
        self.fleet_id = fleet_id
        # if order_id > 0:
        #     raise ValueError("order_id must be greater than 0")
        # else:
        self.order_id = order_id
        # if order_coords.len() != 2:
        #     raise ValueError("order_coords is not the correct length")
        # else:
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
