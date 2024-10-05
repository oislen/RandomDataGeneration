import unittest
import os
import sys
import random
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)

from utilities.gen_random_entity_counts import gen_random_entity_counts
from utilities.gen_obj_idhash_series import gen_obj_idhash_series
from objects.User import User
from objects.Device import Device

start_date = cons.unittest_registration_start_date
end_date = cons.unittest_registration_end_date
n_user_ids = cons.unittest_n_entities
fpath_firstnames = '.' + cons.fpath_firstnames.split(cons.fpath_repo_dir)[1]
fpath_lastnames = '.' + cons.fpath_lastnames.split(cons.fpath_repo_dir)[1]
fpath_countrieseurope = '.' + cons.fpath_countrieseurope.split(cons.fpath_repo_dir)[1]
fpath_domain_email = '.' + cons.fpath_domain_email.split(cons.fpath_repo_dir)[1]
fpath_smartphones = '.' + cons.fpath_smartphones.split(cons.fpath_repo_dir)[1]

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)

# create user object
user_object = User(n_user_ids=n_user_ids, start_date=start_date, end_date=end_date, fpath_firstnames=fpath_firstnames, fpath_lastnames=fpath_lastnames, fpath_countrieseurope=fpath_countrieseurope, fpath_domain_email=fpath_domain_email)
# generate random entity counts
random_entity_counts = gen_random_entity_counts(user_obj=user_object)
# generate random entity values
device_obj = Device(n_device_hashes=random_entity_counts['n_devices'].sum(), fpath_smartphones=fpath_smartphones)
#  generate user data and device hashes
user_data = random_entity_counts.copy()
obs_obj_idhash_series = gen_obj_idhash_series(idhashes_props_dict=device_obj.device_hashes_props_dict, n_counts_series=user_data['n_devices'])
exp_obj_idhash_series = pd.Series([['2ff23757073a0735'], ['73d2fd828c1fd115'], ['2fc83030d4f37f76', '20f0fba2565dd55c', '257aa14d0bef04bc'], ['f232f0f0bbdcd452']])

class Test_gen_idhash_cnt_dict(unittest.TestCase):
    """"""

    def setUp(self):
        self.obs_obj_idhash_series = obs_obj_idhash_series
        self.exp_obj_idhash_series = exp_obj_idhash_series

    def test_type(self):
        self.assertEqual(type(self.obs_obj_idhash_series), type(self.exp_obj_idhash_series))

    def test_shape(self):
        self.assertEqual(self.obs_obj_idhash_series.shape, self.exp_obj_idhash_series.shape)

    def test_dtypes(self):
        self.assertEqual(self.obs_obj_idhash_series.dtypes, self.exp_obj_idhash_series.dtypes)

    def test_isnull(self):
        self.assertTrue((self.obs_obj_idhash_series.isnull() == self.exp_obj_idhash_series.isnull()).all().all())

    def test_notnull(self):
        self.assertTrue((self.obs_obj_idhash_series.notnull() == self.exp_obj_idhash_series.notnull()).all().all())

    def test_object(self):
        self.assertTrue((self.obs_obj_idhash_series.explode() == self.exp_obj_idhash_series.explode()).all().all())


if __name__ == "__main__":
    unittest.main()
