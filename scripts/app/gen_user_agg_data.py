import pandas as pd
import numpy as np
from utilities.gen_random_poisson_sq import gen_random_poisson_sq

def gen_user_agg_data(user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj):
    """Generates random aggregated user level telecom payments data

    Parameters
    ----------
    user_obj : class
        The random user data model object
    device_obj : class
        The random device data model object
    card_obj : class
        The random card data model object
    ip_obj : class
        The random ip data model object
    transaction_obj : class
        The random transaction data model object
    application_obj : class
        The random application data model object

    Returns
    -------
    pandas.DataFrame
        The random aggregated user level telecom payments data
    """
    # create an empty pandas dataframe to hold the random aggregated data
    user_agg_data = pd.DataFrame()
    # extract out the number of users to generate
    n_users = user_obj.n_user_ids
    # randomly sample from the random user uids
    user_agg_data['uid'] = np.random.choice(a = list(user_obj.user_ids_props_dict.keys()), size = n_users, replace = False)
    # randomly simulate the number of entities per user
    user_agg_data['n_devices'] = gen_random_poisson_sq(lam = device_obj.lam, size = n_users)
    user_agg_data['n_cards'] = gen_random_poisson_sq(lam = card_obj.lam, size = n_users)
    user_agg_data['n_ips'] = gen_random_poisson_sq(lam = ip_obj.lam, size = n_users)
    user_agg_data['n_transactions'] = gen_random_poisson_sq(lam = transaction_obj.lam, size = n_users)
    user_agg_data['n_applications'] = gen_random_poisson_sq(lam = application_obj.lam, size = n_users)
    return user_agg_data