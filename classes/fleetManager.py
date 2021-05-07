# FleetManager class
import re


class FleetManager:
    def __init__(self, email, first_name=None, last_name=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def getFirstName(self):
        return self.first_name

    def setFirstName(self, first_name):
        if(re.match("^[a-zA-Z]+$", first_name)):
            self.first_name = first_name
        else:
            raise ValueError("First name can only have letters")
    def getLastName(self):
        return self.last_name

    def setLastName(self, last_name):
        if(re.match("^[a-zA-Z]+$", last_name)):
            self.last_name = last_name
        else:
            raise ValueError("Last name can only have letters")

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        if(re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email)):
            self.email = email
        else:
            raise ValueError("Invalid email passed!")

    def setPassword(self, password):
        if(re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$", password)):
            self.password = password
        else:
            raise ValueError("Passwords must be 6 to 20 characters which contain at least one numeric digit, one uppercase and one lowercase letter")

    def get_register_data(self):
        return self.__dict__

    def get_login_data(self):
        return self.email, self.password
