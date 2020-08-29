import json
from flask import Response
from core.CoreDirector import CoreDirector


def get_true_value(params):
    """
    Process the request from a single mail
    :param json_mail:
    :return:
    """
    data_cleaning_director = CoreDirector()
    result = data_cleaning_director.calculate_true_value(params)
    if result:
        return Response(json.dumps({"result": result, "status": "ok"}, default=str), status=200, mimetype='application/json')
    else:
        return Response(json.dumps({"result": "", "status": "error", "message": 'Is not possible to calculate the true value provided by insurers'}, default=str), status=400, mimetype='application/json')