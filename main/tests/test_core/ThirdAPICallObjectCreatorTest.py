import unittest
from core.object.concrete.ThirdAPICallObject import ThirdAPICallObject


class APIObjectTest(unittest.TestCase):
    """
        Tests the APIObject that is in charge to make and save the information of the requests
    """
    def setUp(self):
        self.api_call_object = ThirdAPICallObject()

    def test_features(self):
            """
                Function for test the health insurance API when is receiving information and processing correctly
            :param self:
            :return:
            """
            self.assertIsInstance(self.api_call_object.result, dict,
                                  " The format of the result changed on the APIObject")
            self.assertIsInstance(self.api_call_object.method, str,
                                  " The format of the method changed on the APIObject")
            self.assertIsInstance(self.api_call_object.domain, str,
                                  " The format of the domain changed on the APIObject")
            self.assertListEqual([*self.api_call_object.result], ["deductible", "stop_loss", "oop_max"])

    def test_assign_features(self):
            """
                Function for test the health insurance API when is receiving information and processing correctly
            :param self:
            :return:
            """
            domain = "three-algo"
            method = "api3"
            api1_response = {
                'deductible': 1000,
                'stop_loss': 10000,
                'oop_max': 6000
            }
            self.api_call_object.assign_features(domain, method, {})
            self.assertIsInstance(self.api_call_object.result, dict,
                                  " The format of the result changed on the APIObject")
            self.assertIsInstance(self.api_call_object.method, str,
                                  " The format of the method changed on the APIObject")
            self.assertIsInstance(self.api_call_object.domain, str,
                                  " The format of the domain changed on the APIObject")
            self.assertListEqual([*self.api_call_object.result], ["deductible", "stop_loss", "oop_max"],
                                 "The API returned not the expected format")
            self.assertEqual(self.api_call_object.method, method, "The method changed the value of the method")
            self.assertEqual(self.api_call_object.domain, domain, "The method changed the value of the domain")
            self.assertDictEqual(self.api_call_object.result, api1_response, "The API suffer some changes internally")