from utilities.gen_hash_dict import gen_hash_dict
from utilities.cnt2prop_dict import cnt2prop_dict

class Ip():

    def __init__(self, n_ip_hashes):
        self.n_ip_hashes = n_ip_hashes
        self.ip_hashes_cnts_dict = gen_hash_dict(n_hashes = self.n_ip_hashes)
        self.ip_hashes_props_dict = cnt2prop_dict(self.ip_hashes_cnts_dict)