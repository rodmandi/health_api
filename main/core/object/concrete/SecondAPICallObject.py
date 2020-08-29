from core.object.abstract.APIObject import APICallObject
from core.helpers.DefaultLogger import DefaultLogger

logger = DefaultLogger.get_logger(__name__)


class SecondAPICallObject(APICallObject):

    def assign_features(self, domain, method, params):
        """
            Function that assigns the most import features of the request
        :param domain: Str that contains the API that we want to send a request
        :param method: Str that contains the name of the method to call
        :param params: JSON Object with the parameters to send to the API
        :return:
        """
        self.domain = domain
        self.method = method
        self.params = params
        response = super().send_request()

        if response is not None:
            try:
                self.result["deductible"] = response["deductible"]
                self.result["stop_loss"] = response["stop_loss"]
                self.result["oop_max"] = response["oop_max"]
            except:
                logger.error("Error getting response", self.domain, self.params)
                self.result = None
        else:
            self.result = None
