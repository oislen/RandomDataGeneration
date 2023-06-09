import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from objects.Transaction import Transaction

exp_transaction_hashes_cnts_dict = {'se7kimaanzn2l1nt': 43, '1kwbloqrfe26k8h3': 7, 'od8p1jr67ydgz315': 9, '3shpx9zdue7dmkfh': 88}
exp_transaction_hashes_props_dict = {'se7kimaanzn2l1nt': 0.2925170068027211, '1kwbloqrfe26k8h3': 0.047619047619047616, 'od8p1jr67ydgz315': 0.061224489795918366, '3shpx9zdue7dmkfh': 0.5986394557823129}
exp_transaction_hashes_payment_channel_dict = {'se7kimaanzn2l1nt': 'adyen', '1kwbloqrfe26k8h3': 'worldpay', 'od8p1jr67ydgz315': 'adyen', '3shpx9zdue7dmkfh': 'paypal'}
exp_transaction_hashes_status_dict = {'se7kimaanzn2l1nt': 'successful', '1kwbloqrfe26k8h3': 'successful', 'od8p1jr67ydgz315': 'successful', '3shpx9zdue7dmkfh': 'successful'}
exp_payment_channels = cons.data_model_payment_channels
exp_transaction_status = cons.data_model_transaction_status
exp_rejection_codes = cons.data_model_rejection_codes
exp_n_transaction_hashes = cons.unittest_n_entities
exp_start_date = cons.programme_parameters_transaction_start_date
exp_end_date = cons.programme_parameters_transaction_end_date
exp_lam = cons.data_model_poisson_lambda_params['transaction']

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)
transaction_object = Transaction(exp_n_transaction_hashes, exp_start_date, exp_end_date)

obs_transaction_hashes_cnts_dict = transaction_object.transaction_hashes_cnts_dict
obs_transaction_hashes_props_dict = transaction_object.transaction_hashes_props_dict
obs_transaction_hashes_payment_channel_dict = transaction_object.transaction_hashes_payment_channel_dict
obs_transaction_hashes_status_dict = transaction_object.transaction_hashes_status_dict
obs_payment_channels = transaction_object.payment_channels
obs_transaction_status = transaction_object.transaction_status
obs_rejection_codes = transaction_object.rejection_codes
obs_start_date = transaction_object.start_date
obs_end_date = transaction_object.end_date
obs_n_transaction_hashes = transaction_object.n_transaction_hashes
obs_lam = transaction_object.lam

class Test_Transaction(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_transaction_hashes_cnts_dict = exp_transaction_hashes_cnts_dict
        self.obs_transaction_hashes_cnts_dict = obs_transaction_hashes_cnts_dict
        self.exp_transaction_hashes_props_dict = exp_transaction_hashes_props_dict
        self.obs_transaction_hashes_props_dict = obs_transaction_hashes_props_dict
        self.exp_transaction_hashes_payment_channel_dict = exp_transaction_hashes_payment_channel_dict
        self.obs_transaction_hashes_payment_channel_dict = obs_transaction_hashes_payment_channel_dict
        self.exp_transaction_hashes_status_dict = exp_transaction_hashes_status_dict
        self.obs_transaction_hashes_status_dict = obs_transaction_hashes_status_dict
        self.exp_payment_channels = exp_payment_channels
        self.obs_payment_channels = obs_payment_channels
        self.exp_transaction_status = exp_transaction_status
        self.obs_transaction_status = obs_transaction_status
        self.exp_rejection_codes = exp_rejection_codes
        self.obs_rejection_codes = obs_rejection_codes
        self.exp_start_date = exp_start_date
        self.obs_start_date = obs_start_date
        self.exp_end_date = exp_end_date
        self.obs_end_date = obs_end_date
        self.exp_n_transaction_hashes = exp_n_transaction_hashes
        self.obs_n_transaction_hashes = obs_n_transaction_hashes
        self.exp_lam = exp_lam
        self.obs_lam = obs_lam
    
    def test_type(self):
        self.assertEqual(type(self.obs_transaction_hashes_cnts_dict), type(self.exp_transaction_hashes_cnts_dict))
        self.assertEqual(type(self.obs_transaction_hashes_props_dict), type(self.exp_transaction_hashes_props_dict))
        self.assertEqual(type(self.obs_transaction_hashes_payment_channel_dict), type(self.exp_transaction_hashes_payment_channel_dict))
        self.assertEqual(type(self.obs_transaction_hashes_status_dict), type(self.exp_transaction_hashes_status_dict))
        self.assertEqual(type(self.obs_payment_channels), type(self.exp_payment_channels))
        self.assertEqual(type(self.obs_transaction_status), type(self.exp_transaction_status))
        self.assertEqual(type(self.obs_rejection_codes), type(self.exp_rejection_codes))
        self.assertEqual(type(self.obs_start_date), type(self.exp_start_date))
        self.assertEqual(type(self.obs_end_date), type(self.exp_end_date))
        self.assertEqual(type(self.obs_n_transaction_hashes), type(self.exp_n_transaction_hashes))
        self.assertEqual(type(self.obs_lam), type(self.exp_lam))

    def test_len(self):
        self.assertEqual(len(self.obs_transaction_hashes_cnts_dict), len(self.exp_transaction_hashes_cnts_dict))
        self.assertEqual(len(self.obs_transaction_hashes_props_dict), len(self.exp_transaction_hashes_props_dict))
        self.assertEqual(len(self.obs_transaction_hashes_payment_channel_dict), len(self.exp_transaction_hashes_payment_channel_dict))
        self.assertEqual(len(self.obs_transaction_hashes_status_dict), len(self.exp_transaction_hashes_status_dict))
        self.assertEqual(len(self.obs_payment_channels), len(self.exp_payment_channels))
        self.assertEqual(len(self.obs_transaction_status), len(self.exp_transaction_status))
        self.assertEqual(len(self.obs_rejection_codes), len(self.exp_rejection_codes))

    def test_keys(self):
        self.assertEqual(list(self.obs_transaction_hashes_cnts_dict.keys()), list(self.exp_transaction_hashes_cnts_dict.keys()))
        self.assertEqual(list(self.obs_transaction_hashes_props_dict.keys()), list(self.exp_transaction_hashes_props_dict.keys()))
        self.assertEqual(list(self.obs_transaction_hashes_payment_channel_dict.keys()), list(self.exp_transaction_hashes_payment_channel_dict.keys()))
        self.assertEqual(list(self.obs_transaction_hashes_status_dict.keys()), list(self.exp_transaction_hashes_status_dict.keys()))
        self.assertEqual(list(self.obs_payment_channels.keys()), list(self.exp_payment_channels.keys()))
        self.assertEqual(list(self.obs_transaction_status.keys()), list(self.exp_transaction_status.keys()))
        self.assertEqual(list(self.obs_rejection_codes.keys()), list(self.exp_rejection_codes.keys()))

    def test_values(self):
        self.assertEqual(list(self.obs_transaction_hashes_cnts_dict.values()), list(self.exp_transaction_hashes_cnts_dict.values()))
        self.assertEqual(list(self.obs_transaction_hashes_props_dict.values()), list(self.exp_transaction_hashes_props_dict.values()))
        self.assertEqual(list(self.obs_transaction_hashes_payment_channel_dict.values()), list(self.exp_transaction_hashes_payment_channel_dict.values()))
        self.assertEqual(list(self.obs_transaction_hashes_status_dict.values()), list(self.exp_transaction_hashes_status_dict.values()))
        self.assertEqual(list(self.obs_payment_channels.values()), list(self.exp_payment_channels.values()))
        self.assertEqual(list(self.obs_transaction_status.values()), list(self.exp_transaction_status.values()))
        self.assertEqual(list(self.obs_rejection_codes.values()), list(self.exp_rejection_codes.values()))

    def test_object(self):
        self.assertEqual(self.obs_transaction_hashes_cnts_dict, self.exp_transaction_hashes_cnts_dict)
        self.assertEqual(self.obs_transaction_hashes_props_dict, self.exp_transaction_hashes_props_dict)
        self.assertEqual(self.obs_transaction_hashes_payment_channel_dict, self.exp_transaction_hashes_payment_channel_dict)
        self.assertEqual(self.obs_transaction_hashes_status_dict, self.exp_transaction_hashes_status_dict)
        self.assertEqual(self.obs_payment_channels, self.exp_payment_channels)
        self.assertEqual(self.obs_transaction_status, self.exp_transaction_status)
        self.assertEqual(self.obs_rejection_codes, self.exp_rejection_codes)
        self.assertEqual(self.obs_start_date, self.exp_start_date)
        self.assertEqual(self.obs_end_date, self.exp_end_date)
        self.assertEqual(self.obs_n_transaction_hashes, self.exp_n_transaction_hashes)
        self.assertEqual(self.obs_lam, self.exp_lam)


if __name__ == "__main__":
    unittest.main()
