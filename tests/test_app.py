from tests.test_base import BaseTestCase
from app.helpers.db import Database
# from api.models.user import User
# from api import DB
import json


class Test_auth(BaseTestCase):
    def test_signup(self):
        """
        Test a user is successfully created through the api
        """
        with self.test_client:
            response = self.register_user("grace", "bantariza")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status'], 200)
            self.assertEqual(data['message'], "you have successfully signed up")
    
    def tests_index(self):
        with self.test_client:
            response = self.test_index()
            data = json.loads(response.data.decode())
            
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], "hi welcome to the ireporter testing")
            self.assertEqual(data['status'], 200)