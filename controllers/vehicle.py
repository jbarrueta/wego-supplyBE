from bson.objectid import ObjectId
from pymongo.errors import PyMongoError
from classes.vehicle import Vehicle
from mongo.mongoConfig import mongoConnect
import logging
from controllers.fleet import validFleet


def registerVehicle(path, postBody):
    response = {}
    try:
        fleet_id = path.split("/")[1]
        if not(validFleet(fleet_id)):
            raise PyMongoError(f"Fleet with ID: {fleet_id} does not exist")
        vehicleClass = Vehicle(postBody['vehicle_model'],
                               postBody['license_plate'],
                               postBody['vehicle_status'],
                               ObjectId(fleet_id)
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
                'license_plate'], 'vehicle_status': vehicleObj['vehicle_status'], '_id': vehicleID, "current_location": vehicleObj["current_location"]}}
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


def getVehicleList(paramsDict):
    try:
        vehicleList = getVehicles(paramsDict)
        response = {"status": "OK", "data": {
            "vehicleList": vehicleList}}
    except Exception:
        response = {"status": "INTERNAL_SERVER_ERROR", "data": {
            "msg": "Server stopped working, please try again later"}}
    return response


def getVehicles(query):
    client = mongoConnect()
    db = client.team12_supply
    vehicle = db.vehicle
    print(query)
    docs = vehicle.find(query)
    vehicleList = []
    for doc in docs:
        vehicleList.append(doc)
    print("This is the list of vehicles")
    logging.debug(vehicleList)
    return vehicleList


def getClosestVehicle(vehicles, coords):
    # insert logic here
    return vehicles[0]
