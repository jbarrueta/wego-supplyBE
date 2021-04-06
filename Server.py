import logging
import json
from utils.mapboxUtils import getCoordinates, getRoute
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from urllib.parse import urlparse, parse_qsl
from classes.fleetManager import FleetManager
from classes.vehicle import Vehicle
from controllers.vehicle import registerVehicle
from controllers.fleetManager import registerUser, loginUser
from controllers.fleet import getAvailableVehicles 
from classes.dispatch import Dispatch
from classes.fleet import Fleet

# Class Logger we can use for debugging our Python service. You can add an additional parameter here for
# specifying a log file if you want to see a stream of log data in one file.
logging.basicConfig(level=logging.DEBUG)


class TaasAppService(BaseHTTPRequestHandler):

    # HTTP Response code dictionary constant we can reuse inside our responses back to the client. Typically this
    # would be in a configuration file where you store constants you repeatedly use throughout your services.
    HTTP_STATUS_RESPONSE_CODES = {
        'OK': HTTPStatus.OK,
        'FORBIDDEN': HTTPStatus.FORBIDDEN,
        'NOT_FOUND': HTTPStatus.NOT_FOUND,
        'CONFLICT': HTTPStatus.CONFLICT,
        'INTERNAL_SERVER_ERROR': HTTPStatus.INTERNAL_SERVER_ERROR
    }

    # Here's how you extract GET parameters from a URL entered by a client.
    def extract_GET_parameters(self):
        path = self.path
        parsedPath = urlparse(path)
        paramsDict = dict(parse_qsl(parsedPath.query))
        logging.info('GET parameters received: ' +
                     json.dumps(paramsDict, indent=4, sort_keys=True))
        return paramsDict

    def extract_POST_Body(self):
        # The content-length HTTP header is where our POST data will be in the request. So we'll need to
        # read the data using an IO input buffer stream built into the http.server module.
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        # loads string into dict
        postBodyDict = json.loads(postBodyString)
        # exclude logging sensitive info
        blacklist = ["password"]
        # json.dumps formats dict into string and then indent formats in a nice way
        logging.info('POST Body received: ' +
                     json.dumps({k: postBodyDict[k] for k in set(list(postBodyDict.keys())) - set(blacklist)}, indent=4, sort_keys=True))
        return postBodyDict

    # The do_GET(self) function is how we respond to GET requests from clients.
    def do_GET(self):
        # self.path here will return us the http request path entered by the client.
        path = self.path
        # Extract the GET parameters associated with this HTTP request and store them in a python dictionary
        paramsDict = self.extract_GET_parameters()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND'].value
        responseBody = {}

        # This is a root URI or block of code that will be executed when client requests the address:
        # http://localhost:8082.
        if path == '/':
            status = self.HTTP_STATUS_RESPONSE_CODES['OK'].value
            responseBody['data'] = 'Hello world'
        
        elif '/vehicles/req' in path:
            o = urlparse(path)
            # https://supply.team12.sweispring21.tk/api/vehicles/req?service_type="pet2vet"&order_id=1&customer_id="KG2342"&destination="3001 S. Congress"
            orderParams = self.extract_GET_parameters()
            print(orderParams)
            # get address as coordinates, [long, lat]
            orderCoords = getCoordinates(orderParams['destination'])
            # create dispatch object with service type, order id and order coordinates 
            orderDispatch = Dispatch(orderParams['service_type'], orderParams['order_id'], orderCoords)
            # use fleet controller to find a list of max 7 available vehicles of that service type
            avalVehicleObj = getAvailableVehicles('service_type')
            if avalVehicleObj['status'] != 'OK':
                responseBody = avalVehicleObj
            else:
                fleet = Fleet(orderParams["service_type"], avalVehicleObj['data'])
                vehicleAssigned = fleet.getClosestVehicle(orderCoords)
                # set dispatch with closest vehicle
                orderDispatch.assignVehicle(vehicleAssigned['id'])
                # get a route and set route in dispatch class
                orderDispatch.setRoute(
                    getRoute(vehicleAssigned['current_location'][0], vehicleAssigned['current_location'][1], 
                    orderCoords[0], orderCoords[1]))
                # Need to find a way to get ETA from route
                responseBody = {'status': 'OK', 'data':{
                            'ETA':'10', 
                            'route': orderDispatch.getCurrentRoute(),
                            'vehicle_id': orderDispatch.getAssignedVehicle()
                            }}

            status = self.HTTP_STATUS_RESPONSE_CODES[responseBody["status"]].value
                        


        # We can define other GET API endpoints here like so. See that when we can utilize the 'in' operator
        # in Python here to match the string prefix of a URL, which comes in handy when our request URL's have GET
        # parameters associated with them.

        # This will add a response header to the header buffer. Here, we are simply sending back
        # an HTTP response header with an HTTP status code to the client.
        self.send_response(status)
        # This will add a header to the header buffer included in our HTTP response. Here we are specifying
        # the data Content-type of our response from the server to the client.
        self.send_header("Content-type", "text/html")
        # The end_headers method will close the header buffer, indicating that we're not sending
        # any more headers back to the client after the line below.
        self.end_headers()
        # Convert the Key-value python dictionary into a string which we'll use to respond to this request
        response = json.dumps(responseBody)
        logging.info('Response: ' + response)
        # Fill the output stream with our encoded response string which will be returned to the client.
        # The wfile.write() method will only accept bytes data.
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)

    # The do_POST(self) function is how we respond to POST requests from clients.
    def do_POST(self):
        path = self.path
        # Extract the POST body data from the HTTP request, and store it into a Python
        # dictionary we can utilize inside of any of our POST endpoints.
        postBody = self.extract_POST_Body()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND'].value

        responseBody = {}
        if path == '/registration':
            # create instance of the FleetManager Class, FleetManager class will validate the information

            # 1. Access POST parameters using your postBody
            fleetManager = FleetManager(postBody['email'], first_name=postBody['firstName'],
                                last_name=postBody['lastName'], password=postBody['password'])
            fleetManagerDict = fleetManager.get_register_data()

            # attempting to add user into DB with Controllers.FleetManagerController
            responseBody = registerUser(fleetManagerDict)

            # set status
            status = self.HTTP_STATUS_RESPONSE_CODES[responseBody["status"]].value

        elif path == '/login':
            customer = FleetManager(postBody["email"],
                                password=postBody["password"])
            email, password = FleetManager.get_login_data()

            # attempting to find user credentials with DB with method in Controllers.FleetManagerController
            responseBody = loginUser(email, password)

            # set status
            status = self.HTTP_STATUS_RESPONSE_CODES[responseBody["status"]].value
        
        elif path == '/vehicles/add':
            vehicleAdd = Vehicle(postBody['fleetID'],
                                postBody['vehicleModel'],
                                postBody['licensePlate'],
                                postBody['vehicleStatus'],
                                postBody['id'],
                                postBody['serviceType']
                                )
            vehicleDict = vehicleAdd.get_register_data()
            # attempting to add user into DB with controllers.VehicleController
            responseBody = registerVehicle(vehicleDict)
            status = self.HTTP_STATUS_RESPONSE_CODES[responseBody["status"]].value
                    
         


        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # When using the json.dumps() method, you may encounter data types which aren't easily serializable into
        # a string. When working with these types of data you can include an additional parameters in the dumps()
        # method, 'default=str' to let the serializer know to convert to a string when it encounters a data type
        # it doesn't automatically know how to convert.
        response = json.dumps(responseBody, indent=4,
                              sort_keys=True, default=str)
        logging.info('Response: ' + response)
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)


# Turn the application server on at port 8082 on localhost and fork the process.
if __name__ == '__main__':
    hostName = "localhost"
    # Ports are part of a socket connection made between a server and a client. Ports 0-1023 are
    # reserved for common TCP/IP applications and shouldn't be used here. Communicate with your
    # DevOps member to find out which port you should be running your application off of.
    serverPort = 8082
    appServer = HTTPServer((hostName, serverPort), TaasAppService)
    logging.info('Server started http://%s:%s' % (hostName, serverPort))

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    logging.info('Server stopped')
