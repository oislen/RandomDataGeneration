import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from objects.Application import Application

exp_application_hashes_cnts_dict = {'se7kimaanzn2l1nt': 31, '1kwbloqrfe26k8h3': 5, 'od8p1jr67ydgz315': 9, '3shpx9zdue7dmkfh': 6}
exp_application_hashes_prices_dict = {'se7kimaanzn2l1nt': 1.51, '1kwbloqrfe26k8h3': 0.44, 'od8p1jr67ydgz315': 7.63, '3shpx9zdue7dmkfh': 0.32}
exp_application_hashes_props_dict = {'se7kimaanzn2l1nt': 0.6078431372549019, '1kwbloqrfe26k8h3': 0.09803921568627451, 'od8p1jr67ydgz315': 0.17647058823529413, '3shpx9zdue7dmkfh': 0.11764705882352941}
exp_n_application_hashes = cons.unittest_n_entities
exp_lam = cons.data_model_poisson_lambda_params['application']

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)
application_object = Application(n_application_hashes=exp_n_application_hashes)

obs_application_hashes_cnts_dict = application_object.application_hashes_cnts_dict
obs_application_hashes_prices_dict = application_object.application_hashes_prices_dict
obs_application_hashes_props_dict = application_object.application_hashes_props_dict
obs_lam = application_object.lam
obs_n_application_hashes = application_object.n_application_hashes

class Test_Application(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_application_hashes_cnts_dict = exp_application_hashes_cnts_dict
        self.obs_application_hashes_cnts_dict = obs_application_hashes_cnts_dict
        self.exp_application_hashes_props_dict = exp_application_hashes_props_dict
        self.obs_application_hashes_props_dict = obs_application_hashes_props_dict
        self.exp_application_hashes_prices_dict = exp_application_hashes_prices_dict
        self.obs_application_hashes_prices_dict = obs_application_hashes_prices_dict
        self.exp_n_application_hashes = exp_n_application_hashes
        self.obs_n_application_hashes = obs_n_application_hashes
        self.exp_lam = exp_lam
        self.obs_lam = obs_lam
    
    def test_type(self):
        self.assertEqual(type(self.obs_application_hashes_cnts_dict), type(self.exp_application_hashes_cnts_dict))
        self.assertEqual(type(self.obs_application_hashes_props_dict), type(self.exp_application_hashes_props_dict))
        self.assertEqual(type(self.obs_application_hashes_prices_dict), type(self.exp_application_hashes_prices_dict))
        self.assertEqual(type(self.obs_n_application_hashes), type(self.exp_n_application_hashes))
        self.assertEqual(type(self.obs_lam), type(self.exp_lam))

    def test_len(self):
        self.assertEqual(len(self.obs_application_hashes_props_dict), len(self.exp_application_hashes_props_dict))
        self.assertEqual(len(self.obs_application_hashes_cnts_dict), len(self.exp_application_hashes_cnts_dict))
        self.assertEqual(len(self.obs_application_hashes_prices_dict), len(self.exp_application_hashes_prices_dict))

    def test_keys(self):
        self.assertEqual(list(self.obs_application_hashes_props_dict.keys()), list(self.exp_application_hashes_props_dict.keys()))
        self.assertEqual(list(self.obs_application_hashes_cnts_dict.keys()), list(self.exp_application_hashes_cnts_dict.keys()))
        self.assertEqual(list(self.obs_application_hashes_prices_dict.keys()), list(self.exp_application_hashes_prices_dict.keys()))

    def test_values(self):
        self.assertEqual(list(self.obs_application_hashes_props_dict.values()), list(self.exp_application_hashes_props_dict.values()))
        self.assertEqual(list(self.obs_application_hashes_cnts_dict.values()), list(self.exp_application_hashes_cnts_dict.values()))
        self.assertEqual(list(self.obs_application_hashes_prices_dict.values()), list(self.exp_application_hashes_prices_dict.values()))

    def test_object(self):
        self.assertEqual(self.obs_application_hashes_cnts_dict, self.exp_application_hashes_cnts_dict)
        self.assertEqual(self.obs_application_hashes_props_dict, self.exp_application_hashes_props_dict)
        self.assertEqual(self.obs_application_hashes_prices_dict, self.exp_application_hashes_prices_dict)
        self.assertEqual(self.obs_n_application_hashes, self.exp_n_application_hashes)
        self.assertEqual(self.obs_lam, self.exp_lam)


if __name__ == "__main__":
    unittest.main()
