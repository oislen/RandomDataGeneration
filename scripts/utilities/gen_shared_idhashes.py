import numpy as np
from utilities.cnt2prop_dict import cnt2prop_dict


def gen_shared_idhashes(idhash_cnt_dict, prop_shared_idhashes):
    """Generates a dictionary of shared idhashes proportions

    Parameters
    ----------
    idhashes_cnts_dict : dict
        A dictionary of idhashes counts
    prop_shared_idhashes : float
        The total proportion of shared idhashes

    Returns
    -------
    dict
        A dictionary of shared idhashes proportion
    """
    # calculate the total number of idhashes
    n_idhashes = len(idhash_cnt_dict)
    # randomly sample the idhashes based on the total proportion of shared idhashes
    shared_idhashes_list = list(
        np.random.choice(
            a=list(idhash_cnt_dict.keys()),
            size=int(np.round(n_idhashes * prop_shared_idhashes)),
        )
    )
    # subset the idhashes counts dictionary based on the shared idhashes
    shared_idhashes_cnts_dict = {
        key: idhash_cnt_dict[key] for key in shared_idhashes_list
    }
    # convert the shared idhashes counts to proportions
    shared_idhashes_prop_dict = cnt2prop_dict(shared_idhashes_cnts_dict)
    return shared_idhashes_prop_dict
