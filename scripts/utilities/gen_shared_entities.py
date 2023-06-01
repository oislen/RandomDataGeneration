import numpy as np
from utilities.cnt2prop_dict import cnt2prop_dict

def gen_shared_entities(cnt_dict, prop_shared_entities):
    """"""
    n_idhashes = len(cnt_dict)
    shared_idhashes_list = list(np.random.choice(a = list(cnt_dict.keys()), size = int(np.round(n_idhashes * prop_shared_entities))))
    shared_idhashes_cnts_dict = {key:cnt_dict[key] for key in shared_idhashes_list}
    shared_idhashes_prop_dict = cnt2prop_dict(shared_idhashes_cnts_dict)
    return shared_idhashes_prop_dict