import os
import unittest
from run_insurer import app_insurer


class TestBaseAPI(unittest.TestCase):
    """
        Class for TEST the API
    """

    def test_api_services(self):
            """
                Function for test the health insurance API when is receiving information and processing correctly
            :param self:
            :return:
            """
            api1_response = {
                'deductible': 1000,
                'stop_loss': 10000,
                'oop_max': 5000
            }
            api2_response = {
                'deductible': 1200,
                'stop_loss': 13000,
                'oop_max': 6000
            }
            api3_response = {
                'deductible': 1000,
                'stop_loss': 10000,
                'oop_max': 6000
            }
            tester = app_insurer.test_client(self)
            response = tester.post('/api1', content_type='html/text')
            self.assertEqual(response.status_code, 200, "The API is not running correctly")
            self.assertIsInstance(response.json, dict, " The algorithm changes the way to select the true value")
            self.assertEqual(response.json, api1_response)
            response = tester.post('/api2', content_type='html/text')
            self.assertEqual(response.status_code, 200, "The API is not running correctly")
            self.assertIsInstance(response.json, dict, " The algorithm changes the way to select the true value")
            self.assertEqual(response.json, api2_response)
            response = tester.post('/api3', content_type='html/text')
            self.assertEqual(response.status_code, 200, "The API is not running correctly")
            self.assertIsInstance(response.json, dict, " The algorithm changes the way to select the true value")
            self.assertEqual(response.json, api3_response)


