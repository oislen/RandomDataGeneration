def cnt2prop_dict(idhash_cnt_dict):
    """Converts a dictionary of counts to a dictionary of proportions

    Parameters
    ----------
    idhash_cnt_dict : dict
        A dictionary of key, value pairs where the value indicates a count

    Returns
    -------
    dict
        A dictionary of key, value pairs where the value indicates a proportion
    """
    # empty dictionary for proportions
    prop_dict = {}
    # sum of dictionary counts
    cnt_total = sum(idhash_cnt_dict.values())
    # iterate over input dictionary and convert counts to proportions
    for idhash, cnt in idhash_cnt_dict.items():
        prop_dict[idhash] = cnt / cnt_total
    return prop_dict
