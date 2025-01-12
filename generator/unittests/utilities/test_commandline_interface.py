import unittest
import os
import sys
import numpy as np
import pandas as pd
import random

sys.path.append(os.path.join(os.getcwd(), "generator"))

import cons
from utilities.commandline_interface import commandline_interface

random.seed(cons.unittest_seed)

if False and __name__ == "__main__":

    obs_input_params_dict = commandline_interface()
    obs_n_users = obs_input_params_dict["n_users"]
    obs_use_random_seed = obs_input_params_dict["use_random_seed"]
    obs_n_itr = obs_input_params_dict["n_itr"]

    exp_n_users = 100
    exp_use_random_seed = 0
    exp_n_itr = 1


    class Test_commandline_interface(unittest.TestCase):
        """"""

        def setUp(self):
            self.obs_n_users = obs_n_users
            self.exp_n_users = exp_n_users
            self.obs_use_random_seed = obs_use_random_seed
            self.exp_use_random_seed = exp_use_random_seed
            self.obs_n_itr = obs_n_itr
            self.exp_n_itr = exp_n_itr

        def test_type(self):
            self.assertEqual(type(self.obs_n_users),type(self.exp_n_users),)
            self.assertEqual(type(self.obs_use_random_seed),type(self.exp_use_random_seed),)
            self.assertEqual(type(self.obs_n_itr), type(self.exp_n_itr))

        def test_object(self):
            self.assertEqual(self.obs_n_users, self.exp_n_users)
            self.assertEqual(self.obs_use_random_seed,self.exp_use_random_seed,)
            self.assertEqual(self.obs_n_itr, self.exp_n_itr)


    unittest.main()
