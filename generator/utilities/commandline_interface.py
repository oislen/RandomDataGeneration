import argparse


def commandline_interface():
    """A commandline interface for parsing input parameters with

    Windows
    python RandomTeleComData\\generator\\main.py --n_users 100 --random_seed 1 --n_itr 2

    Linux
    python3 RandomTeleComData/generator/main.py --n_users 100 --random_seed 1 --n_itr 2

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
    parser.add_argument("--registration_start_date", action="store", dest="registration_start_date", type=str, default="2020-01-01", help="String, the start date for registrations",)
    parser.add_argument("--registration_end_date", action="store", dest="registration_end_date", type=str, default="2020-12-31", help="String, the end date for registrations",)
    parser.add_argument("--transaction_start_date", action="store", dest="transaction_start_date", type=str, default="2021-01-01", help="String, the start date for transactions",)
    parser.add_argument("--transaction_end_date", action="store", dest="transaction_end_date", type=str, default="2021-12-31", help="String, the end date for transactions",)
    # create an output dictionary to hold the results
    input_params_dict = {}
    # extract input arguments
    args = parser.parse_args()
    # map input arguments into output dictionary
    input_params_dict["n_users"] = args.n_users
    input_params_dict["use_random_seed"] = args.use_random_seed
    input_params_dict["n_itr"] = args.n_itr
    input_params_dict["registration_start_date"] = args.registration_start_date
    input_params_dict["registration_end_date"] = args.registration_end_date
    input_params_dict["transaction_start_date"] = args.transaction_start_date
    input_params_dict["transaction_end_date"] = args.transaction_end_date
    return input_params_dict
