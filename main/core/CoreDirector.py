import os
from core.factory.FirstAPICallObjectCreator import FirstAPICallObjectCreator
from core.factory.SecondAPICallObjectCreator import SecondAPICallObjectCreator
from core.factory.ThirdAPICallObjectCreator import ThirdAPICallObjectCreator
from core.algorithms.select_best_insurer import select_best_insurer
from core.helpers.standardization import format_result_object
import json


ENDPOINT = os.environ['DOMAIN']
FIRST_API_METHOD = os.environ['FIRST_METHOD']
SECOND_API_METHOD = os.environ['SECOND_METHOD']
THIRD_API_METHOD = os.environ['THIRD_METHOD']


class CoreDirector:
    """
        Director that helps to determine the true value of patient given a set of results from multiple APIS
    """
    def __init__(self):
        self.api_name = "Health_API"

    def calculate_true_value(self, params):
        """
            Function that determines the true insurance value of Patient
        :return:
        """
        results = []
        response = None
        FirstAPI = FirstAPICallObjectCreator()
        SecondAPI = SecondAPICallObjectCreator()
        ThirdAPI = ThirdAPICallObjectCreator()
        first_api = FirstAPI.create_object(ENDPOINT, FIRST_API_METHOD, params)
        if first_api.result:
            results.append(first_api.result)
        second_api = SecondAPI.create_object(ENDPOINT, SECOND_API_METHOD, params)
        if second_api.result:
            results.append(second_api.result)
        third_api = ThirdAPI.create_object(ENDPOINT, THIRD_API_METHOD, params)
        if second_api.result:
            results.append(third_api.result)
        result = select_best_insurer(results)
        if result:
            response = format_result_object(result)

        return response





