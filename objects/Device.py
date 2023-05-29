import string
import numpy as np
from utilities.gen_hash_dict import gen_hash_dict
from utilities.cnt2prop_dict import cnt2prop_dict

class Device():

    def __init__(self, n_device_hashes, n_device_types):
        self.n_device_hashes = n_device_hashes
        self.n_device_types = n_device_types
        self.device_hashes_cnts_dict = gen_hash_dict(n_hashes = self.n_device_hashes)
        self.device_hashes_props_dict = cnt2prop_dict(self.device_hashes_cnts_dict)
        self.device_hashes_type_dict = self.gen_device_type(self.device_hashes_cnts_dict, n_device_types = self.n_device_types)
    
    def gen_device_type(self, device_hashes_dict, n_device_types):
        """"""
        device_types_list = []
        letters = list(set(string.ascii_letters.upper()))
        digits = list(string.digits)
        for i in range(n_device_types):
            prefix = ''.join(np.random.choice(letters, size = 3, replace = False))
            suffix = ''.join(np.random.choice(digits, size = 3, replace = False))
            device_type = f'{prefix}-{suffix}'
            device_types_list.append(device_type)
        device_types_dict = {}
        for key, val in device_hashes_dict.items():
            device_types_dict[key] = np.random.choice(a = device_types_list, size = 1)[0]
        return device_types_dict