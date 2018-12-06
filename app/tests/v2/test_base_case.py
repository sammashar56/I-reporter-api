#standard system libraries

import unittest 
import json
 
#installed libs
import pytest


#import local modules
from app import create_app

# class BaseTestCase(unittest.TestCase):
#     def Setup(self):
#         self.app = create_app('testing')
#         self.client = self.app.test_client()
#         pass
#     def teardown(self):
          