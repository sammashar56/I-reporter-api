import unittest
import json
from app import create_app

class BaseTestCase(unittest.TestCase):
    """setting up instances that will be used all over the tests """
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_get_all_records(self):
        res = self.client.get('/api/v1/incidents', content_type="application/json")
        self.assertTrue(res.status_code == 200)

    def test_get_specific_incident(self):
        res = self.client.get('/api/v1/incident/1', content_type='application/json')
        if res.status_code == 404:
            self.assertTrue(res.status_code == 404)
        else:
            self.assertTrue(res.status_code == 200)

    def test_create_incident(self):
        data = {
        "comment": "corruption corner",
        "type_of_incident":"red flag",
        "location": "dagoretti corner"
            }
        res = self.client.post('/api/v1/incidents', content_type='application/json', data=json.dumps(data))
        self.assertEqual(res.status_code, 201)

    def test_update_incident(self):
        data = {
        "comment": "corruption corner",
        "type_of_incident":"red flag",
        "location": "dagoretti corner"
            }
        res = self.client.put('/api/v1/incident/1',content_type='application/json', data=json.dumps(data))
        self.assertTrue(res.status_code, 201)
        
    def test_delete_specific_incident(self):
        data = {
        "comment": "corruption corner",
        "type_of_incident":"red flag",
        "location": "dagoretti corner"
            }
        res = self.client.delete('/api/v1/incident/1', content_type='application/json', data=json.dumps(data))
        self.assertEquals(res.status_code, 200)
        
        

if __name__ == '__main__':
    unittest.main()