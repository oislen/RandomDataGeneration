import cons
import numpy as np
import pandas as pd
from utilities.cnt2prop_dict import cnt2prop_dict


def gen_country_codes_dict(idhashes_cnts_dict):
    """Generates a dictionary of random country codes for an input dictionary of idhashes counts

    Parameters
    ----------
    idhashes_cnts_dict : dict
        A dictionary of idhashes counts

    Returns
    -------
    dict
        A dictionary of idhashes country codes
    """

    # load population data of european countries
    european_populations_cnt_data = pd.read_csv(
        filepath_or_buffer=cons.fpath_countrieseurope,
        usecols=["ISO numeric", "population"],
    )
    # convert to a dictionary of ISO country codes with population counts
    european_populations_cnt_dict = european_populations_cnt_data.set_index(
        "ISO numeric"
    ).to_dict()["population"]
    # convert dictionary of population counts to dictionary of population proportions
    european_populations_props_dict = cnt2prop_dict(european_populations_cnt_dict)
    # extract out idhashes from idhashes counts dictionary
    idhashes_list = list(idhashes_cnts_dict.keys())
    # randomly generate country codes for all idhashes based on population proportions
    country_codes_list = list(
        np.random.choice(
            a=list(european_populations_props_dict.keys()),
            p=list(european_populations_props_dict.values()),
            replace=True,
            size=len(idhashes_list),
        )
    )
    # return a dictionary of idhashes and country codes
    idhashes_country_codes = dict(zip(idhashes_list, country_codes_list))
    return idhashes_country_codes
