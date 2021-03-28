from config.mongoConnect import mongoConnect
import bcrypt

def registerVehicle(addedVehicleData):
    response = {}
    try:
        # 2. Open a new database connection
        client = mongoConnect()
        # 3. write data from the database
        db = client.team12_supply #check
        vehicle = db.vehicle
        if (vehicle.count_documents({'fleetID': addedVehicleData['fleetID']}) == 0):
            vehicleObj = addedVehicleData
           # vehicleObj['password'] = hashPassword(fleetManagerData['password'])
            vehicleAddID = Vehicle.insert_one(vehicleObj).inserted_id
            response = {'status': 'OK', 'data': {'fleetID': vehicleObj['fleetID'], 'vehicleModel': fleetManagerObj['vehicle_model'], 'licensePlate': fleetManagerObj['license_plate'], "id": vehicleAddID}}
        else:
            response = {'status': 'CONFLICT', 'data': {'msg': 'already registered'}}
        # TODO: create session now
    except Exception as err:
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {'msg': 'Server stopped working, please try again later'}}
    return response