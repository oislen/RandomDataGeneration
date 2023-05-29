def cnt2prop_dict(cnt_dict):
    """"""
    prop_dict = {}
    cnt_total = sum(cnt_dict.values())
    for key, cnt in cnt_dict.items():
        prop_dict[key] = cnt / cnt_total
    return prop_dict
