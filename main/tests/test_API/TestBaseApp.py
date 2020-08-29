import os
import unittest
from run import app


class BasicTestCase(unittest.TestCase):

    def test_health_service(self):
            """
                Function for test the health insurance API when is not receiving information from API parties
            :param self:
            :return:
            """
            tester = app.test_client(self)
            response = tester.post('/health_services/get_true_value', content_type='html/text')
            self.assertEqual(response.status_code, 400)
