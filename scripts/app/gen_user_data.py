import pandas as pd
import numpy as np
from utilities.gen_random_poisson_power import gen_random_poisson_power
from utilities.remove_duplicate_idhashes import remove_duplicate_idhashes

def gen_user_data(user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj):
    """Generates random user level telecom payments data

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
        The random user level telecom payments data
    """
    # create an empty pandas dataframe to hold the random aggregated data
    user_agg_data = pd.DataFrame()
    # extract out the number of users to generate
    n_users = user_obj.n_user_ids
    # randomly sample from the random user uids
    user_agg_data['uid'] = np.random.choice(a = list(user_obj.user_ids_props_dict.keys()), size = n_users, replace = False)
    # randomly simulate the number of entities per user
    user_agg_data['n_devices'] = gen_random_poisson_power(lam = device_obj.lam, size = n_users, power = 1)
    user_agg_data['n_cards'] = gen_random_poisson_power(lam = card_obj.lam, size = n_users, power = 1)
    user_agg_data['n_ips'] = gen_random_poisson_power(lam = ip_obj.lam, size = n_users, power = 2)
    user_agg_data['n_transactions'] = gen_random_poisson_power(lam = transaction_obj.lam, size = n_users, power = 3)
    user_agg_data['n_applications'] = gen_random_poisson_power(lam = application_obj.lam, size = n_users, power = 2)
    user_data = user_agg_data.copy()
    # add user data
    user_data['firstname'] = user_data['uid'].replace(user_obj.user_ids_firstname_dict)
    user_data['lastname'] = user_data['uid'].replace(user_obj.user_ids_lastname_dict)
    user_data['registration_date'] = user_data['uid'].replace(user_obj.user_ids_dates_dict)
    user_data['registration_country_code'] = user_data['uid'].replace(user_obj.user_ids_country_code_dict)
    user_data['email_domain'] = user_data['uid'].replace(user_obj.user_ids_email_domain_dict)
    userid_date_country_code = user_data['registration_date'].dt.strftime('%Y%m%d') + user_data['registration_country_code'].astype(str)
    zero_pad = (userid_date_country_code.str.len() - 11).abs().apply(lambda x: '0'*x)
    user_data['userid'] = userid_date_country_code + zero_pad + user_data['uid'].astype(str).str[-5:]
    # add hash data lists
    user_data['device_hash'] = user_data['n_devices'].apply(lambda x: list(np.random.choice(a = list(device_obj.device_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['card_hash'] = user_data['n_cards'].apply(lambda x: list(np.random.choice(a = list(card_obj.card_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['ip_hash'] = user_data['n_ips'].apply(lambda x: list(np.random.choice(a = list(ip_obj.ip_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['transaction_hash'] = user_data['n_transactions'].apply(lambda x: list(np.random.choice(a = list(transaction_obj.transaction_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['application_hash'] = user_data['n_applications'].apply(lambda x: list(np.random.choice(a = list(application_obj.application_hashes_props_dict.keys()), p = list(application_obj.application_hashes_props_dict.values()), replace = True, size = x)))
    # remove duplicate idhashes
    user_data = remove_duplicate_idhashes(user_data, idhash_col = 'device_hash')
    user_data = remove_duplicate_idhashes(user_data, idhash_col = 'card_hash')
    user_data = remove_duplicate_idhashes(user_data, idhash_col = 'ip_hash')
    user_data = remove_duplicate_idhashes(user_data, idhash_col = 'transaction_hash')
    # drop excess columns
    drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_applications', 'n_transactions']
    user_data = user_data.drop(columns = drop_columns)
    return user_data