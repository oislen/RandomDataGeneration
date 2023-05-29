import pandas as pd
import numpy as np

def gen_user_agg_data(user_obj, user_config):
    """"""
    n_users = user_obj.n_user_ids
    user_agg_data = pd.DataFrame()
    user_agg_data['uid'] = np.random.choice(a = list(user_obj.user_ids_props_dict.keys()), size = n_users, replace = False)
    user_agg_data['n_devices'] = np.random.poisson(lam = user_config['lambda']['device'], size = n_users) + 1
    user_agg_data['n_cards'] = np.random.poisson(lam = user_config['lambda']['card'], size = n_users) + 1
    user_agg_data['n_ips'] = np.random.poisson(lam = user_config['lambda']['ip'], size = n_users) + 1
    user_agg_data['n_applications'] = np.random.poisson(lam = user_config['lambda']['application'], size = n_users) + 1
    user_agg_data['n_countries'] = np.random.poisson(lam = user_config['lambda']['country'], size = n_users) + 1
    user_agg_data['n_transactions'] = np.random.poisson(lam = user_config['lambda']['transaction'], size = n_users) + 1
    return user_agg_data