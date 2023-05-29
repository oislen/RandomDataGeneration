import numpy as np
import pandas as pd
import pandas as pd
from datetime import datetime
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict

class Transaction():

    def __init__(self, n_transaction_hashes, start_date, end_date):
        self.n_transaction_hashes = n_transaction_hashes
        self.start_date = start_date
        self.end_date = end_date
        self.payment_channels = cons.payment_channels
        self.transaction_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_transaction_hashes)
        self.transaction_hashes_props_dict = cnt2prop_dict(self.transaction_hashes_cnts_dict)
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

