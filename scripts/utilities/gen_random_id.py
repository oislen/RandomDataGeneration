import string
import numpy as np

def gen_random_id(size, nbytes = 16):
    """"""
    digits = list(string.digits)
    random_ids = []
    for i in range(size):
        random_id = int(''.join(np.random.choice(a = digits, size = nbytes, replace = True)))
        random_ids.append(random_id)
    return random_ids
    