from core.factory.APICallObjectCreator import APIObjectCreator
from core.object.concrete.SecondAPICallObject import SecondAPICallObject


class SecondAPICallObjectCreator(APIObjectCreator):
    """
        Factory to create second api objects
    """
    def create_object(self, domain, method, params):
        """
        Creates the APICallObject
        :param domain: Str that contains the API that we want to send a request
        :param method: Str that contains the name of the method to call
        :param params: JSON Object with the parameters to send to the API
        :return:
        """
        second_api_object = SecondAPICallObject()
        second_api_object.assign_features(domain, method, params)
        return second_api_object
