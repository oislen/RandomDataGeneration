import pandas as pd
import numpy as np
from utilities.gen_random_poisson_sq import gen_random_poisson_sq

def gen_user_agg_data(user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj):
    """"""
    n_users = user_obj.n_user_ids
    user_agg_data = pd.DataFrame()
    user_agg_data['uid'] = np.random.choice(a = list(user_obj.user_ids_props_dict.keys()), size = n_users, replace = False)
    user_agg_data['n_devices'] = gen_random_poisson_sq(lam = device_obj.lam, size = n_users)
    user_agg_data['n_cards'] = gen_random_poisson_sq(lam = card_obj.lam, size = n_users)
    user_agg_data['n_ips'] = gen_random_poisson_sq(lam = ip_obj.lam, size = n_users)
    user_agg_data['n_transactions'] = gen_random_poisson_sq(lam = transaction_obj.lam, size = n_users)
    user_agg_data['n_applications'] = gen_random_poisson_sq(lam = application_obj.lam, size = n_users)
    return user_agg_data