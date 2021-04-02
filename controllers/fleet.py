import logging
from mongo.mongoConfig import mongoConnect

def getAvailableVehicles(service_type):
    response = {}
    try:
        client = mongoConnect()
        db = client.team12_supply
        vehicle = db.vehicle

        availableVehicles = vehicle.find({'status': 'available'}).limit(7)
        logging.debug(availableVehicles)
        if len(availableVehicles) == 0:
            response = {'status': "CONFLICT", 'data' : {'msg': 'There are no available vehicles for this service at this time'}}

        else:
            response = {'status': "OK", 'data': availableVehicles}

    except Exception as err:
        logging.error(err)
        response = {'status': "INTERNAL_SERVER_ERROR", 'data' : {'msg': 'Server stopped working, the service type may be unavailable'}}
    
    return response