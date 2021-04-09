from bson.objectid import ObjectId
from pymongo.errors import PyMongoError
from classes.fleet import Fleet
import logging
from pymongo import client_options
from mongo.mongoConfig import mongoConnect


def registerFleet(postBody):
    response = {}
    try:
        fleetClass = Fleet(postBody["service_type"])
        client = mongoConnect()
        db = client.team12_supply
        fleet = db.fleet
        fleetObj = fleetClass.__dict__
        service_type = fleetObj["service_type"]
        if(fleet.count_documents({"service_type": service_type}) == 0):
            fleetId = fleet.insert_one(
                {"service_type": service_type}).inserted_id
            fleetClass.setId(fleetId)
            response = {"status": "OK", "data": {
                "service_type": fleetObj["service_type"], "fleetId": fleetId}}
        else:
            response = {"status": "CONFLICT", "data": {
                "msg": f"Fleet for {service_type} already exists"}}
    except Exception as err:
        response = {"status": "INTERNAL_SERVER_ERROR", "data": {
            "msg": "Server stopped working, please try again later"}}
    return response


def validFleet(_id):
    client = mongoConnect()
    fleet = client.team12_supply.fleet
    return fleet.count_documents({"_id": _id}) != 0


def getFleetId(service_type):
    client = mongoConnect()
    fleet = client.team12_supply.fleet
    doc = fleet.find_one({"service_type": service_type})
    if doc != None:
        fleetId = doc['_id']
        return fleetId
    else:
        raise PyMongoError(
            f"Fleet with service type, {service_type}, does not exist")
