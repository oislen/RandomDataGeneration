import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_country_codes_dict import gen_country_codes_dict
from utilities.gen_shared_idhashes import gen_shared_idhashes

class Card():

    def __init__(self, n_card_hashes):
        self.n_card_hashes = n_card_hashes
        self.card_types = cons.card_types
        self.lam = cons.poisson_lambda_params['card']
        self.prop_shared_card_hashes = cons.shared_entities_dict['card']
        self.card_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_card_hashes, lam = self.lam)
        self.card_hashes_props_dict = cnt2prop_dict(self.card_hashes_cnts_dict)
        self.card_hashes_type_dict = self.gen_card_type(self.card_hashes_cnts_dict, self.card_types)
        self.card_hashes_country_code_dict = gen_country_codes_dict(self.card_hashes_cnts_dict)
        self.card_hashes_shared_props_dict = gen_shared_idhashes(self.card_hashes_cnts_dict, self.prop_shared_card_hashes)
    
    def gen_card_type(self, card_hashes_cnts_dict, card_types):
        """"""
        card_hashes = list(card_hashes_cnts_dict.keys())
        card_types = np.random.choice(a = list(card_types.keys()), p = list(card_types.values()), size = len(card_hashes), replace = True)
        card_hashes_type_dict = dict(zip(card_hashes, card_types))
        return card_hashes_type_dict