import random
import numpy as np
import cons

def gen_trans_status(series, rejection_rates_dict):
    """"""
    # set country code columns
    country_code_columns = ['registration_country_code', 'ip_country_code', 'card_country_code']
    # add rejections based on crime rates within country codes
    if rejection_rates_dict['country_code_trans_reject_rate_dict'][np.random.choice(a = series[country_code_columns].dropna().to_list(), size = 1)[0]] >= random.uniform(0,1):
        status = 'rejected'
    # add rejections based on domain frequencies
    elif rejection_rates_dict['domain_email_trans_reject_rate_dict'][series['email_domain']] >= random.uniform(0,1):
        status = 'rejected'
    # add rejections based on inconsistent country codes
    elif cons.data_model_inconsistent_country_codes_rejection_rate[series[country_code_columns].dropna().nunique()] >= random.uniform(0,1):
        status = 'rejected'
    # add rejections based on shared ips, cards and devices
    elif series['device_hash'] == series['device_hash'] and rejection_rates_dict['shared_devices_reject_rate_dict'][series['device_hash']] >= random.uniform(0,1):
        status = 'rejected'
    elif series['ip_hash'] == series['ip_hash'] and rejection_rates_dict['shared_ips_reject_rate_dict'][series['ip_hash']] >= random.uniform(0,1):
        status = 'rejected'
    elif series['card_hash'] == series['card_hash'] and rejection_rates_dict['shared_cards_reject_rate_dict'][series['card_hash']] >= random.uniform(0,1):
        status = 'rejected'
    # add rejections based on counts of devices, ips and cards
    elif rejection_rates_dict['count_devices_reject_rate_dict'][series['userid']] >= random.uniform(0,1):
        status = 'rejected'
    elif rejection_rates_dict['count_ips_reject_rate_dict'][series['userid']] >= random.uniform(0,1):
        status = 'rejected'
    elif rejection_rates_dict['count_cards_reject_rate_dict'][series['userid']] >= random.uniform(0,1):
        status = 'rejected'
    # otherwise return successful status
    else:
        status = series['transaction_status']
    return status