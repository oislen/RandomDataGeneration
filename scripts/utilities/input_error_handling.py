def input_error_handling(input_params_dict):
    """Runs error handling on the input params dictionary

    Parameters
    ----------
    input_params_dict : dict
        A dictionary of input parameters

    Returns
    -------
    int
        Returns 0 for successful completion, otherwise returns value errors depending on failed input parameter check
    """
    # check if the n users parameter is positive
    if not input_params_dict["n_users"] >= 1:
        raise ValueError(f"Invalid n_users parameter value {input_params_dict['n_users']}; must be a integer >= 1.")
    # check if the random seed is either 0 or 1
    if not input_params_dict["use_random_seed"] in (0, 1):
        raise ValueError(f"Invalid random_seed use_random_seed value {input_params_dict['use_random_seed']}; must be either 0 or 1.")
    # check if the number of iterations is greater than or equal to 1
    if not input_params_dict["n_itr"] >= 1:
        raise ValueError(f"Invalid n_itr parameter value {input_params_dict['n_itr']}; must be an integer >= 1.")
    return 0
