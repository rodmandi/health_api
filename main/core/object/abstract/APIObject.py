import abc
import grequests
import os
import json
from core.helpers.DefaultLogger import DefaultLogger

logger = DefaultLogger.get_logger(__name__)
API_PORT = 6000


class APICallObject(metaclass=abc.ABCMeta):
    """
    Define the interface of object the factory method creates.
    Creates APICall Object
    """
    def __init__(self):
        """
            Constructor of the APICall object
        """
        self.method = ""
        self.domain = ""
        self.params = {}
        self.result = {
            "deductible": int(),
            "stop_loss": int(),
            "oop_max": int()
        }

    @property
    def response(self):
        """
            Getter for result dictionary
        :return:
        """
        return self.result

    @abc.abstractmethod
    def assign_features(self, method, domain, params):
        """
            Abstract method for assign features of the request
        :param features:
        :return:
        """
        pass

    def make_request(self, req):
        """
            Function that sends a request to a specific API
        :param req: Request object
        :return:
        """
        responses = list()
        response_json = None
        try:
            responses = grequests.map(req)
        except:
            logger.exception('URL', self.domain)

        try:
            response = responses[0]
            if not response:
                logger.error("Request No Response", self.domain)
            else:
                status = response.status_code
                if 200 <= status < 300:
                    status_message = "Success"
                    logger.info("Request {} {}".format(status_message, status), self.domain)
                    response_json = response.json()
                else:
                    if 400 <= status < 500:
                        status_message = "Client Error " + "{}".format(response.text.replace("\n", "\\n"))
                    elif 500 <= status < 600:
                        status_message = "Server Error " + "{}".format(response.text.replace("\n", "\\n"))
                    logger.info("Request {} {}".format(status_message, status), self.domain)
        except:
            logger.error("Error getting response", self.domain)

        return response_json

    def send_request(self):
        """

        :return:
        """
        logger.info("Request http://{}:{}/{} ".format(self.domain, API_PORT, self.method))
        response = self.make_request([grequests.post(
            "http://{}:{}/{}".format(
                self.domain,
                API_PORT,
                self.method
            ),
            json=json.loads(json.dumps(self.params, default=str)), headers={"Content-Type": "application/json"},
            verify=False, timeout=20)])
        return response
