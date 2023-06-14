import unittest
import os
import sys
import random
import numpy as np

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons
from objects.Device import Device

exp_device_hashes_cnts_dict = {
    "63cea7c46926aa74": 1,
    "37725417bd51fb40": 5,
    "b95cb80aae9fbbfe": 1,
    "dded2b63f8242648": 1,
}
exp_device_hashes_props_dict = {
    "63cea7c46926aa74": 0.125,
    "37725417bd51fb40": 0.625,
    "b95cb80aae9fbbfe": 0.125,
    "dded2b63f8242648": 0.125,
}
exp_device_hashes_type_dict = {
    "63cea7c46926aa74": "JDN-204",
    "37725417bd51fb40": "JDN-204",
    "b95cb80aae9fbbfe": "POH-969",
    "dded2b63f8242648": "DVR-772",
}
exp_device_hashes_shared_props_dict = {}
exp_prop_shared_device_hashes = cons.data_model_shared_entities_dict["device"]
exp_n_device_hashes = cons.unittest_n_entities
exp_n_device_types = cons.unittest_n_device_types
exp_lam = cons.data_model_poisson_lambda_params["device"]

random.seed(cons.unittest_seed)
np.random.seed(cons.unittest_seed)
device_object = Device(exp_n_device_hashes, exp_n_device_types)

obs_device_hashes_cnts_dict = device_object.device_hashes_cnts_dict
obs_device_hashes_props_dict = device_object.device_hashes_props_dict
obs_device_hashes_type_dict = device_object.device_hashes_type_dict
obs_device_hashes_shared_props_dict = device_object.device_hashes_shared_props_dict
obs_prop_shared_device_hashes = device_object.prop_shared_device_hashes
obs_n_device_hashes = device_object.n_device_hashes
obs_n_device_types = device_object.n_device_types
obs_lam = device_object.lam


class Test_Device(unittest.TestCase):
    """"""

    def setUp(self):
        self.exp_device_hashes_cnts_dict = exp_device_hashes_cnts_dict
        self.obs_device_hashes_cnts_dict = obs_device_hashes_cnts_dict
        self.exp_device_hashes_props_dict = exp_device_hashes_props_dict
        self.obs_device_hashes_props_dict = obs_device_hashes_props_dict
        self.exp_device_hashes_type_dict = exp_device_hashes_type_dict
        self.obs_device_hashes_type_dict = obs_device_hashes_type_dict
        self.exp_device_hashes_shared_props_dict = exp_device_hashes_shared_props_dict
        self.obs_device_hashes_shared_props_dict = obs_device_hashes_shared_props_dict
        self.exp_prop_shared_device_hashes = exp_prop_shared_device_hashes
        self.obs_prop_shared_device_hashes = obs_prop_shared_device_hashes
        self.exp_n_device_hashes = exp_n_device_hashes
        self.obs_n_device_hashes = obs_n_device_hashes
        self.exp_n_device_types = exp_n_device_types
        self.obs_n_device_types = obs_n_device_types
        self.exp_lam = exp_lam
        self.obs_lam = obs_lam

    def test_type(self):
        self.assertEqual(
            type(self.obs_device_hashes_cnts_dict),
            type(self.exp_device_hashes_cnts_dict),
        )
        self.assertEqual(
            type(self.obs_device_hashes_props_dict),
            type(self.exp_device_hashes_props_dict),
        )
        self.assertEqual(
            type(self.obs_device_hashes_type_dict),
            type(self.exp_device_hashes_type_dict),
        )
        self.assertEqual(
            type(self.obs_device_hashes_shared_props_dict),
            type(self.exp_device_hashes_shared_props_dict),
        )
        self.assertEqual(
            type(self.obs_prop_shared_device_hashes),
            type(self.exp_prop_shared_device_hashes),
        )
        self.assertEqual(type(self.obs_n_device_hashes), type(self.exp_n_device_hashes))
        self.assertEqual(type(self.obs_n_device_types), type(self.exp_n_device_types))
        self.assertEqual(type(self.obs_lam), type(self.exp_lam))

    def test_len(self):
        self.assertEqual(
            len(self.obs_device_hashes_cnts_dict), len(self.exp_device_hashes_cnts_dict)
        )
        self.assertEqual(
            len(self.obs_device_hashes_props_dict),
            len(self.exp_device_hashes_props_dict),
        )
        self.assertEqual(
            len(self.obs_device_hashes_type_dict), len(self.exp_device_hashes_type_dict)
        )
        self.assertEqual(
            len(self.obs_device_hashes_shared_props_dict),
            len(self.exp_device_hashes_shared_props_dict),
        )

    def test_keys(self):
        self.assertEqual(
            list(self.obs_device_hashes_cnts_dict.keys()),
            list(self.exp_device_hashes_cnts_dict.keys()),
        )
        self.assertEqual(
            list(self.obs_device_hashes_props_dict.keys()),
            list(self.exp_device_hashes_props_dict.keys()),
        )
        self.assertEqual(
            list(self.obs_device_hashes_type_dict.keys()),
            list(self.exp_device_hashes_type_dict.keys()),
        )
        self.assertEqual(
            list(self.obs_device_hashes_shared_props_dict.keys()),
            list(self.exp_device_hashes_shared_props_dict.keys()),
        )

    def test_values(self):
        self.assertEqual(
            list(self.obs_device_hashes_cnts_dict.values()),
            list(self.exp_device_hashes_cnts_dict.values()),
        )
        self.assertEqual(
            list(self.obs_device_hashes_props_dict.values()),
            list(self.exp_device_hashes_props_dict.values()),
        )
        self.assertEqual(
            list(self.obs_device_hashes_type_dict.values()),
            list(self.exp_device_hashes_type_dict.values()),
        )
        self.assertEqual(
            list(self.obs_device_hashes_shared_props_dict.values()),
            list(self.exp_device_hashes_shared_props_dict.values()),
        )

    def test_object(self):
        self.assertEqual(
            self.obs_device_hashes_cnts_dict, self.exp_device_hashes_cnts_dict
        )
        self.assertEqual(
            self.obs_device_hashes_props_dict, self.exp_device_hashes_props_dict
        )
        self.assertEqual(
            self.obs_device_hashes_type_dict, self.exp_device_hashes_type_dict
        )
        self.assertEqual(
            self.obs_device_hashes_shared_props_dict,
            self.exp_device_hashes_shared_props_dict,
        )
        self.assertEqual(
            self.obs_prop_shared_device_hashes, self.exp_prop_shared_device_hashes
        )
        self.assertEqual(self.obs_n_device_hashes, self.exp_n_device_hashes)
        self.assertEqual(self.obs_n_device_types, self.exp_n_device_types)
        self.assertEqual(self.obs_lam, self.exp_lam)


if __name__ == "__main__":
    unittest.main()
