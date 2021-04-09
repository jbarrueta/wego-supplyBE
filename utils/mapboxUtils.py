import requests
import json
from mapbox import Geocoder

api_key = "pk.eyJ1Ijoia2F5dGx5bmd1ZXJyZXJvIiwiYSI6ImNrbGd5ejMwMTB5cDQyd29paGZoYnE0dW4ifQ.FN8hXcvlYPaxkl0UdIatVQ"
# Receives an address, returns the coordinates
def getCoordinates(address):
    geocoder = Geocoder()
    geocoder = Geocoder(access_token="pk.eyJ1Ijoia2F5dGx5bmd1ZXJyZXJvIiwiYSI6ImNrbGd5ejMwMTB5cDQyd29paGZoYnE0dW4ifQ.FN8hXcvlYPaxkl0UdIatVQ")
    destination = geocoder.forward(address).json()['features'][0]["geometry"]["coordinates"]
    return destination

# Forward geocoding - receives a set of coordinates and returns an address
def getGeocoding(startLong, StartLat):
    geocodingRequest = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ str(startLong)+","+str(StartLat)+".json?access_token="+ api_key)
    mapData = geocodingRequest.json()
    address = json.dumps(mapData.get("features")[0].get('place_name'))
    return address

# Receives 2 sets of coordinates and returns the route (set of coordinates) from point A -> B
## Given coordinates are The Capital of Austin to St. Edwards University
## Should return the coordinates that run along the geoJSON line
def getRoute(startLong, StartLat, endLong, endLat):
    drivingRequest = requests.get("https://api.mapbox.com/directions/v5/mapbox/driving/" +str(startLong)+","+str(StartLat)+";"+str(endLong)+","+str(endLat)+ "?geometries=geojson&access_token=" + api_key)
    mapData = drivingRequest.json()
    responseCoordinates = json.dumps(mapData.get("routes")[0].get("geometry").get("coordinates"))
    return responseCoordinates

# Receives 2 sets of coordinates and returns the ETA from point A -> B 
def getETA(startLong, startLat, endLong, endLat):
    drivingRequest = requests.get("https://api.mapbox.com/directions/v5/mapbox/driving/" +str(startLong)+","+str(startLat)+";"+str(endLong)+","+str(endLat)+ "?geometries=geojson&access_token=" + api_key)
    mapData = drivingRequest.json()
    distance = float(json.dumps(mapData.get("routes")[0].get("distance")))
    # 1 mile = 1609.34 meters (distance is given in meters from mapbox)
    eta = ((distance/1609.34)/50)*60
    # Only grab 2 places after decimal
    return "ETA: "+ "%.2f" % eta + " minutes"
# print(getETA(-97.7431,30.2672,-97.7526,30.2289))

