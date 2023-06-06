import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict

random.seed(42)
np.random.seed(42)

exp_id_dict = {
    "6374692674377254": 4,
    "1751409580926382": 5,
    "4264861381989413": 2,
    "6720317315593519": 10,
}
exp_hash_dict = {
    "o68n07nag7yyw4r6": 1,
    "87bxwmnylqy0yd20": 3,
    "4pdq8eepcvv3tmes": 2,
    "zcv6lr15rrjtarow": 1,
}
obs_id_dict = gen_idhash_cnt_dict(idhash_type="id", n=4, lam=1, nbytes=16)
obs_hash_dict = gen_idhash_cnt_dict(idhash_type="hash", n=4, lam=1, nbytes=16)


class Test_gen_idhash_cnt_dict(unittest.TestCase):
    """"""

    def setUp(self):
        self.obs_id_dict = obs_id_dict
        self.exp_id_dict = exp_id_dict
        self.obs_hash_dict = obs_hash_dict
        self.exp_hash_dict = exp_hash_dict

    def test_type(self):
        self.assertEqual(type(self.obs_id_dict), type(self.exp_id_dict))
        self.assertEqual(type(self.obs_hash_dict), type(self.exp_hash_dict))

    def test_len(self):
        self.assertEqual(len(self.obs_id_dict), len(self.exp_id_dict))
        self.assertEqual(len(self.obs_hash_dict), len(self.exp_hash_dict))

    def test_keys(self):
        self.assertEqual(list(self.obs_id_dict.keys()), list(self.exp_id_dict.keys()))
        self.assertEqual(
            list(self.obs_hash_dict.keys()), list(self.exp_hash_dict.keys())
        )

    def test_values(self):
        self.assertEqual(
            list(self.obs_id_dict.values()), list(self.exp_id_dict.values())
        )
        self.assertEqual(
            list(self.obs_hash_dict.values()), list(self.exp_hash_dict.values())
        )

    def test_object(self):
        self.assertEqual(self.obs_id_dict, self.exp_id_dict)
        self.assertEqual(self.obs_hash_dict, self.exp_hash_dict)


if __name__ == "__main__":
    unittest.main()
