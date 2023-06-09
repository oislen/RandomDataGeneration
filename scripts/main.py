import os
import sys
from time import time
import pandas as pd

# set file path for custom python modules
sys.path.append(os.path.join(os.getcwd(), 'RandomTeleComData'))
sys.path.append(os.path.join(os.getcwd(), 'RandomTeleComData', 'scripts'))
# import cons
import cons
# load utility functions
from utilities.commandline_interface import commandline_interface
from utilities.input_error_handling import input_error_handling
from utilities.multiprocess import multiprocess
from app.gen_random_telecom_data import gen_random_telecom_data

if __name__ == '__main__':

    if cons.debug_mode:
        print(f'Debug Mode: {cons.debug_mode}')
        # set user parameters
        input_params_dict = {}
        input_params_dict['factor'] = cons.programme_parameters_factor
        input_params_dict['randomseed'] = cons.programme_parameters_randomseed
        input_params_dict['nitr'] = cons.programme_parameters_nitr
    else:
        input_params_dict = commandline_interface()

    # run input error handling
    res = input_error_handling(input_params_dict)

    print(f'Input Parameters: {input_params_dict}')

    # start timer
    t0 = time()
    # generate random telecom data via multiprocess call
    args = [(input_params_dict['factor'], None if input_params_dict['randomseed'] == 0 else itr) for itr in range(input_params_dict['nitr'])]
    results = multiprocess(func = gen_random_telecom_data, args = args, ncpu = os.cpu_count())
    # concatenate random telecom datasets into a single file
    trans_data = pd.concat(objs = results, axis = 0, ignore_index = True)
    # end timer
    t1 = time()
    total_runtime_seconds = round(t1 - t0, 2)
    print(f'Total Runtime: {total_runtime_seconds} seconds')

    # print out head and shape of data
    print(f'RandomTeleComData.shape: {trans_data.shape}')

    # check output data directory exists
    data_fdir = os.path.dirname(cons.fpath_randomtelecomdata) 
    if not os.path.exists(data_fdir):
        os.mkdir(data_fdir)

    # write data to disk
    trans_data.to_csv(cons.fpath_randomtelecomdata, index = False)