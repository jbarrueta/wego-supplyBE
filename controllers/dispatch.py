from bson.objectid import ObjectId
from pymongo.errors import PyMongoError
from classes.dispatch import Dispatch
from mongo.mongoConfig import mongoConnect
import logging
from utils.mapboxUtils import getCoordinates, getETA, getRoute
from controllers.vehicle import getVehicles, getClosestVehicle, updateVehicleDoc
import datetime


def dispatchOrder(orderParams):
    # get address as coordinates, [long, lat]
    orderCoords = getCoordinates(orderParams['destination'])
    # create dispatch object with service type, order id and order coordinates
    orderDispatch = Dispatch(
        orderParams['service_type'], orderParams['order_id'], orderCoords)
    # use fleet controller to find a list of max 7 available vehicles of that service type
    availableVehicles = getVehicles(
        {"fleet_id": orderDispatch.getFleetId(), 'vehicle_status': 'available'})
    if(len(availableVehicles) != 0):
        vehicleAssigned = getClosestVehicle(
            availableVehicles, orderCoords)
        # set dispatch with closest vehicle`
        orderDispatch.assignVehicle(str(vehicleAssigned['_id']))
        updateVehicleDoc(vehicleAssigned['_id'], {"vehicle_status": "busy"})
        # get a route and set route in dispatch class
        orderDispatch.setRoute(getRoute(vehicleAssigned['current_location'][0], vehicleAssigned['current_location'][1],
                                        orderCoords[0], orderCoords[1]))
        eta = getETA(vehicleAssigned['current_location'][0], vehicleAssigned['current_location'][1],
                     orderCoords[0], orderCoords[1])
        now = datetime.datetime.now()
        eta = now + datetime.timedelta(minutes=eta)
        # Need to find a way to get ETA from route
        responseBody = {'status': 'OK', 'data': {
            'ETA': eta.strftime('%Y-%m-%dT%H:%M:%S'),
            'route': orderDispatch.getCurrentRoute(),
            'vehicle_id': orderDispatch.getAssignedVehicle()
        }}
    else:
        responseBody = {'status': 'CONFLICT', 'data': {
            'msg': 'No available vehicles at this time!'}}
    return responseBody
