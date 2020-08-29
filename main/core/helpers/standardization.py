
def format_result_object(results):
    """
    Formats the result object so it can be send using requests
    :param results: The object from cleaned results.
    :return: The result object formatted
    """
    result = {}
    for key, value in results.items():

        if not isinstance(value, str):
            if not isinstance(value, tuple):
                if not isinstance(value, dict):
                    result[key] = str(value)
                else:
                    result[key] = value
            else:
                result[key] = value
        else:
            result[key] = value
    return result