import random
import pandas as pd
import numpy as np
import cons
from utilities.gen_country_codes_map import gen_country_codes_map
from utilities.align_country_codes import align_country_codes
from utilities.gen_trans_error_codes import gen_trans_error_codes

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
    trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.random.choice(a = list(ip_obj.ip_hashes_shared_props_dict.keys()), p = list(ip_obj.ip_hashes_shared_props_dict.values()), size = 1)[0] if random.uniform(0, 1) <= cons.data_model_shared_entities_dict['ip'] else x)
    trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.random.choice(a = list(card_obj.card_hashes_shared_props_dict.keys()), p = list(card_obj.card_hashes_shared_props_dict.values()), size = 1)[0] if random.uniform(0, 1) <= cons.data_model_shared_entities_dict['card'] else x)
    trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.random.choice(a = list(device_obj.device_hashes_shared_props_dict.keys()), p = list(device_obj.device_hashes_shared_props_dict.values()), size = 1)[0] if random.uniform(0, 1) <= cons.data_model_shared_entities_dict['device'] else x)
    # add null rates
    trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.nan if random.uniform(0, 1) <= cons.data_model_null_rates['ip'] else x)
    trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.nan if random.uniform(0, 1) <= cons.data_model_null_rates['card'] else x)
    trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.nan if random.uniform(0, 1) <= cons.data_model_null_rates['device'] else x)
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

    # align payment channel with missing card hashes and 0 transaction amounts
    zero_transaction_amount_filter = (trans_data['transaction_amount'] == 0.0)
    missing_card_hash_filter = (trans_data['card_hash'].isnull())
    trans_data.loc[zero_transaction_amount_filter | missing_card_hash_filter, ['payment_channel']] = np.nan
    trans_data.loc[zero_transaction_amount_filter, ['card_hash', 'card_type', 'card_country_code']] = np.nan
    # align country codes for user, ip and card
    country_code_columns = ['registration_country_code', 'ip_country_code', 'card_country_code']
    trans_data[country_code_columns] = trans_data[country_code_columns].apply(lambda series: align_country_codes(series), axis = 1)
    agg_aligned_ips = trans_data.groupby(by = ['ip_hash', 'ip_country_code'], as_index = False).size().sort_values(by = ['ip_hash', 'ip_country_code'], ascending = [True, False]).drop_duplicates(subset = ['ip_hash'], keep = 'first').drop(columns = ['size'])
    agg_aligned_cards = trans_data.groupby(by = ['card_hash', 'card_country_code'], as_index = False).size().sort_values(by = ['card_hash', 'card_country_code'], ascending = [True, False]).drop_duplicates(subset = ['card_hash'], keep = 'first').drop(columns = ['size'])
    trans_data = pd.merge(left = trans_data.drop(columns = ['ip_country_code']), right = agg_aligned_ips, on = 'ip_hash', how = 'left')
    trans_data = pd.merge(left = trans_data.drop(columns = ['card_country_code']), right = agg_aligned_cards, on = 'card_hash', how = 'left')
    # align registration and transaction dates
    date_columns = ['registration_date', 'transaction_date']
    trans_data[date_columns] = trans_data[date_columns].apply(lambda s: s.sort_values().to_list(), result_type = 'expand', axis = 1).copy()
    # map iso numeric country codes to iso alpha country codes
    country_codes_map = gen_country_codes_map()
    trans_data['registration_country_code']  = trans_data['registration_country_code'].replace(country_codes_map)
    trans_data['card_country_code']  = trans_data['card_country_code'].replace(country_codes_map)
    trans_data['ip_country_code']  = trans_data['ip_country_code'].replace(country_codes_map)

    # TODO: wrap all rejection logic within a single function and call over .apply with lambda
    # create initial transaction status
    trans_data['transaction_status'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_status_dict)
    # add rejections based on crime rates within country codes
    countrieseurope = pd.read_csv(cons.fpath_countrieseurope, usecols = ['ISO numeric', 'ISO alpha 2'])
    countrycrimeindex = pd.read_csv(cons.fpath_countrycrimeindex, usecols = ['country_code', 'crime_index'])
    europecountrycrimeindex = pd.merge(left = countrieseurope, right = countrycrimeindex, left_on = 'ISO alpha 2', right_on = 'country_code', how = 'left')
    europecountrycrimeindex['trans_reject_rate'] = europecountrycrimeindex['crime_index'].divide(europecountrycrimeindex['crime_index'].sum())
    country_code_trans_reject_rate_dict = europecountrycrimeindex.set_index('ISO alpha 2')['trans_reject_rate'].to_dict()
    country_code_columns = ['registration_country_code', 'ip_country_code', 'card_country_code']
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if country_code_trans_reject_rate_dict[np.random.choice(a = series[country_code_columns].dropna().to_list(), size = 1)[0]] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    # add rejections based on domain frequencies
    domain_email = pd.read_csv(cons.fpath_domain_email, usecols = ['domain', 'proportion'])
    domain_email['trans_reject_rate'] = (1 - domain_email['proportion']) / (1 - domain_email['proportion']).sum()
    domain_email_trans_reject_rate_dict = domain_email.set_index('domain')['trans_reject_rate'].to_dict()
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if domain_email_trans_reject_rate_dict[series['email_domain']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    # add rejections based on inconsistent country codes
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if cons.data_model_inconsistent_country_codes_rejection_rate[series[country_code_columns].dropna().nunique()] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    # add rejections based on shared ips, cards and devices
    shared_devices = trans_data.groupby(by = 'device_hash').agg({'userid':'nunique'}).sort_values(by = 'userid')
    shared_ips = trans_data.groupby(by = 'ip_hash').agg({'userid':'nunique'}).sort_values(by = 'userid')
    shared_cards = trans_data.groupby(by = 'card_hash').agg({'userid':'nunique'}).sort_values(by = 'userid')
    shared_devices_reject_rate_dict = shared_devices.divide(shared_devices['userid'].sum()).to_dict()['userid']
    shared_ips_reject_rate_dict = shared_ips.divide(shared_ips['userid'].sum()).to_dict()['userid']
    shared_cards_reject_rate_dict = shared_cards.divide(shared_cards['userid'].sum()).to_dict()['userid']
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if series['device_hash'] == series['device_hash'] and shared_devices_reject_rate_dict[series['device_hash']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if series['ip_hash'] == series['ip_hash'] and shared_ips_reject_rate_dict[series['ip_hash']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if series['card_hash'] == series['card_hash'] and shared_cards_reject_rate_dict[series['card_hash']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    # add rejections based on counts of devices, ips and cards
    count_devices = trans_data.groupby(by = 'userid').agg({'device_hash':'nunique'}).sort_values(by = 'device_hash')
    count_ips = trans_data.groupby(by = 'userid').agg({'ip_hash':'nunique'}).sort_values(by = 'ip_hash')
    count_cards = trans_data.groupby(by = 'userid').agg({'card_hash':'nunique'}).sort_values(by = 'card_hash')
    count_devices_reject_rate_dict = count_devices.divide(count_devices['device_hash'].sum()).to_dict()['device_hash']
    count_ips_reject_rate_dict = count_ips.divide(count_ips['ip_hash'].sum()).to_dict()['ip_hash']
    count_cards_reject_rate_dict = count_cards.divide(count_cards['card_hash'].sum()).to_dict()['card_hash']
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if count_devices_reject_rate_dict[series['userid']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if count_ips_reject_rate_dict[series['userid']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    trans_data['transaction_status'] = trans_data.apply(lambda series: 'rejected' if count_cards_reject_rate_dict[series['userid']] >= random.uniform(0,1) else series['transaction_status'], axis = 1)
    # add transaction status and error codes
    trans_data['transaction_error_code'] = gen_trans_error_codes(trans_data = trans_data, trans_status_col = 'transaction_status', rejection_codes = transaction_obj.rejection_codes)
    
    # sort data by transaction date
    trans_data = trans_data.sort_values(by = 'transaction_date').reset_index(drop = True)
    return trans_data