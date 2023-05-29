import cons
import numpy as np
import pandas as pd
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_country_codes import gen_country_codes

class User():

    def __init__(self, n_user_ids):
        self.n_user_ids = n_user_ids
        self.user_ids_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'id', n = self.n_user_ids)
        self.user_ids_props_dict = cnt2prop_dict(self.user_ids_cnts_dict)
        self.user_ids_firstname_dict = self.gen_user_firstname(cons)
        self.user_ids_lastname_dict = self.gen_user_surname(cons)
        self.user_ids_country_codes = gen_country_codes(self.user_ids_cnts_dict)
    
    def gen_user_firstname(self, cons):
        """"""
        first_name_data = pd.read_csv(cons.first_names_url, header = None)
        user_ids_list = list(self.user_ids_cnts_dict.keys())
        user_firstname_list = first_name_data[0].sample(n = self.n_user_ids, replace = True)
        user_ids_firstname_dict = dict(zip(user_ids_list, user_firstname_list))
        return user_ids_firstname_dict

    def gen_user_surname(self, cons):
        """"""
        last_name_data = pd.read_csv(cons.last_names_url, header = None)
        user_ids_list = list(self.user_ids_cnts_dict.keys())
        user_lastname_list = last_name_data[0].sample(n = self.n_user_ids, replace = True)
        user_ids_lastname_dict = dict(zip(user_ids_list, user_lastname_list))
        return user_ids_lastname_dict