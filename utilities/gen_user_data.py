import numpy as np

def gen_user_data(user_agg_data, device_obj, card_obj, ip_obj, transaction_obj, application_obj):
    """"""
    user_data = user_agg_data.copy()
    user_data['device_hash'] = user_data['n_devices'].apply(lambda x: np.random.choice(a = list(device_obj.device_hashes_props_dict.keys()), p = list(device_obj.device_hashes_props_dict.values()), replace = True, size = x))
    user_data['card_hash'] = user_data['n_cards'].apply(lambda x: np.random.choice(a = list(card_obj.card_hashes_props_dict.keys()), p = list(card_obj.card_hashes_props_dict.values()), replace = True, size = x))
    user_data['ip_hash'] = user_data['n_ips'].apply(lambda x: np.random.choice(a = list(ip_obj.ip_hashes_props_dict.keys()), p = list(ip_obj.ip_hashes_props_dict.values()), replace = True, size = x))
    user_data['transaction_hash'] = user_data['n_transactions'].apply(lambda x: np.random.choice(a = list(transaction_obj.transaction_hashes_props_dict.keys()), p = list(transaction_obj.transaction_hashes_props_dict.values()), replace = False, size = x))
    user_data['application_hash'] = user_data['n_applications'].apply(lambda x: np.random.choice(a = list(application_obj.application_hashes_props_dict.keys()), p = list(application_obj.application_hashes_props_dict.values()), replace = True, size = x))
    drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_applications', 'n_countries', 'n_transactions']
    user_data = user_data.drop(columns = drop_columns)
    return user_data