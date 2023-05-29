import numpy as np

def gen_trans_data(user_data, device_obj, card_obj, application_obj, transaction_obj):
    """"""
    trans_data = user_data.explode('transaction_hash')
    trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
    trans_data['device_type'] = trans_data['device_hash'].replace(device_obj.device_hashes_type_dict)
    trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
    trans_data['card_type'] = trans_data['card_hash'].replace(card_obj.card_hashes_type_dict)
    trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
    trans_data['application_hash'] = trans_data['application_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
    trans_data['transaction_amount'] = trans_data['application_hash'].replace(application_obj.application_hashes_prices_dict)
    trans_data['payment_channel'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_payment_channel_dict)
    trans_data['transaction_date'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_dates_dict)
    trans_data = trans_data.sort_values(by = 'transaction_date').reset_index(drop = True)
    return trans_data