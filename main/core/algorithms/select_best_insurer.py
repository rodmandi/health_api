import pandas as pd
from core.helpers.DefaultLogger import DefaultLogger
logger = DefaultLogger.get_logger(__name__)


def select_best_insurer(insurers_results):
    """
        Function that selects true value given insurers information
    :param insurers_results: List with insurers API's results
    :return:
    """
    if insurers_results == []:
        return None
    df = pd.DataFrame.from_dict(insurers_results, orient='columns')
    if len(insurers_results) > 1:
        # Get Most Frequent group
        series = df.groupby(['deductible'])['deductible'].count()

        deductible = None
        stop_loss = None
        oop_max = None

        if series.values[0] > 1:
            deductible = series.values[0]

        series = df.groupby(['stop_loss'])['stop_loss'].count()

        if series.values[0] > 1:
            stop_loss = series.values[0]
        oop_max = df["oop_max"].min()
        if (deductible is None) & (stop_loss is None):
            df = df[df["oop_max"] == oop_max].sort_values(by=["deductible", "stop_loss"]).iloc[0, :]
        if deductible is None:
            df = df[df["stop_loss"] == stop_loss].sort_values(by=["deductible", "oop_max"]).iloc[0, :]
        if stop_loss is None:
            df = df[df["deductible"] == deductible].sort_values(by=["stop_loss", "oop_max"]).iloc[0, :]

    result = df.iloc[0, :].to_dict()
    logger.info(result)
    return result


