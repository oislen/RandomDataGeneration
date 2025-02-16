import cons
import pandas as pd
from beartype import beartype

@beartype
def gen_country_codes_map(
    fpath_countrieseurope:str=cons.fpath_countrieseurope
    ) -> dict:
    """
    Generates a dictionary of ISO numeric codes mapping to ISO alpha codes.

    Parameters
    ----------
    fpath_countrieseurope : str
        The full file path to the european countries reference file, default is cons.fpath_countrieseurope.

    Returns
    -------
    dict
        A dictionary of ISO numeric codes mapping to ISO alpha codes.
    """
    # load european county codes data
    country_codes_data = pd.read_csv(filepath_or_buffer=fpath_countrieseurope, usecols=["ISO numeric", "ISO alpha 2"],)
    # convert data to a dictionary of ISO numeric codes mapping to ISO alpha codes
    country_codes_map = country_codes_data.set_index("ISO numeric").to_dict()["ISO alpha 2"]
    return country_codes_map
