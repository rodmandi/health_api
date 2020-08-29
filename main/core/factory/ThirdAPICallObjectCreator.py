from core.factory.APICallObjectCreator import APIObjectCreator
from core.object.concrete.ThirdAPICallObject import ThirdAPICallObject


class ThirdAPICallObjectCreator(APIObjectCreator):
    """
        Factory to create Third api objects
    """
    def create_object(self, domain, method, params):
        """
        Creates the APICallObject
        :param domain: Str that contains the API that we want to send a request
        :param method: Str that contains the name of the method to call
        :param params: JSON Object with the parameters to send to the API
        :return:
        """
        third_api_object = ThirdAPICallObject()
        third_api_object.assign_features(domain, method, params)
        return third_api_object
