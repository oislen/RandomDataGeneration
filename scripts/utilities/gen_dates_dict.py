import pandas as pd
import numpy as np
from datetime import datetime


def gen_dates_dict(idhashes_cnts_dict, start_date, end_date):
    """Generates a dictionary of random dates for an input dictionary of idhashes counts

    Parameters
    ----------
    idhashes_cnts_dict : dict
        A dictionary of idhashes counts
    start_date : str
        The start date ("%Y-%m-%d") to generate random dates from
    end_date : str
        The end date ("%Y-%m-%d") to generate random dates till

    Returns
    -------
    dict
        A dictionary of idhashes dates
    """
    # generate a range of dates between the given input start and end dates
    dates = pd.date_range(
        start=datetime.strptime(start_date, "%Y-%m-%d"),
        end=datetime.strptime(end_date, "%Y-%m-%d") - pd.Timedelta(days=1),
        freq="d",
    )
    # extract out the idhashes from idhashes counts dictionary
    idhashes_list = list(idhashes_cnts_dict.keys())
    # randomly sample dates for each of the idhashes
    dates_list = list(np.random.choice(a=dates, replace=True, size=len(idhashes_list)))
    # return a dictionary of idhashes and dates
    idhashes_dates_dict = dict(zip(idhashes_list, dates_list))
    return idhashes_dates_dict
