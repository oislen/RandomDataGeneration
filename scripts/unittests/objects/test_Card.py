import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from objects.Card import Card

exp_card_hashes_cnts_dict = {'se7kimaanzn2l1nt': 1, '1kwbloqrfe26k8h3': 1, 'od8p1jr67ydgz315': 2, '3shpx9zdue7dmkfh': 1}
exp_card_hashes_type_dict = {'se7kimaanzn2l1nt': 'visa', '1kwbloqrfe26k8h3': 'visa', 'od8p1jr67ydgz315': 'visa', '3shpx9zdue7dmkfh': 'visa'}
exp_card_hashes_props_dict = {'se7kimaanzn2l1nt': 0.2, '1kwbloqrfe26k8h3': 0.2, 'od8p1jr67ydgz315': 0.4, '3shpx9zdue7dmkfh': 0.2}
exp_card_hashes_country_code_dict = {'se7kimaanzn2l1nt': 642, '1kwbloqrfe26k8h3': 620, 'od8p1jr67ydgz315': 826, '3shpx9zdue7dmkfh': 528}
exp_card_hashes_shared_props_dict = {}
exp_card_types_dict = cons.data_model_card_types_dict
exp_prop_shared_card_hashes = cons.data_model_shared_entities_dict['card']
exp_n_card_hashes = cons.unittest_n_entities
exp_lam = cons.data_model_poisson_lambda_params['card']

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)
card_object = Card(n_card_hashes=exp_n_card_hashes)

obs_card_hashes_cnts_dict = card_object.card_hashes_cnts_dict
obs_card_types_dict = card_object.card_types_dict
obs_card_hashes_type_dict = card_object.card_hashes_type_dict
obs_card_hashes_props_dict = card_object.card_hashes_props_dict
obs_card_hashes_country_code_dict = card_object.card_hashes_country_code_dict
obs_card_hashes_shared_props_dict = card_object.card_hashes_shared_props_dict
obs_prop_shared_card_hashes = card_object.prop_shared_card_hashes
obs_lam = card_object.lam
obs_n_card_hashes = card_object.n_card_hashes

class Test_Card(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_card_hashes_cnts_dict = exp_card_hashes_cnts_dict
        self.obs_card_hashes_cnts_dict = obs_card_hashes_cnts_dict
        self.exp_card_types_dict = exp_card_types_dict
        self.obs_card_types_dict = obs_card_types_dict
        self.exp_card_hashes_type_dict = exp_card_hashes_type_dict
        self.obs_card_hashes_type_dict = obs_card_hashes_type_dict
        self.exp_card_hashes_props_dict = exp_card_hashes_props_dict
        self.obs_card_hashes_props_dict = obs_card_hashes_props_dict
        self.exp_card_hashes_country_code_dict = exp_card_hashes_country_code_dict
        self.obs_card_hashes_country_code_dict = obs_card_hashes_country_code_dict
        self.exp_card_hashes_shared_props_dict = exp_card_hashes_shared_props_dict
        self.obs_card_hashes_shared_props_dict = obs_card_hashes_shared_props_dict
        self.exp_prop_shared_card_hashes = exp_prop_shared_card_hashes
        self.obs_prop_shared_card_hashes = obs_prop_shared_card_hashes
        self.exp_lam = exp_lam
        self.obs_lam = obs_lam
        self.exp_n_card_hashes = exp_n_card_hashes
        self.obs_n_card_hashes = obs_n_card_hashes
    
    def test_type(self):
        self.assertEqual(type(self.obs_card_hashes_cnts_dict), type(self.exp_card_hashes_cnts_dict))
        self.assertEqual(type(self.obs_card_types_dict), type(self.exp_card_types_dict))
        self.assertEqual(type(self.obs_card_hashes_type_dict), type(self.exp_card_hashes_type_dict))
        self.assertEqual(type(self.obs_card_hashes_props_dict), type(self.exp_card_hashes_props_dict))
        self.assertEqual(type(self.obs_prop_shared_card_hashes), type(self.exp_prop_shared_card_hashes))
        self.assertEqual(type(self.obs_card_hashes_country_code_dict), type(self.exp_card_hashes_country_code_dict))
        self.assertEqual(type(self.obs_card_hashes_shared_props_dict), type(self.exp_card_hashes_shared_props_dict))
        self.assertEqual(type(self.obs_lam), type(self.exp_lam))
        self.assertEqual(type(self.obs_n_card_hashes), type(self.exp_n_card_hashes))

    def test_len(self):
        self.assertEqual(len(self.obs_card_hashes_cnts_dict), len(self.exp_card_hashes_cnts_dict))
        self.assertEqual(len(self.obs_card_types_dict), len(self.exp_card_types_dict))
        self.assertEqual(len(self.obs_card_hashes_type_dict), len(self.exp_card_hashes_type_dict))
        self.assertEqual(len(self.obs_card_hashes_props_dict), len(self.exp_card_hashes_props_dict))
        self.assertEqual(len(self.obs_card_hashes_country_code_dict), len(self.exp_card_hashes_country_code_dict))
        self.assertEqual(len(self.obs_card_hashes_shared_props_dict), len(self.exp_card_hashes_shared_props_dict))

    def test_keys(self):
        self.assertEqual(list(self.obs_card_hashes_cnts_dict.keys()), list(self.exp_card_hashes_cnts_dict.keys()))
        self.assertEqual(list(self.obs_card_types_dict.keys()), list(self.exp_card_types_dict.keys()))
        self.assertEqual(list(self.obs_card_hashes_type_dict.keys()), list(self.exp_card_hashes_type_dict.keys()))
        self.assertEqual(list(self.obs_card_hashes_props_dict.keys()), list(self.exp_card_hashes_props_dict.keys()))
        self.assertEqual(list(self.obs_card_hashes_country_code_dict.keys()), list(self.exp_card_hashes_country_code_dict.keys()))
        self.assertEqual(list(self.obs_card_hashes_shared_props_dict.keys()), list(self.exp_card_hashes_shared_props_dict.keys()))

    def test_values(self):
        self.assertEqual(list(self.obs_card_hashes_cnts_dict.values()), list(self.exp_card_hashes_cnts_dict.values()))
        self.assertEqual(list(self.obs_card_types_dict.values()), list(self.exp_card_types_dict.values()))
        self.assertEqual(list(self.obs_card_hashes_type_dict.values()), list(self.exp_card_hashes_type_dict.values()))
        self.assertEqual(list(self.obs_card_hashes_props_dict.values()), list(self.exp_card_hashes_props_dict.values()))
        self.assertEqual(list(self.obs_card_hashes_country_code_dict.values()), list(self.exp_card_hashes_country_code_dict.values()))
        self.assertEqual(list(self.obs_card_hashes_shared_props_dict.values()), list(self.exp_card_hashes_shared_props_dict.values()))

    def test_object(self):
        self.assertEqual(self.obs_card_hashes_cnts_dict, self.exp_card_hashes_cnts_dict)
        self.assertEqual(self.obs_card_types_dict, self.exp_card_types_dict)
        self.assertEqual(self.obs_card_hashes_type_dict, self.exp_card_hashes_type_dict)
        self.assertEqual(self.obs_card_hashes_props_dict, self.exp_card_hashes_props_dict)
        self.assertEqual(self.obs_prop_shared_card_hashes, self.exp_prop_shared_card_hashes)
        self.assertEqual(self.obs_card_hashes_country_code_dict, self.exp_card_hashes_country_code_dict)
        self.assertEqual(self.obs_card_hashes_shared_props_dict, self.exp_card_hashes_shared_props_dict)
        self.assertEqual(self.obs_lam, self.exp_lam)
        self.assertEqual(self.obs_n_card_hashes, self.exp_n_card_hashes)


if __name__ == "__main__":
    unittest.main()
