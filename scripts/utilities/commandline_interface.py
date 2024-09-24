import argparse


def commandline_interface():
    """A commandline interface for parsing input parameters with

    Windows
    python RandomTeleComData\scripts\main.py --n_users 100 --random_seed 1 --n_itr 2

    Linux
    python3 RandomTeleComData/scripts/main.py --n_users 100 --random_seed 1 --n_itr 2

    Parameters
    ----------

    Returns
    -------
    dict
        A dictionary of key, value pairs where the values are parsed input parameters
    """
    # define argument parser object
    parser = argparse.ArgumentParser(description="Execute Random TeleCom Data Programme.")
    # add input arguments
    parser.add_argument("--n_users", action="store", dest="n_users", type=int, default=100, help="Integer, the number of users to generate random telecom payments data for",)
    parser.add_argument("--use_random_seed", action="store", dest="use_random_seed", type=int, default=0, help="Integer, use a set random seed for reproducible results; must be either 0 or 1",)
    parser.add_argument("--n_itr", action="store", dest="n_itr", type=int, default=1, help="Integer, number of iterations to run",)
    # create an output dictionary to hold the results
    input_params_dict = {}
    # extract input arguments
    args = parser.parse_args()
    # map input arguments into output dictionary
    input_params_dict["n_users"] = args.n_users
    input_params_dict["use_random_seed"] = args.use_random_seed
    input_params_dict["n_itr"] = args.n_itr
    return input_params_dict
