import os
from multiprocessing import Pool


def multiprocess(func, args, ncpu=os.cpu_count()):
    """Generates a dictionary of random dates for an input dictionary of idhashes counts

    Parameters
    ----------
    func : <class 'function'>
        The function to be executed in parallel
    args : list
        The input parameters as a list of tuples to be passed with the function in parallel
    ncpu : int
        The number of cpus to execute across

    Returns
    -------
    list
        A list of output returned from the func calls ran in parallel
    """
    # initialize a pool of ncpus
    pool = Pool(ncpu)
    # execution given function and arguments across pool of ncpus
    results = pool.starmap(func, args)
    # close pool of ncpus
    pool.close()
    return results
