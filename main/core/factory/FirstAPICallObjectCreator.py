from core.factory.APICallObjectCreator import APIObjectCreator
from core.object.concrete.FirstAPICallObject import FirstAPICallObject


class FirstAPICallObjectCreator(APIObjectCreator):
    """
        Factory to create first api objects
    """

    def create_object(self, domain, method, params):
        """
        Creates the APICallObject
        :param domain: Str that contains the API that we want to send a request
        :param method: Str that contains the name of the method to call
        :param params: JSON Object with the parameters to send to the API
        :return:
        """
        first_api_object = FirstAPICallObject()
        first_api_object.assign_features(domain, method, params)
        return first_api_object

