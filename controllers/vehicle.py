from bson.objectid import ObjectId
from pymongo.errors import PyMongoError
from classes.vehicle import Vehicle
from mongo.mongoConfig import mongoConnect
import logging


def registerVehicle(path, postBody):
    response = {}
    try:
        fleetId = path.split("/")[1]
        vehicleClass = Vehicle(postBody['vehicleModel'],
                               postBody['licensePlate'],
                               postBody['vehicleStatus'],
                               ObjectId(fleetId)
                               )
        vehicleObj = vehicleClass.get_register_data()
        print("here")
        print(vehicleObj)
        # 2. Open a new database connection
        client = mongoConnect()
        # 3. write data from the database
        db = client.team12_supply  # check
        vehicle = db.vehicle
        if (vehicle.count_documents({'license_plate': vehicleObj['license_plate']}) == 0):
            vehicleID = vehicle.insert_one(vehicleObj).inserted_id
            response = {'status': 'OK', 'data': {'fleet_id': vehicleObj['fleet_id'], 'vehicle_model': vehicleObj['vehicle_model'], 'license_plate': vehicleObj[
                'license_plate'], 'vehicle_status': vehicleObj['vehicle_status'], 'id': vehicleID}}
        else:
            response = {'status': 'CONFLICT',
                        'data': {'msg': 'Vehicle already registered'}}
    except PyMongoError as err:
        response = {'status': 'CONFLICT', 'data': {
            'msg': err}}
    except Exception as err:
        logging.error(err)
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {
            'msg': 'Server stopped working, please try again later'}}
    return response


def getAvailableVehicles(fleetId):
    print(fleetId)
    client = mongoConnect()
    db = client.team12_supply
    vehicle = db.vehicle

    docs = vehicle.find(
        {'vehicle_status': 'available', 'fleet_id': ObjectId(fleetId)})
    availableVehicles = []
    for doc in docs:
        availableVehicles.append(doc)
    print("This is the list of vehicles")
    logging.debug(availableVehicles)
    return availableVehicles


def getClosestVehicle(vehicles, coords):
    # insert logic here
    return vehicles[0]
