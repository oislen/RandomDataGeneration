import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from objects.Ip import Ip

exp_ip_hashes_cnts_dict = {'se7kimaanzn2l1nt': 11, '1kwbloqrfe26k8h3': 3, 'od8p1jr67ydgz315': 1, '3shpx9zdue7dmkfh': 5}
exp_ip_hashes_props_dict = {'se7kimaanzn2l1nt': 0.55, '1kwbloqrfe26k8h3': 0.15, 'od8p1jr67ydgz315': 0.05, '3shpx9zdue7dmkfh': 0.25}
exp_ip_hashes_country_code_dict = {'se7kimaanzn2l1nt': 703, '1kwbloqrfe26k8h3': 688, 'od8p1jr67ydgz315': 616, '3shpx9zdue7dmkfh': 250}
exp_ip_hashes_shared_props_dict = {}
exp_prop_shared_ip_hashes = cons.shared_entities_dict['ip']
exp_n_ip_hashes = cons.unittest_n_entities
exp_lam = cons.poisson_lambda_params['ip']

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)
ip_object = Ip(n_ip_hashes=exp_n_ip_hashes)

obs_ip_hashes_cnts_dict = ip_object.ip_hashes_cnts_dict
obs_ip_hashes_props_dict = ip_object.ip_hashes_props_dict
obs_ip_hashes_country_code_dict = ip_object.ip_hashes_country_code_dict
obs_ip_hashes_shared_props_dict = ip_object.ip_hashes_shared_props_dict
obs_prop_shared_ip_hashes = ip_object.prop_shared_ip_hashes
obs_lam = ip_object.lam
obs_n_ip_hashes = ip_object.n_ip_hashes

class Test_Ip(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_ip_hashes_cnts_dict = exp_ip_hashes_cnts_dict
        self.obs_ip_hashes_cnts_dict = obs_ip_hashes_cnts_dict
        self.exp_ip_hashes_props_dict = exp_ip_hashes_props_dict
        self.obs_ip_hashes_props_dict = obs_ip_hashes_props_dict
        self.exp_ip_hashes_country_code_dict = exp_ip_hashes_country_code_dict
        self.obs_ip_hashes_country_code_dict = obs_ip_hashes_country_code_dict
        self.exp_ip_hashes_shared_props_dict = exp_ip_hashes_shared_props_dict
        self.obs_ip_hashes_shared_props_dict = obs_ip_hashes_shared_props_dict
        self.exp_prop_shared_ip_hashes = exp_prop_shared_ip_hashes
        self.obs_prop_shared_ip_hashes = obs_prop_shared_ip_hashes
        self.exp_lam = exp_lam
        self.obs_lam = obs_lam
        self.exp_n_ip_hashes = exp_n_ip_hashes
        self.obs_n_ip_hashes = obs_n_ip_hashes
    
    def test_type(self):
        self.assertEqual(type(self.obs_ip_hashes_cnts_dict), type(self.exp_ip_hashes_cnts_dict))
        self.assertEqual(type(self.obs_ip_hashes_props_dict), type(self.exp_ip_hashes_props_dict))
        self.assertEqual(type(self.obs_prop_shared_ip_hashes), type(self.exp_prop_shared_ip_hashes))
        self.assertEqual(type(self.obs_ip_hashes_country_code_dict), type(self.exp_ip_hashes_country_code_dict))
        self.assertEqual(type(self.obs_ip_hashes_shared_props_dict), type(self.exp_ip_hashes_shared_props_dict))
        self.assertEqual(type(self.obs_lam), type(self.exp_lam))
        self.assertEqual(type(self.obs_n_ip_hashes), type(self.exp_n_ip_hashes))

    def test_len(self):
        self.assertEqual(len(self.obs_ip_hashes_cnts_dict), len(self.exp_ip_hashes_cnts_dict))
        self.assertEqual(len(self.obs_ip_hashes_props_dict), len(self.exp_ip_hashes_props_dict))
        self.assertEqual(len(self.obs_ip_hashes_country_code_dict), len(self.exp_ip_hashes_country_code_dict))
        self.assertEqual(len(self.obs_ip_hashes_shared_props_dict), len(self.exp_ip_hashes_shared_props_dict))

    def test_keys(self):
        self.assertEqual(list(self.obs_ip_hashes_cnts_dict.keys()), list(self.exp_ip_hashes_cnts_dict.keys()))
        self.assertEqual(list(self.obs_ip_hashes_props_dict.keys()), list(self.exp_ip_hashes_props_dict.keys()))
        self.assertEqual(list(self.obs_ip_hashes_country_code_dict.keys()), list(self.exp_ip_hashes_country_code_dict.keys()))
        self.assertEqual(list(self.obs_ip_hashes_shared_props_dict.keys()), list(self.exp_ip_hashes_shared_props_dict.keys()))

    def test_values(self):
        self.assertEqual(list(self.obs_ip_hashes_cnts_dict.values()), list(self.exp_ip_hashes_cnts_dict.values()))
        self.assertEqual(list(self.obs_ip_hashes_props_dict.values()), list(self.exp_ip_hashes_props_dict.values()))
        self.assertEqual(list(self.obs_ip_hashes_country_code_dict.values()), list(self.exp_ip_hashes_country_code_dict.values()))
        self.assertEqual(list(self.obs_ip_hashes_shared_props_dict.values()), list(self.exp_ip_hashes_shared_props_dict.values()))

    def test_object(self):
        self.assertEqual(self.obs_ip_hashes_cnts_dict, self.exp_ip_hashes_cnts_dict)
        self.assertEqual(self.obs_ip_hashes_props_dict, self.exp_ip_hashes_props_dict)
        self.assertEqual(self.obs_prop_shared_ip_hashes, self.exp_prop_shared_ip_hashes)
        self.assertEqual(self.obs_ip_hashes_country_code_dict, self.exp_ip_hashes_country_code_dict)
        self.assertEqual(self.obs_ip_hashes_shared_props_dict, self.exp_ip_hashes_shared_props_dict)
        self.assertEqual(self.obs_lam, self.exp_lam)
        self.assertEqual(self.obs_n_ip_hashes, self.exp_n_ip_hashes)


if __name__ == "__main__":
    unittest.main()
