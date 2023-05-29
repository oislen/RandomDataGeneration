import numpy as np
from utilities.gen_ranom_hash import gen_random_hash

def gen_hash_dict(n_hashes = 1000):
    """"""
    hashes_dict = {}
    for i in range(n_hashes):
        hash = gen_random_hash(size = 1, nbytes = 16)[0]
        hashes_dict[hash] = np.random.poisson(lam = 20, size = 1)[0]
    return hashes_dict