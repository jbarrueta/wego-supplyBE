
# Vehicle class object
from controllers.fleet import validFleet
from pymongo.errors import PyMongoError


class Vehicle:
    def __init__(self, vehicle_model, license_plate, vehicle_status, fleet_id):
        self.vehicle_status = vehicle_status
        self.license_plate = license_plate
        self.vehicle_model = vehicle_model
        if(validFleet(fleet_id)):
            self.fleet_id = fleet_id
        else:
            raise PyMongoError(f"Fleet with ID: {fleet_id} does not exist")
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
