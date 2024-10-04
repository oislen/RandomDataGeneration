import unittest
import os
import sys
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from utilities.gen_country_codes_dict import gen_country_codes_dict

np.random.seed(cons.unittest_seed)

cnt_data = {"a": 1, "b": 2, "c": 3, "d": 4}
exp_prop_dict = {"a": 276, "b": 756, "c": 642, "d": 826}
fpath_countrieseurope = '.' + cons.fpath_countrieseurope.split(cons.fpath_repo_dir)[1]
obs_prop_dict = gen_country_codes_dict(cnt_data, fpath_countrieseurope=fpath_countrieseurope)

class Test_gen_country_codes_dict(unittest.TestCase):
    """"""

    def setUp(self):
        self.cnt_data = cnt_data
        self.obs_prop_dict = obs_prop_dict
        self.exp_prop_dict = exp_prop_dict

    def test_type(self):
        self.assertEqual(type(self.obs_prop_dict), type(self.exp_prop_dict))

    def test_len(self):
        self.assertEqual(len(self.obs_prop_dict), len(self.exp_prop_dict))

    def test_keys(self):
        self.assertEqual(
            list(self.obs_prop_dict.keys()), list(self.exp_prop_dict.keys())
        )

    def test_values(self):
        self.assertEqual(
            list(self.obs_prop_dict.values()), list(self.exp_prop_dict.values())
        )

    def test_object(self):
        self.assertEqual(self.obs_prop_dict, self.exp_prop_dict)


if __name__ == "__main__":
    unittest.main()
