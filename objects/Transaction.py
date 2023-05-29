import numpy as np
import pandas as pd
import pandas as pd
from datetime import datetime
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_dates_dict import gen_dates_dict

class Transaction():

    def __init__(self, n_transaction_hashes, start_date, end_date):
        self.n_transaction_hashes = n_transaction_hashes
        self.start_date = start_date
        self.end_date = end_date
        self.payment_channels = cons.payment_channels
        self.transaction_status = cons.transaction_status
        self.transaction_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type = 'hash', n = self.n_transaction_hashes)
        self.transaction_hashes_props_dict = cnt2prop_dict(self.transaction_hashes_cnts_dict)
        self.transaction_hashes_dates_dict = gen_dates_dict(self.transaction_hashes_cnts_dict, start_date = self.start_date, end_date = self.end_date)
        self.transaction_hashes_payment_channel_dict = self.gen_transaction_payment_channel(self.transaction_hashes_cnts_dict, self.payment_channels)
        self.transaction_hashes_status_dict = self.gen_transaction_status(self.transaction_hashes_cnts_dict, self.transaction_status)

    def gen_transaction_payment_channel(self, transaction_hashes_cnts_dict, payment_channels):
        """"""
        transaction_hashes = list(transaction_hashes_cnts_dict.keys())
        transactioin_payment_channels = list(np.random.choice(a = list(payment_channels.keys()), p = list(payment_channels.values()), replace = True, size = len(transaction_hashes)))
        transaction_hashes_payment_channels_dict = dict(zip(transaction_hashes, transactioin_payment_channels))
        return transaction_hashes_payment_channels_dict

    def gen_transaction_status(self, transaction_hashes_cnts_dict, transaction_status):
        """"""
        transaction_hashes = list(transaction_hashes_cnts_dict.keys())
        transaction_status = list(np.random.choice(a = list(transaction_status.keys()), p = list(transaction_status.values()), replace = True, size = len(transaction_hashes)))
        transaction_hashes_status_dict = dict(zip(transaction_hashes, transaction_status))
        return transaction_hashes_status_dict
