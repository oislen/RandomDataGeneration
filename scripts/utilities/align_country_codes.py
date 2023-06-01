import random
import numpy as np
import pandas as pd

def align_country_codes(series, proba_comm_ip = 0.95, proba_comm_card = 0.99):
    """"""
    random_unif = random.uniform(0, 1)
    # extract country codes
    registration_country_code = series['registration_country_code']
    ip_country_code = series['ip_country_code']
    card_country_code = series['card_country_code']
    # determine new ip country code
    if ip_country_code == ip_country_code:
        if random_unif >= proba_comm_ip:
            new_ip_country_code = ip_country_code
        else:
            new_ip_country_code = registration_country_code
    else:
        new_ip_country_code = np.nan
    # determine new card country code
    if card_country_code == card_country_code:
        if random_unif >= proba_comm_card:
            new_card_country_code = card_country_code
        else:
            new_card_country_code = registration_country_code
    else:
        new_card_country_code = np.nan
    # return aligned codes
    align_code_dict = {'registration_country_code':registration_country_code, 'ip_country_code':new_ip_country_code, 'card_country_code':new_card_country_code}
    aligned_code_series = pd.Series(align_code_dict)
    return aligned_code_series