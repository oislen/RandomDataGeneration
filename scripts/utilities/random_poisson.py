import numpy as np

def random_poisson(lam, size): 
    a = np.random.poisson(lam, size)**2 + np.random.poisson(lam, size) + 1
    return a