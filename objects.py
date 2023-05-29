import utilities as utl
import numpy as np
import pandas as pd
import string
import pandas as pd
from datetime import datetime

class Device():

    def __init__(self, n_device_hashes, n_device_types):
        self.n_device_hashes = n_device_hashes
        self.n_device_types = n_device_types
        self.device_hashes_cnts_dict = utl.gen_hash_dict(n_hashes = self.n_device_hashes)
        self.device_hashes_props_dict = utl.cnt2prop_dict(self.device_hashes_cnts_dict)
        self.device_hashes_type_dict = self.gen_device_type(self.device_hashes_cnts_dict, n_device_types = self.n_device_types)
    
    def gen_device_type(self, device_hashes_dict, n_device_types):
        """"""
        device_types_list = []
        letters = list(set(string.ascii_letters.upper()))
        digits = list(string.digits)
        for i in range(n_device_types):
            prefix = ''.join(np.random.choice(letters, size = 3, replace = False))
            suffix = ''.join(np.random.choice(digits, size = 3, replace = False))
            device_type = f'{prefix}-{suffix}'
            device_types_list.append(device_type)
        device_types_dict = {}
        for key, val in device_hashes_dict.items():
            device_types_dict[key] = np.random.choice(a = device_types_list, size = 1)[0]
        return device_types_dict

class Application():

    def __init__(self, n_application_hashes):
        self.n_application_hashes = n_application_hashes
        self.application_hashes_cnts_dict = utl.gen_hash_dict(n_hashes = self.n_application_hashes)
        self.application_hashes_props_dict = utl.cnt2prop_dict(self.application_hashes_cnts_dict)
        self.application_hashes_prices_dict = self.gen_application_prices(self.application_hashes_cnts_dict)
    
    def gen_application_prices(self, app_hashes_dict):
        """"""
        app_prices_dict = {}
        for key, val in app_hashes_dict.items():
            app_prices_dict[key] = np.round(np.random.normal(loc = 1, scale = 2, size = 1)[0]**2, 2)
        return app_prices_dict

class Transaction():

    def __init__(self, n_transaction_hashes, start_date, end_date):
        self.n_transaction_hashes = n_transaction_hashes
        self.start_date = start_date
        self.end_date = end_date
        self.payment_channels = {'paypal':0.4, 'adyen':0.3, 'worldpay':0.2, 'docomo':0.1}
        self.transaction_hashes_cnts_dict = utl.gen_hash_dict(n_hashes = self.n_transaction_hashes)
        self.transaction_hashes_props_dict = utl.cnt2prop_dict(self.transaction_hashes_cnts_dict)
        self.transaction_hashes_dates_dict = self.gen_transaction_date(self.transaction_hashes_cnts_dict, start_date = self.start_date, end_date = self.end_date)
        self.transaction_hashes_payment_channel_dict = self.gen_transaction_payment_channel(self.transaction_hashes_cnts_dict, self.payment_channels)

    def gen_transaction_date(self, transaction_hashes_cnts_dict, start_date, end_date):
        """"""
        transaction_hashes_dates_dict = {}
        dates = pd.date_range(datetime.strptime(start_date, '%Y-%m-%d'), datetime.strptime(end_date, '%Y-%m-%d') - pd.Timedelta(days=1),freq='d')
        for key, val in transaction_hashes_cnts_dict.items():
            transaction_hashes_dates_dict[key] = np.random.choice(a = dates, replace = True, size = 1)[0]
        return transaction_hashes_dates_dict

    def gen_transaction_payment_channel(self, transaction_hashes_cnts_dict, payment_channels):
        """"""
        transaction_hashes_payment_channels_dict = {}
        for key, val in transaction_hashes_cnts_dict.items():
            transaction_hashes_payment_channels_dict[key] = np.random.choice(a = list(payment_channels.keys()), p = list(payment_channels.values()), replace = True, size = 1)[0]
        return transaction_hashes_payment_channels_dict

