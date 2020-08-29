from flask import Response
from core.models import health_model


def get_true_value(json):
    """
    Verify that json is correct or route logic
    :param json: Json param from client
    :return:
    """
    return health_model.get_true_value(json)
