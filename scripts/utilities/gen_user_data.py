import numpy as np

def remove_duplicate_idhashes(user_data, idhash):
    """"""
    # take deep copy of the data
    tmp_data = user_data.copy()
    # define duplicate idhash column name
    duplicate_idhash = f'duplicate_{idhash}'
    # explode out the idhashes
    user_transaction_hashes = tmp_data[idhash].explode().rename(duplicate_idhash)
    # identify the duplicate idhashes
    duplicated_user_transaction_hashes = user_transaction_hashes[user_transaction_hashes.duplicated()].reset_index().groupby(by = 'index').agg({duplicate_idhash:list})
    # join duplicated idhashes to temp data
    tmp_data = tmp_data.join(duplicated_user_transaction_hashes, how = 'left')
    # remove duplicate id hashes
    tmp_data[idhash] = tmp_data.apply(lambda s: s[idhash] if not s[duplicate_idhash] == s[duplicate_idhash] else [v for v in s[idhash] if v not in s[duplicate_idhash]], axis = 1)
    # drop duplicate id hashes columns
    tmp_data = tmp_data.drop(columns = [duplicate_idhash])
    return tmp_data

def gen_user_data(user_agg_data, user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj):
    """"""
    user_data = user_agg_data.copy()
    # add user data
    user_data['firstname'] = user_data['uid'].replace(user_obj.user_ids_firstname_dict)
    user_data['lastname'] = user_data['uid'].replace(user_obj.user_ids_lastname_dict)
    user_data['registration_date'] = user_data['uid'].replace(user_obj.user_ids_dates_dict)
    user_data['registration_country_code'] = user_data['uid'].replace(user_obj.user_ids_country_code_dict)
    user_data['email_domain'] = user_data['uid'].replace(user_obj.user_ids_email_domain_dict)
    user_data['userid'] = user_data['registration_date'].dt.year.astype(str) + user_data['registration_country_code'].astype(str) + user_data['uid'].astype(str).str[-9:]
    # add hash data lists
    user_data['device_hash'] = user_data['n_devices'].apply(lambda x: list(np.random.choice(a = list(device_obj.device_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['card_hash'] = user_data['n_cards'].apply(lambda x: list(np.random.choice(a = list(card_obj.card_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['ip_hash'] = user_data['n_ips'].apply(lambda x: list(np.random.choice(a = list(ip_obj.ip_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['transaction_hash'] = user_data['n_transactions'].apply(lambda x: list(np.random.choice(a = list(transaction_obj.transaction_hashes_props_dict.keys()), replace = False, size = x)))
    user_data['application_hash'] = user_data['n_applications'].apply(lambda x: list(np.random.choice(a = list(application_obj.application_hashes_props_dict.keys()), p = list(application_obj.application_hashes_props_dict.values()), replace = True, size = x)))
    # remove duplicate idhashes
    user_data = remove_duplicate_idhashes(user_data, idhash = 'device_hash')
    user_data = remove_duplicate_idhashes(user_data, idhash = 'card_hash')
    user_data = remove_duplicate_idhashes(user_data, idhash = 'ip_hash')
    user_data = remove_duplicate_idhashes(user_data, idhash = 'transaction_hash')
    # drop excess columns
    drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_applications', 'n_transactions']
    user_data = user_data.drop(columns = drop_columns)
    return user_data