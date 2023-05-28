import string
import numpy as np
import secrets

def cnt2prop_dict(cnt_dict):
    """"""
    prop_dict = {}
    cnt_total = sum(cnt_dict.values())
    for key, cnt in cnt_dict.items():
        prop_dict[key] = cnt / cnt_total
    return prop_dict

def gen_device_type(n_device_types = 20):
    """"""
    device_types_dict = {}
    letters = list(set(string.ascii_letters.upper()))
    digits = list(string.digits)
    for i in range(n_device_types):
        prefix = ''.join(np.random.choice(letters, size = 3, replace = False))
        suffix = ''.join(np.random.choice(digits, size = 3, replace = False))
        device_type = f'{prefix}-{suffix}'
        device_types_dict[device_type] = np.random.poisson(lam = 20, size = 1)[0]
    return device_types_dict

def gen_application_hash(n_application_hashes = 1000):
    """"""
    app_hashes_dict = {}
    for i in range(n_application_hashes):
        app_hash = gen_random_hash(size = 1, nbytes = 16)[0]
        app_hashes_dict[app_hash] = np.random.poisson(lam = 20, size = 1)[0]
    return app_hashes_dict

def gen_random_hash(size, nbytes = 16):
    """"""
    random_hashes = []
    for i in range(size):
        random_hashes.append(secrets.token_hex(nbytes = nbytes))
    return random_hashes