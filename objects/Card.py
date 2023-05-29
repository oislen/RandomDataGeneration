import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict

class Card():

    def __init__(self, n_card_hashes):
        self.n_card_hashes = n_card_hashes
        self.card_types = cons.card_types
        self.card_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_card_hashes)
        self.card_hashes_props_dict = cnt2prop_dict(self.card_hashes_cnts_dict)
        self.card_hashes_type_dict = self.gen_card_type(self.card_hashes_cnts_dict, self.card_types)
    
    def gen_card_type(self, card_hashes_cnts_dict, card_types):
        """"""
        card_hashes_type_dict = {}
        for key, val in card_hashes_cnts_dict.items():
            card_type = np.random.choice(a = list(card_types.keys()), p = list(card_types.values()), size = 1, replace = True)[0]
            card_hashes_type_dict[key] = card_type
        return card_hashes_type_dict