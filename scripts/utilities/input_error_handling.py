def input_error_handling(input_params_dict):
    """"""
    if not input_params_dict['factor'] > 0:
        raise ValueError(f"Invalid factor parameter value {input_params_dict['factor']}; must be a float > 0.")
    if not input_params_dict['randomseed'] in (0, 1):
        raise ValueError(f"Invalid randomseed parameter value {input_params_dict['randomseed']}; must be either 0 or 1.")
    if not input_params_dict['nitr'] >= 1:
        raise ValueError(f"Invalid nitr parameter value {input_params_dict['nitr']}; must be an integer >= 1.")
    return 0