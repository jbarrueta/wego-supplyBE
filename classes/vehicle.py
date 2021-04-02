
# Vehicle class object 
class Vehicle:
    def __init__(self, vehicle_model, license_plate, vehicle_status, id, service_type):
        self.vehicle_status = vehicle_status
        self.license_plate = license_plate
        self.vehicle_model = vehicle_model
        self.id = id
        self.service_type = service_type
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

