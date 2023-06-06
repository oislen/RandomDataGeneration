import unittest
import os
import sys
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

from utilities.gen_random_poisson_sq import gen_random_poisson_sq

np.random.seed(42)

exp_random_poisson = np.array([5, 7, 1, 1])
obs_random_poisson = gen_random_poisson_sq(lam = 1, size = 4)

class Test_gen_random_poisson_sq(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_random_poisson = exp_random_poisson
        self.obs_random_poisson = obs_random_poisson

    def test_type(self):
        self.assertEqual(type(self.obs_random_poisson), type(self.exp_random_poisson))

    def test_shape(self):
        self.assertEqual(self.obs_random_poisson.shape, self.exp_random_poisson.shape)

    def test_object(self):
        self.assertTrue((self.obs_random_poisson == self.exp_random_poisson).all())


if __name__ == "__main__":
    unittest.main()
