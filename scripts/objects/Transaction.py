import numpy as np
import pandas as pd
import pandas as pd
from datetime import datetime
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_dates_dict import gen_dates_dict


class Transaction:
    """The randomly generated transaction data model object 

    Parameters
    ----------
    n_transaction_hashes : int
        The number of transaction hashes to generate
    start_date : str
        The start date to generate transactions from
    end_date : str
        The end date to generate transaction till

    Attributes
    ----------
    n_transaction_hashes : int
        The number of transaction hashes generated
    start_date : str
        The date transactions are generated from, must be of the form '%Y-%m-%d'
    end_date : str
        The date transactions are generated till, must be of the form '%Y-%m-%d'
    lam : float
        The lambda parameter of the squared poisson distribution used to generate the transaction hash counts
    payment_channels : float
        The population proportion of payment channels
    transaction_status : float
        The population proportion of transaction statuses
    rejection_codes : float
        The population proportion of rejection codes
    transaction_hashes_cnts_dict : dict
        The transaction hash counts dictionary
    transaction_hashes_props_dict : dict
        The transaction hash proportions dictionary
    transaction_hashes_dates_dict : dict
        The transaction hash dates dictionary
    transaction_hashes_payment_channel_dict : dict
        The transaction hash payment channels dictionary
    transaction_hashes_status_dict : dict
        The transaction hash status dictionary
    """

    def __init__(self, n_transaction_hashes, start_date, end_date):
        self.n_transaction_hashes = n_transaction_hashes
        self.start_date = start_date
        self.end_date = end_date
        self.lam = cons.data_model_poisson_lambda_params["transaction"]
        self.payment_channels = cons.data_model_payment_channels
        self.transaction_status = cons.data_model_transaction_status
        self.rejection_codes = cons.data_model_rejection_codes
        self.transaction_hashes_cnts_dict = gen_idhash_cnt_dict(
            idhash_type="hash", n=self.n_transaction_hashes, lam=self.lam
        )
        self.transaction_hashes_props_dict = cnt2prop_dict(
            self.transaction_hashes_cnts_dict
        )
        self.transaction_hashes_dates_dict = gen_dates_dict(
            self.transaction_hashes_cnts_dict,
            start_date=self.start_date,
            end_date=self.end_date,
        )
        self.transaction_hashes_payment_channel_dict = self.gen_transaction_payment_channel(
            list(self.transaction_hashes_cnts_dict.keys()), self.payment_channels
        )
        self.transaction_hashes_status_dict = self.gen_transaction_status(
            list(self.transaction_hashes_cnts_dict.keys()), self.transaction_status
        )

    def gen_transaction_payment_channel(self, transaction_hashes, payment_channels):
        """Generates a dictionary of random transaction payment channels
        
        Parameters
        ----------
        transaction_hashes : list
            The transaction hashes
        payment_channels : dict
            The population proportion of payment channels
        
        Returns
        -------
        dict
            A dictionary of transaction payment channels
        """
        # randomly sample payment channels based on population proportions
        transactoin_payment_channels = list(
            np.random.choice(
                a=list(payment_channels.keys()),
                p=list(payment_channels.values()),
                replace=True,
                size=len(transaction_hashes),
            )
        )
        # return payment channels and transaction hashes
        transaction_hashes_payment_channels_dict = dict(
            zip(transaction_hashes, transactoin_payment_channels)
        )
        return transaction_hashes_payment_channels_dict

    def gen_transaction_status(self, transaction_hashes, transaction_status):
        """Generates a dictionary of random transaction statuses
        
        Parameters
        ----------
        transaction_hashes : list
            The transaction hashes
        payment_channels : dict
            The population proportion of transaction statuses
        
        Returns
        -------
        dict
            A dictionary of transaction statuses
        """
        # randomly sample transaction status based on population proportions
        transaction_status = list(
            np.random.choice(
                a=list(transaction_status.keys()),
                p=list(transaction_status.values()),
                replace=True,
                size=len(transaction_hashes),
            )
        )
        # return transaction hashes and statuses
        transaction_hashes_status_dict = dict(
            zip(transaction_hashes, transaction_status)
        )
        return transaction_hashes_status_dict
