import unittest
from app import create_app
import json

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.data = {
		"comment":"comment",
		"type_of_incident":"adfadf",
		"location":"kawangware"
		}
        self.user = {
            "firstname":"machar",
            "lastname":"mashar",
            "phone_no":1233,
            "email":"asdfads",
            "password":"rakatacalacala",
            "confirm_password":"rakatacalacala"
        }
    def test_create_incident(self):
    	res = self.client.post('api/v1/incidents', 
        data=json.dumps(self.data), 
        content_type="application/json")
    	self.assertTrue(res.status_code == 201)

    def test_get_all_incidents(self):
        res = self.client.get('/api/v1/incidents', 
        content_type="application/json")
        self.assertTrue(res.status_code == 200)

    def test_get_specific_incident(self):
        self.client.post('api/v1/incidents', 
        data=json.dumps(self.data), 
        content_type="application/json")
        res = self.client.get('/api/v1/incident/1', 
        content_type="application/json")
        self.assertTrue(res.status_code == 200)

    def test_update_comment_only(self):
        self.client.post('api/v1/incidents', 
        data=json.dumps(self.data), 
        content_type="application/json")
        data = {
            "comment":"rakata",
        }
        res = self.client.put('/api/v1/incident/1', 
        data=json.dumps(data), content_type="application/json")
        self.assertEqual(res.status_code, 201)

    def test_update_comment_and_location(self):
        self.client.post('api/v1/incidents', 
        data=json.dumps(self.data), 
        content_type="application/json")
        data = {
            "location":"dadf",
            "comment":"fsadf"
        }
        res = self.client.put('api/v1/incident/1', 
        data=json.dumps(data), 
        content_type="application/json")
        self.assertEqual(res.status_code, 201)
        
    def test_delete_specific_incident(self):
        res = self.client.delete('api/v1/incident/1', 
        data=json.dumps(self.data), 
        content_type="application/json")
        self.assertTrue(res.status_code == 200)
    
    def test_update_location_only(self):
        self.client.post('api/v1/incidents', 
        data=json.dumps(self.data), 
        content_type="application/json")
        data = {
            "location":"adfad"
        }
        res = self.client.put('api/v1/incident/1', 
        data=json.dumps(data), 
        content_type="application/json")
        self.assertEqual(res.status_code, 201)

    def test_nothing_updated(self):
        self.client.post('api/v1/incidents', 
        data=json.dumps(self.data), 
        content_type="application/json")
        data = {}
        res = self.client.put('api/v1/incident/1', 
        data=json.dumps(data), 
        content_type="application/json")
        self.assertEqual(res.status_code, 200)
        
    def test_delete_specific_not_found(self):
        res = self.client.delete('api/v1/incident/1', 
        data=json.dumps(self.data), 
        content_type="application/json")
        self.assertTrue(res.status_code == 404)        
        
    def test_register_user(self):
        res = self.client.post('api/v1/users', 
        data=json.dumps(self.user), 
        content_type="application/json")
        self.assertTrue(res.status_code == 201)

if __name__ == '__main__':
    unittest.main()
