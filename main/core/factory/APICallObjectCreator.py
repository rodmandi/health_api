import abc


class APIObjectCreator(metaclass=abc.ABCMeta):
    """
        Declare the factory method, which returns an object of type APICallObject
        Creator may also define a default implementation of the Factory
    """
    @abc.abstractmethod
    def create_object(self, domain, method, params):
        """
        Creates the APICallObject
        :param domain: Str that contains the API that we want to send a request
        :param method: Str that contains the method in order to call the API
        :param params: JSON Object with the parameters to send to the API
        :return:
        """