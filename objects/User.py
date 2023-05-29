import cons
import numpy as np
import pandas as pd
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_country_codes import gen_country_codes
from utilities.gen_dates_dict import gen_dates_dict

class User():

    def __init__(self, n_user_ids, start_date, end_date):
        self.n_user_ids = n_user_ids
        self.start_date = start_date
        self.end_date = end_date
        self.user_ids_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'id', n = self.n_user_ids)
        self.user_ids_props_dict = cnt2prop_dict(self.user_ids_cnts_dict)
        self.user_ids_firstname_dict = self.gen_user_firstname(cons)
        self.user_ids_lastname_dict = self.gen_user_surname(cons)
        self.user_ids_country_code_dict = gen_country_codes(self.user_ids_cnts_dict)
        self.user_ids_email_domain_dict = self.gen_user_email_domain(cons)
        self.user_ids_dates_dict = gen_dates_dict(self.user_ids_cnts_dict, start_date = self.start_date, end_date = self.end_date)
    
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
    
    def gen_user_email_domain(self, cons):
        """"""
        email_domain_data = pd.read_csv(cons.domain_email_fpath, index_col = 0)
        email_domain_data['proportion'] = email_domain_data['proportion'].divide(email_domain_data['proportion'].sum())
        email_domain_dict = email_domain_data.set_index('domain').to_dict()['proportion']
        user_ids_list = list(self.user_ids_cnts_dict.keys())
        user_email_domain_list = list(np.random.choice(a = list(email_domain_dict.keys()), p = list(email_domain_dict.values()), replace = True, size = len(user_ids_list)))
        user_ids_email_domain_dict = dict(zip(user_ids_list, user_email_domain_list))
        return user_ids_email_domain_dict