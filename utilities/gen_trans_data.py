import random
import pandas as pd
import numpy as np
import cons
from utilities.gen_country_codes_map import gen_country_codes_map
from utilities.align_country_codes import align_country_codes

def gen_trans_data(user_data, device_obj, card_obj, ip_obj, transaction_obj, application_obj):
    """"""

    # explode user data to transaction level
    trans_data = user_data.explode('transaction_hash').dropna(subset = ['transaction_hash'])

    # select hashes
    trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.random.choice(x, size = 1)[0] if x != [] else np.nan)
    trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.random.choice(x, size = 1)[0] if x != [] else np.nan)
    trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.random.choice(x, size = 1)[0] if x != [] else np.nan)
    trans_data['application_hash'] = trans_data['application_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
    
    # add shared hashed entities
    # TODO: add probabilities for choosing each shared hashed entity
    shared_ip = np.random.choice(a = trans_data['ip_hash'].unique(), size = int(np.round(trans_data['ip_hash'].nunique() * cons.shared_entities_dict['ip'])))
    shared_card = np.random.choice(a = trans_data['card_hash'].unique(), size = int(np.round(trans_data['card_hash'].nunique() * cons.shared_entities_dict['card'])))
    shared_device = np.random.choice(a = trans_data['device_hash'].unique(), size = int(np.round(trans_data['device_hash'].nunique() * cons.shared_entities_dict['device'])))
    trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['ip'] else x)
    trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: random.choice(shared_card) if random.uniform(0, 1) <= cons.shared_entities_dict['card'] else x)
    trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: random.choice(shared_device) if random.uniform(0, 1) <= cons.shared_entities_dict['device'] else x)
    
    # add type data
    trans_data['device_type'] = trans_data['device_hash'].replace(device_obj.device_hashes_type_dict)
    trans_data['card_type'] = trans_data['card_hash'].replace(card_obj.card_hashes_type_dict)
    # add country code data
    trans_data['card_country_code'] = trans_data['card_hash'].replace(card_obj.card_hashes_country_code_dict)
    trans_data['ip_country_code'] = trans_data['ip_hash'].replace(ip_obj.ip_hashes_country_code_dict)
    # add transaction data
    trans_data['transaction_amount'] = trans_data['application_hash'].replace(application_obj.application_hashes_prices_dict)
    trans_data['payment_channel'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_payment_channel_dict)
    trans_data['transaction_date'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_dates_dict)
    trans_data['transaction_status'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_status_dict)

    # align payment channel with missing card hashes and 0 transaction amounts
    zero_transaction_amount_filter = (trans_data['transaction_amount'] == 0.0)
    missing_card_hash_filter = (trans_data['card_hash'].isnull())
    trans_data.loc[zero_transaction_amount_filter | missing_card_hash_filter, ['payment_channel']] = np.nan
    trans_data.loc[zero_transaction_amount_filter, ['card_hash', 'card_type', 'card_country_code']] = np.nan

    # align country codes for user, ip and card
    # TODO: ensure shared ip and card hashes have consistent country codes
    country_code_columns = ['registration_country_code', 'ip_country_code', 'card_country_code']
    trans_data[country_code_columns] = trans_data[country_code_columns].apply(lambda series: align_country_codes(series), axis = 1)

    # align registration and transaction dates
    date_columns = ['registration_date', 'transaction_date']
    trans_data[date_columns] = trans_data[date_columns].apply(lambda s: s.sort_values().to_list(), result_type = 'expand', axis = 1).copy()

    # map iso numeric country codes to iso alpha country codes
    country_codes_map = gen_country_codes_map()
    trans_data['registration_country_code']  = trans_data['registration_country_code'].replace(country_codes_map)
    trans_data['card_country_code']  = trans_data['card_country_code'].replace(country_codes_map)
    trans_data['ip_country_code']  = trans_data['ip_country_code'].replace(country_codes_map)

    # sort data by transaction date
    trans_data = trans_data.sort_values(by = 'transaction_date').reset_index(drop = True)
    return trans_data