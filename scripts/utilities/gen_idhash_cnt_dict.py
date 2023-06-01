import numpy as np
from utilities.gen_ranom_hash import gen_random_hash
from utilities.gen_random_id import gen_random_id
from utilities.random_poisson import random_poisson

def gen_idhash_cnt_dict(idhash_type, n, lam, nbytes = 16):
    """"""
    if idhash_type == 'hash':
        idhash_list = gen_random_hash(size = n, nbytes = nbytes)
    elif idhash_type == 'id':
        idhash_list = gen_random_id(size = n, nbytes = nbytes)
    cnts_list = list(random_poisson(lam = lam, size = n))
    idhash_dict = dict(zip(idhash_list, cnts_list))
    return idhash_dict