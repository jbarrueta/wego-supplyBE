class Fleet: 
    def __int__(self, service_type, available_vehicles)
        self.service_type = service_type
        self.available_vehicles = available_vehicles
    
    # Need to use mapbox to find the closest vehicle to destination
    # hard coded vehicle right now
    def getClosestVehicle(destination):
        return self.available_vehicles[0]

    
    def sendVehicle(vehicleId, route):