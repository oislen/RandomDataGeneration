import numpy as np
from utilities.gen_ranom_hash import gen_random_hash
from utilities.gen_random_id import gen_random_id
from utilities.random_poisson_sq import random_poisson_sq


def gen_idhash_cnt_dict(idhash_type, n, lam, nbytes=16):
    """Generates a dictionary of n random idhashes and assoicated counts

    Parameters
    ----------
    idhash_type : str
        Whether to generate a "id2 or "hash" value
    n : int
        The total number of idhash values to generate
    lam : float
        The lambda value to sample n poisson count values with
    nbytes : int
        The number bytes to include in the idhash value

    Returns
    -------
    dict
        A dictionary of idhashes counts
    """
    # if generating a random hash value
    if idhash_type == "hash":
        idhash_list = gen_random_hash(size=n, nbytes=nbytes)
    # else if generating a random id value
    elif idhash_type == "id":
        idhash_list = gen_random_id(size=n, nbytes=nbytes)
    # randomly sample n counts from a squared poisson distribution with given lam value
    cnts_list = list(random_poisson_sq(lam=lam, size=n))
    # return a dictionary of idhashes and counts
    idhash_dict = dict(zip(idhash_list, cnts_list))
    return idhash_dict
