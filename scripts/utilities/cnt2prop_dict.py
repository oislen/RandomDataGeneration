def cnt2prop_dict(idhash_cnt_dict):
    """"""
    prop_dict = {}
    cnt_total = sum(idhash_cnt_dict.values())
    for key, cnt in idhash_cnt_dict.items():
        prop_dict[key] = cnt / cnt_total
    return prop_dict
