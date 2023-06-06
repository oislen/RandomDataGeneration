import string
import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_shared_idhashes import gen_shared_idhashes

class Device():

    def __init__(self, n_device_hashes, n_device_types):
        self.n_device_hashes = n_device_hashes
        self.n_device_types = n_device_types
        self.lam = cons.poisson_lambda_params['device']
        self.prop_shared_device_hashes = cons.shared_entities_dict['device']
        self.device_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_device_hashes, lam = self.lam)
        self.device_hashes_props_dict = cnt2prop_dict(self.device_hashes_cnts_dict)
        self.device_hashes_type_dict = self.gen_device_type(self.device_hashes_cnts_dict, n_device_types = self.n_device_types)
        self.device_hashes_shared_props_dict = gen_shared_idhashes(self.device_hashes_cnts_dict, self.prop_shared_device_hashes)
    
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
        device_hashes_list = list(device_hashes_dict.keys())
        device_types_list = list(np.random.choice(a = device_types_list, size = len(device_hashes_list)))
        device_hashes_type_dict = dict(zip(device_hashes_list, device_types_list))
        return device_hashes_type_dict