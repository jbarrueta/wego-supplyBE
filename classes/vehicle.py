# Vehicle class object
from controllers.fleet import validFleet
from pymongo.errors import PyMongoError
import re


class Vehicle:
    def __init__(self, vehicle_model, license_plate, vehicle_status, fleet_id):
        self.vehicle_status = vehicle_status.lower()
        if not re.match("^[a-zA-Z0-9]+$", license_plate):
            raise ValueError("license_plate is not correct")
        else:
            self.license_plate = license_plate
        if(re.match("^[a-zA-Z]+$", vehicle_model)):
            self.vehicle_model = vehicle_model
        else:
            raise ValueError("vehicle_model can only have letters")
        if not re.match("^[0-9a-fA-F]{24}$", fleet_id):
            raise ValueError("fleet_id must be type ObjectId")
        else:
            self.fleet_id = fleet_id
        # set all vehicle locations to st.edwards university right now
        self.current_location = [-97.758911, 30.231760]

    def getID(self):
        return self.id

    def getServiceType(self):
        return self.service_type

    def getVehicleStatus(self):
        return self.vehicle_status

    def getLicensePlate(self):
        return self.license_plate

    def getVehicleModel(self):
        return self.vehicle_model

    def getFleetID(self):
        return self.fleet_id

    def get_register_data(self):
        return self.__dict__
