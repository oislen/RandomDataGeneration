from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_country_codes import gen_country_codes

class Ip():

    def __init__(self, n_ip_hashes):
        self.n_ip_hashes = n_ip_hashes
        self.ip_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_ip_hashes)
        self.ip_hashes_props_dict = cnt2prop_dict(self.ip_hashes_cnts_dict)
        self.ip_hashes_country_code_dict = gen_country_codes(self.ip_hashes_cnts_dict)