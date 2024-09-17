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
    # check if the factor parameter is positive
    if not input_params_dict["factor"] > 0:
        raise ValueError(f"Invalid factor parameter value {input_params_dict['factor']}; must be a float > 0.")
    # check if the random seed is either 0 or 1
    if not input_params_dict["randomseed"] in (0, 1):
        raise ValueError(f"Invalid randomseed parameter value {input_params_dict['randomseed']}; must be either 0 or 1.")
    # check if the number of iterations is greater than or equal to 1
    if not input_params_dict["nitr"] >= 1:
        raise ValueError(f"Invalid nitr parameter value {input_params_dict['nitr']}; must be an integer >= 1.")
    return 0
