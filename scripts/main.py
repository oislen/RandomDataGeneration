import os
import sys
from time import time
import pandas as pd
__spec__ = None # persist pdb

# set file path for custom python modules
sys.path.append(os.path.join(os.getcwd(), 'scripts'))
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
    # factor = input_params_dict['factor']
    # randomseed = input_params_dict['randomseed']
    # debug_mode = cons.debug_mode
    args = [(input_params_dict['factor'], None if input_params_dict['randomseed'] == 0 else itr, cons.debug_mode) for itr in range(input_params_dict['nitr'])]
    results = multiprocess(func = gen_random_telecom_data, args = args, ncpu = os.cpu_count())
    # concatenate random telecom datasets into a single file
    user_data = pd.concat(objs = [result['user_data'] for result in results], axis = 0, ignore_index = True)
    trans_data = pd.concat(objs = [result['trans_data'] for result in results], axis = 0, ignore_index = True)
    # order results by userid and transaction date ascending
    user_data = user_data.sort_values(by = 'uid').reset_index(drop = True)
    trans_data = trans_data.sort_values(by = 'transaction_date').reset_index(drop = True)
    # end timer
    t1 = time()
    total_runtime_seconds = round(t1 - t0, 2)
    print(f'Total Runtime: {total_runtime_seconds} seconds')

    # print out head and shape of data
    print(f'RandomTeleComUsersData.shape: {user_data.shape}')
    print(f'RandomTeleComTransData.shape: {trans_data.shape}')

    # check output data directories exist
    data_fdirs = [os.path.dirname(cons.fpath_randomtelecomtransdata), os.path.dirname(cons.fpath_randomtelecomusersdata)] 
    for data_fdir in data_fdirs:
        if not os.path.exists(data_fdir):
            os.mkdir(data_fdir)

    # write data to disk
    user_data.to_parquet(cons.fpath_randomtelecomusersdata, engine='fastparquet')
    trans_data.to_csv(cons.fpath_randomtelecomtransdata, index = False)