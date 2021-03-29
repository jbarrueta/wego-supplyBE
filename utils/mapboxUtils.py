import requests
import json
def getRoute(startLong, StartLat, endLong, endLat):
    api_key = "pk.eyJ1Ijoia2F5dGx5bmd1ZXJyZXJvIiwiYSI6ImNrbGd5ejMwMTB5cDQyd29paGZoYnE0dW4ifQ.FN8hXcvlYPaxkl0UdIatVQ"
    drivingRequest = requests.get("https://api.mapbox.com/directions/v5/mapbox/driving/" +str(startLong)+","+str(StartLat)+";"+str(endLong)+","+str(endLat)+ "?geometries=geojson&access_token=" + api_key)
    mapData = drivingRequest.json()
    responseCoordinates = json.dumps(mapData.get("routes")[0].get("geometry").get("coordinates"))
    return responseCoordinates

## Given coordinates are The Capital of Austin to St. Edwards University
## Should return the coordinates that run along the geoJSON line
print(getRoute(-97.7431,30.2672,-97.7526,30.2289))

def getGeocoding(startLong, StartLat):
    api_key = "pk.eyJ1Ijoia2F5dGx5bmd1ZXJyZXJvIiwiYSI6ImNrbGd5ejMwMTB5cDQyd29paGZoYnE0dW4ifQ.FN8hXcvlYPaxkl0UdIatVQ"
    geocodingRequest = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ str(startLong)+","+str(StartLat)+".json?access_token="+ api_key)
    mapData = geocodingRequest.json()
    address = json.dumps(mapData.get("features")[0].get('place_name'))
    return address
## The coordinates passed is the address of St. Edwards University
print(getGeocoding(-97.7526,30.2289))

def getGeocoding(address):
    api_key = "pk.eyJ1Ijoia2F5dGx5bmd1ZXJyZXJvIiwiYSI6ImNrbGd5ejMwMTB5cDQyd29paGZoYnE0dW4ifQ.FN8hXcvlYPaxkl0UdIatVQ"
    geocodingRequest = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ str(address) +".json?access_token="+ api_key)
    mapData = geocodingRequest.json()
    address = json.dumps(mapData.get("features")[0].get('place_name'))
    return address

