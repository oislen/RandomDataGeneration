import cons
import pandas as pd

def gen_country_codes_map():
    """"""
    country_codes_data = pd.read_csv(cons.european_populations_url, usecols = ['ISO numeric', 'ISO alpha 2'])
    country_codes_map = country_codes_data.set_index('ISO numeric').to_dict()['ISO alpha 2']
    return country_codes_map
