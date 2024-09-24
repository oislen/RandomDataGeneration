import numpy as np
import pandas as pd
import cons
from utilities.gen_random_poisson_power import gen_random_poisson_power

def gen_random_entity_counts(user_obj):
    """
    """
    # create an empty pandas dataframe to hold the random aggregated data
    random_entity_counts = pd.DataFrame()
    # randomly sample from the random user uids
    random_entity_counts['uid'] = np.random.choice(a = list(user_obj.user_ids_props_dict.keys()), size = user_obj.n_user_ids, replace = False)
    # randomly simulate the number of entities per user
    random_entity_counts['n_devices'] = gen_random_poisson_power(lam = cons.data_model_poisson_params["device"]["lambda"], size = user_obj.n_user_ids, power = cons.data_model_poisson_params["device"]["power"])
    random_entity_counts['n_cards'] = gen_random_poisson_power(lam = cons.data_model_poisson_params["card"]["lambda"], size = user_obj.n_user_ids, power = cons.data_model_poisson_params["card"]["power"])
    random_entity_counts['n_ips'] = gen_random_poisson_power(lam = cons.data_model_poisson_params["ip"]["lambda"], size = user_obj.n_user_ids, power = cons.data_model_poisson_params["ip"]["power"])
    random_entity_counts['n_transactions'] = gen_random_poisson_power(lam = cons.data_model_poisson_params["transaction"]["lambda"], size = user_obj.n_user_ids, power = cons.data_model_poisson_params["transaction"]["power"])
    random_entity_counts['n_applications'] = gen_random_poisson_power(lam = cons.data_model_poisson_params["application"]["lambda"], size = user_obj.n_user_ids, power = cons.data_model_poisson_params["application"]["power"])
    return random_entity_counts
