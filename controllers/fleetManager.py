from classes.fleetManager import FleetManager
from mongo.mongoConfig import mongoConnect
import bcrypt


def registerUser(postBody):
    response = {}
    try:
        #1. Data validation in FleetManager class
        fleetManager = FleetManager(postBody['email'], first_name=postBody['firstName'],
                                last_name=postBody['lastName'], password=postBody['password'])
        fleetManagerObj = fleetManager.get_register_data()
        # 2. Open a new database connection
        client = mongoConnect()
        # 3. write data from the database
        db = client.team12_supply  # check
        fleetManager = db.fleetManager
        if (fleetManager.count_documents({'email': fleetManagerObj['email']}) == 0):
            fleetManagerObj['password'] = hashPassword(
                fleetManagerObj['password'])
            fleetManagerID = fleetManager.insert_one(
                fleetManagerObj).inserted_id
            response = {'status': 'OK', 'data': {
                'email': fleetManagerObj['email'], 'fName': fleetManagerObj['first_name'], 'lName': fleetManagerObj['last_name'], "id": fleetManagerID}}
        else:
            response = {'status': 'CONFLICT', 'data': {
                'msg': 'Email is already registered'}}
    except ValueError as err:
        response = {'status': 'CONFLICT', 'data': {
                'msg': err}}
    except Exception as err:
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {
            'msg': 'Server stopped working, please try again later'}}
    return response

# Pre: takes email and password
# Post: Returns obj with email, first name, last name, userid


def loginUser(postBody):
    response = {}
    try:
        fleetManager = FleetManager(postBody["email"],
                                password=postBody["password"])
        email, password = fleetManager.get_login_data()
        client = mongoConnect()
        db = client.team12_supply
        fleetManager = db.fleetManager
        user = fleetManager.find_one({'email': email})
        print(user)
        # checkPassword() will return T/F
        if (user != None and checkPassword(password, user['password'])):
            response = {'status': 'OK', 'data': {
                'email': user['email'], 'fName': user['first_name'], 'lName': user['last_name'], "id": user["_id"]}}
        else:
            response = {'status': 'CONFLICT', 'data': {
                'msg': 'Credentials incorrect'}}
    except ValueError as err:
        response = {'status': 'CONFLICT', 'data': {
                'msg': err}}
    except Exception as err:
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {
            'msg': 'Server stopped working, please try again later'}}
    return response


def hashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def checkPassword(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
