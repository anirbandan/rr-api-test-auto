import unittest
import requests
from src.python.CommonFacilities import *

class TestAPIAutomation(unittest.TestCase):
    ENDPOINT = "api/users/"
    @classmethod
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.config = get_test_configuration()
        self.url = self.config["base_url"] + self.ENDPOINT
        self.test_data_json = get_test_data()

    def test_verify_user_exists(self):
        user_id = str(2)
        logging.info('Test case to verify user id exists')
        response_status_code = requests.get(self.url + user_id).status_code
        self.assertEqual(response_status_code, 200, 'User does not exist for id ' + user_id)

    def test_verify_user_details(self):
        user_id = str(2)
        logging.info('Test case to verify user first name, last name and email')
        response = requests.get(self.url + user_id)
        if (response.status_code == 200):
            self.assertEqual(get_response_details(response, "data.first_name"), "Janet", "Verification of first name fails")
            self.assertEqual(get_response_details(response, "data.last_name"), "Weaver", "Verification of first name fails")
            self.assertEqual(get_response_details(response, "data.email"), "janet.weaver@reqres.in", "Verification of first name fails")
        else: self.assertEqual(response.status_code, 200, 'User does not exist for id =' + user_id)

    def test_create_user(self):
        logging.info('Test case to verify user is getting created successfully')
        response = requests.post(self.url, self.test_data_json)
        self.assertEqual(response.status_code, 201, 'User creation was not successful')

if __name__ == '__main__':
        unittest.main()