import unittest
import os
import sys
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "generator"))

import cons
from utilities.gen_dates_dict import gen_dates_dict

np.random.seed(cons.unittest_seed)

cnt_data = {"a": 1, "b": 2, "c": 3, "d": 4}
exp_prop_dict = {
    "a": np.datetime64("2020-04-12T00:00:00.000000000"),
    "b": np.datetime64("2021-03-11T00:00:00.000000000"),
    "c": np.datetime64("2020-09-27T00:00:00.000000000"),
    "d": np.datetime64("2020-04-16T00:00:00.000000000"),
}
obs_prop_dict = gen_dates_dict(cnt_data, start_date="2020-01-01", end_date="2021-12-31")


class Test_gen_dates_dict(unittest.TestCase):
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
