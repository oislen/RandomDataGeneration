import numpy as np
import secrets

def gen_random_hash(size, nbytes = 16):
    """"""
    random_hashes = []
    for i in range(size):
        random_hashes.append(secrets.token_hex(nbytes = nbytes))
    return random_hashes

def gen_hash_dict(n_hashes = 1000):
    """"""
    hashes_dict = {}
    for i in range(n_hashes):
        hash = gen_random_hash(size = 1, nbytes = 16)[0]
        hashes_dict[hash] = np.random.poisson(lam = 20, size = 1)[0]
    return hashes_dict

def cnt2prop_dict(cnt_dict):
    """"""
    prop_dict = {}
    cnt_total = sum(cnt_dict.values())
    for key, cnt in cnt_dict.items():
        prop_dict[key] = cnt / cnt_total
    return prop_dict
