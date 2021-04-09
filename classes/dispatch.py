from controllers.fleet import getFleetId
from utils.mapboxUtils import getRoute

class Dispatch: 
    def __init__(self, service_type, order_id, order_coords, vehicle_id=None, route=None):
        fleet_id = getFleetId(service_type)
        self.fleet_id = fleet_id
        self.order_id = order_id
        self.order_coords = order_coords
        self.vehicle_id = vehicle_id
        self.route = route

    def assignVehicle(self, vehicle_id):
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