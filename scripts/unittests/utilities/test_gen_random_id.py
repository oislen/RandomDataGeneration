import unittest
import os
import sys
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

from utilities.gen_random_id import gen_random_id

np.random.seed(42)

exp_random_id = ["6374692674377254", "1751409580926382", "4264861381989413", "6720317315593519"]
obs_random_id = gen_random_id(size=4, nbytes=16)

class Test_gen_random_id(unittest.TestCase):
    """"""

    def setUp(self):
        self.obs_random_id = obs_random_id
        self.exp_random_id = exp_random_id

    def test_type(self):
        self.assertEqual(type(self.obs_random_id), type(self.exp_random_id))

    def test_len(self):
        self.assertEqual(len(self.obs_random_id), len(self.exp_random_id))

    def test_object(self):
        self.assertEqual(self.obs_random_id, self.exp_random_id)


if __name__ == "__main__":
    unittest.main()
