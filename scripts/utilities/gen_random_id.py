import string
import numpy as np


def gen_random_id(size, nbytes=16):
    """Generates a list of random ids

    Parameters
    ----------
    size : int
        The total number of ids to generate
    nbytes : int
        The number of numeric values in each id

    Returns
    -------
    list
        A list of random ids
    """
    # generate a list of digits from string library
    digits = list(string.digits)
    # randomly sample nbytes digits, string concatenate and convert to integers
    random_ids = [
        "".join(np.random.choice(a=digits, size=nbytes, replace=True))
        for i in range(size)
    ]
    return random_ids
