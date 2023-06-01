import os
import sys
from time import time
import pandas as pd

# set file path for custom python modules
sys.path.append(os.path.join(os.getcwd(), 'RandomTeleComData'))
# import cons
import cons
# load utility functions
from utilities.multiprocess import multiprocess
from utilities.gen_random_telecom_data import gen_random_telecom_data

if __name__ == '__main__':

    # set user parameters
    factor = 0.5
    randomseed = None
    nitr = 1

    # start timer
    t0 = time()
    # generate random telecom data via multiprocess call
    results = multiprocess(func = gen_random_telecom_data, args = [(factor, randomseed) for itr in range(nitr)], ncpu = os.cpu_count())
    # concatenate random telecom datasets into a single file
    trans_data = pd.concat(objs = results, axis = 0, ignore_index = True)
    # end timer
    t1 = time()
    total_runtime_seconds = round(t1 - t0, 2)
    print(f'Total Runtime: {total_runtime_seconds} seconds')

    # print out head and shape of data
    trans_data.head()
    trans_data.shape

    # write data to disk
    trans_data.to_csv(cons.randomtelecomdata_fpath, index = False)