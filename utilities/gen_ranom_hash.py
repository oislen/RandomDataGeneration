import secrets

def gen_random_hash(size, nbytes = 16):
    """"""
    random_hashes = []
    for i in range(size):
        random_hashes.append(secrets.token_hex(nbytes = nbytes))
    return random_hashes