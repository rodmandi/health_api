import unittest
from core.algorithms.select_best_insurer import select_best_insurer
from core.helpers.standardization import format_result_object

class TestBaseAPI(unittest.TestCase):
    """
        Test the algorithm that selects the true value
    """
    def test_health_service(self):
        """
            Function for test the health insurance API when is receiving information and processing correctly
        :param self:
        :return:
        """
        options = [
                {
                    'deductible': 1000,
                    'stop_loss': 10000,
                    'oop_max': 5000
                },
                {
                    'deductible': 1200,
                    'stop_loss': 13000,
                    'oop_max': 6000
                },
                {
                    'deductible': 1000,
                    'stop_loss': 10000,
                    'oop_max': 6000
                }
            ]
        response = format_result_object(select_best_insurer(options))
        self.assertEqual(response, {"deductible": "1000", "oop_max": "5000", "stop_loss": "10000"},
                             "The algorithm changes the way to select the true value")
