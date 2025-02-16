import numpy as np
import pandas as pd
from datetime import datetime
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_dates_dict import gen_dates_dict
from utilities.round_trans_amount import round_trans_amount
from beartype import beartype

class Transaction:

    @beartype
    def __init__(
        self,
        n_transaction_hashes,
        start_date,
        end_date
        ):
        """
        The randomly generated transaction data model object.

        Parameters
        ----------
        n_transaction_hashes : int
            The number of transaction hashes to generate.
        start_date : str
            The start date to generate transactions from.
        end_date : str
            The end date to generate transaction till.

        Attributes
        ----------
        n_transaction_hashes : int
            The number of transaction hashes generated.
        start_date : str
            The date transactions are generated from, must be of the form '%Y-%m-%d'.
        end_date : str
            The date transactions are generated till, must be of the form '%Y-%m-%d'.
        lam : float
            The lambda parameter of the squared poisson distribution used to generate the transaction hash counts.
        payment_channels : float
            The population proportion of payment channels.
        transaction_status : float
            The population proportion of transaction statuses.
        rejection_codes : float
            The population proportion of rejection codes.
        transaction_hashes_cnts_dict : dict
            The transaction hash counts dictionary.
        transaction_hashes_props_dict : dict
            The transaction hash proportions dictionary.
        transaction_hashes_dates_dict : dict
            The transaction hash dates dictionary.
        transaction_hashes_payment_channel_dict : dict
            The transaction hash payment channels dictionary.
        transaction_hashes_status_dict : dict
            The transaction hash status dictionary.
        transaction_hashes_amounts_dict : dict
            The transaction hash amount dictionary.
        """
        self.n_transaction_hashes = n_transaction_hashes
        self.start_date = start_date
        self.end_date = end_date
        self.lam = cons.data_model_poisson_params["transaction"]["lambda"]
        self.power = cons.data_model_poisson_params["transaction"]["power"]
        self.transaction_status = cons.data_model_transaction_status
        self.transaction_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type="hash", n=self.n_transaction_hashes, lam=self.lam)
        self.transaction_hashes_props_dict = cnt2prop_dict(self.transaction_hashes_cnts_dict)
        self.transaction_hashes_dates_dict = gen_dates_dict(self.transaction_hashes_cnts_dict,start_date=self.start_date,end_date=self.end_date,)
        self.transaction_hashes_status_dict = self.gen_transaction_status(list(self.transaction_hashes_cnts_dict.keys()), self.transaction_status)
        self.transaction_hashes_amounts_dict = self.gen_transaction_amounts(list(self.transaction_hashes_cnts_dict.keys()))

    @beartype
    def gen_transaction_status(
        self,
        transaction_hashes:list,
        transaction_status:dict
        ):
        """
        Generates a dictionary of random transaction statuses

        Parameters
        ----------
        transaction_hashes : list
            The transaction hashes
        transaction_status : dict
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
        transaction_hashes_status_dict = dict(zip(transaction_hashes, transaction_status))
        return transaction_hashes_status_dict

    @beartype
    def gen_transaction_amounts(
        self,
        transaction_hashes:list,
        loc:float=0,
        scale:float=2
        ):
        """
        Generates a dictionary of random transaction hash amounts.

        Parameters
        ----------
        transaction_hashes : list
            The transaction hashes.
        loc : float
            The mean of the transaction amount distribution to generate, default is 0.
        scale : float
            The scale of the transaction amount distribution to generate, default is 2.

        Returns
        -------
        dict
            A dictionary of transaction hash prices
        """
        # randomly sample transaction prices from an absolute normal distribution with mean 0 and standard deviation 2
        trans_prices = np.round(np.abs(np.random.normal(loc=loc, scale=scale, size=len(transaction_hashes)))** 2,2,)
        # return the transaction hashes and prices
        trans_prices_dict = dict(zip(transaction_hashes, round_trans_amount(trans_prices)))
        return trans_prices_dict