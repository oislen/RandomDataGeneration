import string
import numpy as np


def gen_random_hash(size, nbytes=16):
    """Generates a list of random hashes

    Parameters
    ----------
    size : int
        The total number of hashes to generate
    nbytes : int
        The number of alphanumeric values in each hash

    Returns
    -------
    list
        A list of random hashes
    """
    # generate a list of digits and lower case letters from string library
    alphanumeric = list(string.digits) + list(string.ascii_lowercase)[:6]
    # randomly sample nbytes digits, string concatenate and convert to integers
    random_hashes = [
        "".join(np.random.choice(a=alphanumeric, size=nbytes, replace=True))
        for i in range(size)
    ]
    return random_hashes
