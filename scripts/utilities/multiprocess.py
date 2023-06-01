import os
from multiprocessing import Pool

def multiprocess(func, args, ncpu = os.cpu_count()):
    """
    This utility function applyies another function in parallel given a specified number of cpus
    """
    pool = Pool(ncpu)
    results = pool.starmap(func, args)
    pool.close()
    return results