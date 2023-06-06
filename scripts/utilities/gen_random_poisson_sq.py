import numpy as np


def gen_random_poisson_sq(lam, size):
    """Generates data from a square random poisson variable

    Parameters
    ----------
    lam : int
        The lambda of the underyling poisson random variable
    size : int
        The number of values to generate

    Returns
    -------
    numpy.ndarray
        The random squared poisson values
    """
    # randomly generate a square poisson distribution
    a = np.random.poisson(lam, size) ** 2 + np.random.poisson(lam, size) + 1
    return a
