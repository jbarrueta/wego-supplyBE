from classes.fleet import Fleet
import unittest

class TestFleet(unittest.TestCase):
    def setUp(self):
        self.fleet = Fleet("test@test.com", "Testf", "Testl", "testpass")
        #self.fleet = Fleet("The Fleet")




if __name__ == '__main__':
    unittest.main()