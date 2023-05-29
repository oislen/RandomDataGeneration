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

def gen_device_type(device_hashes_dict, n_device_types = 20):
    """"""
    device_types_list = []
    letters = list(set(string.ascii_letters.upper()))
    digits = list(string.digits)
    for i in range(n_device_types):
        prefix = ''.join(np.random.choice(letters, size = 3, replace = False))
        suffix = ''.join(np.random.choice(digits, size = 3, replace = False))
        device_type = f'{prefix}-{suffix}'
        device_types_list.append(device_type)
    device_types_dict = {}
    for key, val in device_hashes_dict.items():
        device_types_dict[key] = np.random.choice(a = device_types_list, size = 1)[0]
    return device_types_dict

def gen_hash_dict(n_hashes = 1000):
    """"""
    hashes_dict = {}
    for i in range(n_hashes):
        hash = gen_random_hash(size = 1, nbytes = 16)[0]
        hashes_dict[hash] = np.random.poisson(lam = 20, size = 1)[0]
    return hashes_dict

def gen_application_prices(app_hashes_dict):
    """"""
    app_prices_dict = {}
    for key, val in app_hashes_dict.items():
        app_prices_dict[key] = np.round(np.random.normal(loc = 1, scale = 2, size = 1)[0]**2, 2)
    return app_prices_dict

def gen_random_hash(size, nbytes = 16):
    """"""
    random_hashes = []
    for i in range(size):
        random_hashes.append(secrets.token_hex(nbytes = nbytes))
    return random_hashes