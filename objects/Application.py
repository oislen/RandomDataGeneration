import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict

class Application():

    def __init__(self, n_application_hashes):
        self.n_application_hashes = n_application_hashes
        self.lam = cons.user_config['lambda']['application']
        self.application_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_application_hashes, lam = self.lam)
        self.application_hashes_props_dict = cnt2prop_dict(self.application_hashes_cnts_dict)
        self.application_hashes_prices_dict = self.gen_application_prices(self.application_hashes_cnts_dict)
    
    def gen_application_prices(self, app_hashes_dict):
        """"""
        app_hashes = list(app_hashes_dict.keys())
        app_prices = np.round(np.abs(np.random.normal(loc = 0, scale = 2, size = len(app_hashes)))**2, 2)
        app_prices_dict = dict(zip(app_hashes, app_prices))
        return app_prices_dict