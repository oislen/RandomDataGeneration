import os
import sys
import unittest
import random
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from app.ProgrammeParams import ProgrammeParams
from app.gen_user_data import gen_user_data
from app.gen_trans_data import gen_trans_data
from objects.Application import Application
from objects.Card import Card
from objects.Device import Device
from objects.Ip import Ip
from objects.Transaction import Transaction
from objects.User import User

# initalise programme parameters
programmeparams = ProgrammeParams(
    factor=cons.programme_parameters_factor,
    randomseed=cons.programme_parameters_randomseed,
    debug_mode=cons.unittest_debug_mode,
)

# set random seed
random.seed(programmeparams.randomseed)
np.random.seed(seed=programmeparams.randomseed)

# generate random data model objects
application_obj = Application(n_application_hashes=programmeparams.n_applications)
card_obj = Card(n_card_hashes=programmeparams.n_cards)
device_obj = Device(
    n_device_hashes=programmeparams.n_devices,
    n_device_types=programmeparams.n_device_types,
)
ip_obj = Ip(n_ip_hashes=programmeparams.n_ips)
transaction_obj = Transaction(
    n_transaction_hashes=programmeparams.n_transactions,
    start_date=programmeparams.transaction_start_date,
    end_date=programmeparams.transaction_end_date,
)
user_obj = User(
    n_user_ids=programmeparams.n_users,
    start_date=programmeparams.registration_start_date,
    end_date=programmeparams.registration_end_date,
)

# generate expected user and transaction level data
obs_user_data = gen_user_data(
    user_obj=user_obj,
    device_obj=device_obj,
    card_obj=card_obj,
    ip_obj=ip_obj,
    transaction_obj=transaction_obj,
    application_obj=application_obj,
)
obs_trans_data = gen_trans_data(
    user_data=obs_user_data,
    device_obj=device_obj,
    card_obj=card_obj,
    ip_obj=ip_obj,
    transaction_obj=transaction_obj,
    application_obj=application_obj,
)

# if writing observed data to unittest data directory
if cons.unittest_gen_test_dfs:
    obs_user_data.to_pickle(cons.fpath_unittest_user_data)
    obs_trans_data.to_pickle(cons.fpath_unittest_transaction_data)

# load in expected user level data
exp_user_data = pd.read_pickle(cons.fpath_unittest_user_data)
exp_trans_data = pd.read_pickle(cons.fpath_unittest_transaction_data)


class Test_gen_user_data(unittest.TestCase):
    """"""

    def setUp(self):
        self.obs_user_data = obs_user_data
        self.exp_user_data = exp_user_data
        self.obs_trans_data = obs_trans_data
        self.exp_trans_data = exp_trans_data

    def test_type(self):
        self.assertEqual(type(self.obs_user_data), type(self.exp_user_data))
        self.assertEqual(type(self.obs_trans_data), type(self.exp_trans_data))

    def test_shape(self):
        self.assertEqual(self.obs_user_data.shape, self.exp_user_data.shape)
        self.assertEqual(self.obs_trans_data.shape, self.exp_trans_data.shape)

    def test_dtypes(self):
        self.assertTrue((self.obs_user_data.dtypes == self.exp_user_data.dtypes).all())
        self.assertTrue(
            (self.obs_trans_data.dtypes == self.exp_trans_data.dtypes).all()
        )

    def test_isnull(self):
        self.assertTrue(
            (self.obs_user_data.isnull() == self.exp_user_data.isnull()).all().all()
        )
        self.assertTrue(
            (self.obs_trans_data.isnull() == self.exp_trans_data.isnull()).all().all()
        )

    def test_notnull(self):
        self.assertTrue(
            (self.obs_user_data.notnull() == self.exp_user_data.notnull()).all().all()
        )
        self.assertTrue(
            (self.obs_trans_data.notnull() == self.exp_trans_data.notnull()).all().all()
        )

    def test_object(self):
        self.assertTrue(
            (self.obs_trans_data.fillna(-999.0) == self.exp_trans_data.fillna(-999.0))
            .all()
            .all()
        )


if __name__ == "__main__":
    unittest.main()
