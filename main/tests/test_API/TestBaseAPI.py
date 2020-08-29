import os
import unittest
from run import app


class TestBaseAPI(unittest.TestCase):
    """
        Class for TEST the API
    """

    def test_health_service(self):
            """
                Function for test the health insurance API when is receiving information and processing correctly
            :param self:
            :return:
            """
            tester = app.test_client(self)
            response = tester.post('/health_services/get_true_value', content_type='html/text')
            self.assertEqual(response.status_code, 200, "The API is not running correctly")
            self.assertIsInstance(response.json, dict, " The algorithm changes the way to select the true value")
            self.assertEqual(response.json, {"result": {"deductible": "1000", "oop_max": "5000", "stop_loss": "10000"},
                                             "status": "ok"}, "The algorithm changes the way to select the true value")


