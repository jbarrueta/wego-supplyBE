from utils.mapboxUtils import getRoute
from bson.objectid import ObjectId
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

    # sets id if it is an instance
    def setId(self, _id):
        if not isinstance(_id, ObjectId):
            raise ValueError("_id must be type ObjectId")
        else:
            self._id = _id

    # This is sending the vehicle with the route for an order
    # Getting route from mapBox
 #   def sendVehicle(vehicleId, route):
