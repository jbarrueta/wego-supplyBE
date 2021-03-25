from config.mongoConnect import mongoConnect
import bcrypt

def registerUser(fleetManagerData):
    response = {}
    try:
        # 2. Open a new database connection
        client = mongoConnect()
        # 3. write data from the database
        db = client.team12_demand
        FleetManager = db.FleetManager
        if (fleetManager.count_documents({'email': fleetManagerData['email']}) == 0):
            fleetManagerObj = fleetManagerData
            fleetManagerObj['password'] = hashPassword(fleetManagerData['password'])
            fleetManagerID = FleetManager.insert_one(fleetManagerObj).inserted_id
            response = {'status': 'OK', 'data': {'email': fleetManagerObj['email'], 'fName': fleetManagerObj['first_name'], 'lName': fleetManagerObj['last_name'], "id": fleetManagerID}}
        else:
            response = {'status': 'CONFLICT', 'data': {'msg': 'Email is already registered'}}
        # TODO: create session now
    except Exception as err:
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {'msg': 'Server stopped working, please try again later'}}
    return response

# Pre: takes email and password
# Post: Returns obj with email, first name, last name, userid
def loginUser(email, password):
    response = {}
    try: 
        client = mongoConnect()
        db = client.team12_demand
        fleetManager = db.fleetManager
        user = fleetManager.find_one({'email': email})
        
        # checkPassword() will return T/F
        if (user != None and checkPassword(password, user['password'])):
            response = {'status': 'OK', 'data': {'email': user['email'], 'fName': user['first_name'], 'lName': user['last_name'], "id": user["_id"]}}
        else:
            response = {'status': 'CONFLICT', 'data': {'msg': 'Credentials incorrect'}}
    except Exception as err:
        response = {'status': 'INTERNAL_SERVER_ERROR', 'data': {'msg': 'Server stopped working, please try again later'}}
    return response


def hashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def checkPassword(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)