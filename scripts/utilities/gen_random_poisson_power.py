import numpy as np


def gen_random_poisson_power(lam, size, power):
    """Generates data from a polynomial random poisson variable to a given power 

    Parameters
    ----------
    lam : int
        The lambda of the underyling poisson random variable
    size : int
        The number of values to generate#
    power : int
        The power of the polynomial sum

    Returns
    -------
    numpy.ndarray
        The random squared poisson values
    """
    # randomly generate a square poisson distribution
    a = np.array([np.random.poisson(lam, size) ** p for p in range(1, power+1)]).sum(axis = 0) + 1
    return a
