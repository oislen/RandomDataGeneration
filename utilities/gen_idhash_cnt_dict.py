import numpy as np
from utilities.gen_ranom_hash import gen_random_hash
from utilities.gen_random_id import gen_random_id

def gen_idhash_cnt_dict(idhash_type, n = 1000):
    """"""
    idhash_dict = {}
    for i in range(n):
        if idhash_type == 'hash':
            idhash = gen_random_hash(size = 1, nbytes = 16)[0]
        elif idhash_type == 'id':
            idhash = gen_random_id(size = 1, nbytes = 16)[0]
        idhash_dict[idhash] = np.random.poisson(lam = 20, size = 1)[0]
    return idhash_dict