import secrets


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
    # randomly sample nbytes hashes
    random_hashes = [secrets.token_hex(nbytes=nbytes) for i in range(size)]
    return random_hashes
