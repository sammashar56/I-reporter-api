#standard system libraries
import unittest 
import json
 
#installed libs
import unittest

#import local modules
from app import create_app
from testdb import TableCreation

class TestBaseCase(unittest.TestCase):
    """This is the base test case holds setup"""
    def setUp(self):
        """This is the test setup"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.db = TableCreation()
       
    def tearDown(self):
        with self.app.app_context():
            self.db.kill()
        