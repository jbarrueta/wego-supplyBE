from utils.mapboxUtils import getRoute
import re

# For this class fleet will have service_type, the fleet name, and its id 
class Fleet:
    def __init__(self, service_type, fleet_name, _id=None):
        self.service_type = service_type
        self.fleet_name = fleet_name
        self._id = _id

    # # Need to use mapbox to find the closest vehicle to destination
    # # hard coded vehicle right now
    # def getClosestVehicle(self, destination):
    #     #logic to find closest vehicle will be here
    #     closestVehicle = self.available_vehicles[0]
    #     return closestVehicle

    def setId(self, _id):
        if not re.match("^[0-9a-fA-F]{24}$", _id):
            raise ValueError("_id must be type ObjectId")
        else:
            self._id = _id

    # This is sending the vehicle with the route for an order
    # Getting route from mapBox
    # TODO change vehicleId status to busy and when done back to available
 #   def sendVehicle(vehicleId, route):
