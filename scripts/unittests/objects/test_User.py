import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from objects.User import User

exp_user_ids_cnts_dict = {
    "6374692674377254": 420,
    "1751409580926382": 318,
    "4264861381989413": 244,
    "6720317315593519": 387,
}
exp_user_ids_props_dict = {
    "6374692674377254": 0.30679327976625276,
    "1751409580926382": 0.2322863403944485,
    "4264861381989413": 0.17823228634039445,
    "6720317315593519": 0.28268809349890434,
}
exp_user_ids_firstname_dict = {
    "6374692674377254": "mikel",
    "1751409580926382": "haas",
    "4264861381989413": "rachelle",
    "6720317315593519": "erika",
}
exp_user_ids_lastname_dict = {
    "6374692674377254": "gpp",
    "1751409580926382": "moraitis",
    "4264861381989413": "bibiana",
    "6720317315593519": "herrera",
}
exp_user_ids_country_code_dict = {
    "6374692674377254": 620,
    "1751409580926382": 826,
    "4264861381989413": 528,
    "6720317315593519": 826,
}
exp_user_ids_email_domain_dict = {
    "6374692674377254": "live.co.uk",
    "1751409580926382": "free.fr",
    "4264861381989413": "yahoo.com",
    "6720317315593519": "gmail.com",
}
exp_user_ids_dates_dict = {
    "6374692674377254": np.datetime64("2020-03-02T00:00:00.000000000"),
    "1751409580926382": np.datetime64("2020-08-03T00:00:00.000000000"),
    "4264861381989413": np.datetime64("2020-10-19T00:00:00.000000000"),
    "6720317315593519": np.datetime64("2020-04-08T00:00:00.000000000"),
}
exp_start_date = cons.unittest_registration_start_date
exp_end_date = cons.unittest_registration_end_date
exp_n_user_ids = cons.unittest_n_entities
exp_lam = cons.data_model_poisson_params["user"]["lambda"]

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)
user_object = User(exp_n_user_ids, exp_start_date, exp_end_date)

obs_user_ids_cnts_dict = user_object.user_ids_cnts_dict
obs_user_ids_props_dict = user_object.user_ids_props_dict
obs_user_ids_firstname_dict = user_object.user_ids_firstname_dict
obs_user_ids_lastname_dict = user_object.user_ids_lastname_dict
obs_user_ids_country_code_dict = user_object.user_ids_country_code_dict
obs_user_ids_email_domain_dict = user_object.user_ids_email_domain_dict
obs_user_ids_dates_dict = user_object.user_ids_dates_dict
obs_start_date = user_object.start_date
obs_end_date = user_object.end_date
obs_n_user_ids = user_object.n_user_ids
obs_lam = user_object.lam


class Test_User(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_user_ids_cnts_dict = exp_user_ids_cnts_dict
        self.obs_user_ids_cnts_dict = obs_user_ids_cnts_dict
        self.exp_user_ids_props_dict = exp_user_ids_props_dict
        self.obs_user_ids_props_dict = obs_user_ids_props_dict
        self.exp_user_ids_firstname_dict = exp_user_ids_firstname_dict
        self.obs_user_ids_firstname_dict = obs_user_ids_firstname_dict
        self.exp_user_ids_lastname_dict = exp_user_ids_lastname_dict
        self.obs_user_ids_lastname_dict = obs_user_ids_lastname_dict
        self.exp_user_ids_country_code_dict = exp_user_ids_country_code_dict
        self.obs_user_ids_country_code_dict = obs_user_ids_country_code_dict
        self.exp_user_ids_email_domain_dict = exp_user_ids_email_domain_dict
        self.obs_user_ids_email_domain_dict = obs_user_ids_email_domain_dict
        self.exp_user_ids_dates_dict = exp_user_ids_dates_dict
        self.obs_user_ids_dates_dict = obs_user_ids_dates_dict
        self.exp_start_date = exp_start_date
        self.obs_start_date = obs_start_date
        self.exp_end_date = exp_end_date
        self.obs_end_date = obs_end_date
        self.exp_n_user_ids = exp_n_user_ids
        self.obs_n_user_ids = obs_n_user_ids
        self.exp_lam = exp_lam
        self.obs_lam = obs_lam

    def test_type(self):
        self.assertEqual(type(self.obs_user_ids_cnts_dict), type(self.exp_user_ids_cnts_dict))
        self.assertEqual(type(self.obs_user_ids_props_dict), type(self.exp_user_ids_props_dict))
        self.assertEqual(type(self.obs_user_ids_firstname_dict),type(self.exp_user_ids_firstname_dict),)
        self.assertEqual(type(self.obs_user_ids_lastname_dict), type(self.exp_user_ids_lastname_dict))
        self.assertEqual(type(self.obs_user_ids_country_code_dict),type(self.exp_user_ids_country_code_dict),)
        self.assertEqual(type(self.obs_user_ids_email_domain_dict),type(self.exp_user_ids_email_domain_dict),)
        self.assertEqual(type(self.obs_user_ids_dates_dict), type(self.exp_user_ids_dates_dict))
        self.assertEqual(type(self.obs_start_date), type(self.exp_start_date))
        self.assertEqual(type(self.obs_end_date), type(self.exp_end_date))
        self.assertEqual(type(self.obs_n_user_ids), type(self.exp_n_user_ids))
        self.assertEqual(type(self.obs_lam), type(self.exp_lam))

    def test_len(self):
        self.assertEqual(len(self.obs_user_ids_cnts_dict), len(self.exp_user_ids_cnts_dict))
        self.assertEqual(len(self.obs_user_ids_props_dict), len(self.exp_user_ids_props_dict))
        self.assertEqual(len(self.obs_user_ids_firstname_dict), len(self.exp_user_ids_firstname_dict))
        self.assertEqual(len(self.obs_user_ids_lastname_dict), len(self.exp_user_ids_lastname_dict))
        self.assertEqual(len(self.obs_user_ids_country_code_dict),len(self.exp_user_ids_country_code_dict),)
        self.assertEqual(len(self.obs_user_ids_email_domain_dict),len(self.exp_user_ids_email_domain_dict),)
        self.assertEqual(len(self.obs_user_ids_dates_dict), len(self.exp_user_ids_dates_dict))

    def test_keys(self):
        self.assertEqual(list(self.obs_user_ids_cnts_dict.keys()),list(self.exp_user_ids_cnts_dict.keys()),)
        self.assertEqual(list(self.obs_user_ids_props_dict.keys()),list(self.exp_user_ids_props_dict.keys()),)
        self.assertEqual(list(self.obs_user_ids_firstname_dict.keys()),list(self.exp_user_ids_firstname_dict.keys()),)
        self.assertEqual(list(self.obs_user_ids_lastname_dict.keys()),list(self.exp_user_ids_lastname_dict.keys()),)
        self.assertEqual(list(self.obs_user_ids_country_code_dict.keys()),list(self.exp_user_ids_country_code_dict.keys()),)
        self.assertEqual(list(self.obs_user_ids_email_domain_dict.keys()),list(self.exp_user_ids_email_domain_dict.keys()),)
        self.assertEqual(list(self.obs_user_ids_dates_dict.keys()),list(self.exp_user_ids_dates_dict.keys()),)

    def test_values(self):
        self.assertEqual(list(self.obs_user_ids_cnts_dict.values()),list(self.exp_user_ids_cnts_dict.values()),)
        self.assertEqual(list(self.obs_user_ids_props_dict.values()),list(self.exp_user_ids_props_dict.values()),)
        self.assertEqual(list(self.obs_user_ids_firstname_dict.values()),list(self.exp_user_ids_firstname_dict.values()),)
        self.assertEqual(list(self.obs_user_ids_lastname_dict.values()),list(self.exp_user_ids_lastname_dict.values()),)
        self.assertEqual(list(self.obs_user_ids_country_code_dict.values()),list(self.exp_user_ids_country_code_dict.values()),)
        self.assertEqual(list(self.obs_user_ids_email_domain_dict.values()),list(self.exp_user_ids_email_domain_dict.values()),)
        self.assertEqual(list(self.obs_user_ids_dates_dict.values()),list(self.exp_user_ids_dates_dict.values()),)

    def test_object(self):
        self.assertEqual(self.obs_user_ids_cnts_dict, self.exp_user_ids_cnts_dict)
        self.assertEqual(self.obs_user_ids_props_dict, self.exp_user_ids_props_dict)
        self.assertEqual(self.obs_user_ids_firstname_dict, self.exp_user_ids_firstname_dict)
        self.assertEqual(self.obs_user_ids_lastname_dict, self.exp_user_ids_lastname_dict)
        self.assertEqual(self.obs_user_ids_country_code_dict, self.exp_user_ids_country_code_dict)
        self.assertEqual(self.obs_user_ids_email_domain_dict, self.exp_user_ids_email_domain_dict)
        self.assertEqual(self.obs_user_ids_dates_dict, self.exp_user_ids_dates_dict)
        self.assertEqual(self.obs_start_date, self.exp_start_date)
        self.assertEqual(self.obs_end_date, self.exp_end_date)
        self.assertEqual(self.obs_n_user_ids, self.exp_n_user_ids)
        self.assertEqual(self.obs_lam, self.exp_lam)


if __name__ == "__main__":
    unittest.main()
