from mongo.mongoConfig import mongoConnect
import logging


def registerVehicle(vehicleObj):
    response = {}
    try:
        # 2. Open a new database connection
        client = mongoConnect()
        # 3. write data from the database
        db = client.team12_supply #check
        vehicle = db.vehicle
        if (vehicle.count_documents({'id': vehicleObj['id']}) == 0):
            vehicleID = vehicle.insert_one(vehicleObj).inserted_id
            response = {'status': 'OK', 'data': {'fleet_id': vehicleObj['fleet_id'], 'vehicle_model': vehicleObj['vehicle_model'], 'license_plate': vehicleObj['license_plate'], 'vehicle_status': vehicleObj['vehicle_status'], 'service_type':vehicleObj['service_type'], 'id': vehicleID}}
        else:
            response = {'status': 'CONFLICT', 'data': {'msg': 'already registered'}}
        # TODO: create session now
    except Exception as err:
        logging.error(err)
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {'msg': 'Server stopped working, please try again later'}}
    return response