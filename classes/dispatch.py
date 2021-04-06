from utils.mapboxUtils import getRoute

class Dispatch: 
    def __init__(self, service_type, order_id, order_coords, vehicle_id=None, route=None):
        self.service_type = service_type
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