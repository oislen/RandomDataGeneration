import numpy as np
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict

class Application():

    def __init__(self, n_application_hashes):
        self.n_application_hashes = n_application_hashes
        self.application_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_application_hashes)
        self.application_hashes_props_dict = cnt2prop_dict(self.application_hashes_cnts_dict)
        self.application_hashes_prices_dict = self.gen_application_prices(self.application_hashes_cnts_dict)
    
    def gen_application_prices(self, app_hashes_dict):
        """"""
        app_prices_dict = {}
        for key, val in app_hashes_dict.items():
            app_prices_dict[key] = np.round(np.random.normal(loc = 1, scale = 2, size = 1)[0]**2, 2)
        return app_prices_dict