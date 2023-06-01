import pandas as pd
import numpy as np
from datetime import datetime

def gen_dates_dict(idhashes_cnts_dict, start_date, end_date):
    """"""
    idhashes_list = list(idhashes_cnts_dict.keys())
    dates = pd.date_range(datetime.strptime(start_date, '%Y-%m-%d'), datetime.strptime(end_date, '%Y-%m-%d') - pd.Timedelta(days=1),freq='d')
    dates_list = list(np.random.choice(a = dates, replace = True, size = len(idhashes_list)))
    idhashes_dates_dict = dict(zip(idhashes_list, dates_list))
    return idhashes_dates_dict