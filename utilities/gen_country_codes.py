import cons
import numpy as np
import pandas as pd
from utilities.cnt2prop_dict import cnt2prop_dict

def gen_country_codes(cnts_dict):
    """"""
    european_populations_cnt_data = pd.read_csv(cons.european_populations_url, usecols = ['ISO numeric', 'population'])
    european_populations_cnt_dict = european_populations_cnt_data.set_index('ISO numeric').to_dict()['population']
    european_populations_props_dict = cnt2prop_dict(european_populations_cnt_dict)
    idhashes_list = list(cnts_dict.keys())
    country_codes_list = list(np.random.choice(a = list(european_populations_props_dict.keys()), p = list(european_populations_props_dict.values()), replace = True, size = len(idhashes_list)))
    idhashes_country_codes = dict(zip(idhashes_list, country_codes_list))
    return idhashes_country_codes
