import numpy as np
import random
from beartype import beartype

from app.ProgrammeParams import ProgrammeParams
from app.gen_user_data import gen_user_data
from app.gen_trans_data import gen_trans_data
from objects.Application import Application
from objects.Card import Card
from objects.Device import Device
from objects.Ip import Ip
from objects.Transaction import Transaction
from objects.User import User
from utilities.gen_random_entity_counts import gen_random_entity_counts
import cons

@beartype
def gen_random_telecom_data(
    n_users=1,
    random_seed=None,
    registration_start_date='2020-01-01',
    registration_end_date='2020-12-31',
    transaction_start_date='2021-01-01',
    transaction_end_date='2021-12-31'
    ):
    """
    Generates random telecommunications data.

    Parameters
    ----------
    n_users : float
        The number of users to generate random telecom payments data for.
    random_seed : int
        A set random seed for reproducible results, default is None.
    registration_start_date : str
        The user registration start date.
    registration_end_date : str
        The user registration end date.
    transaction_start_date : str
        The user transaction start date.
    transaction_end_date : str
        The user transaction end date.

    Returns
    -------
    pandas.DataFrame
        A random telecommunication payments dataset.
    """

    # initalise programme parameters
    programmeparams = ProgrammeParams(
        n_users=n_users, 
        random_seed=random_seed,
        n_applications=20000,
        registration_start_date=registration_start_date, 
        registration_end_date=registration_end_date,
        transaction_start_date=transaction_start_date,
        transaction_end_date=transaction_end_date
        )

    # set random seed
    random.seed(programmeparams.random_seed)
    np.random.seed(seed=programmeparams.random_seed)

    # generate random users
    user_obj = User(
        n_user_ids=programmeparams.n_users,
        start_date=programmeparams.registration_start_date,
        end_date=programmeparams.registration_end_date,
        fpath_firstnames=cons.fpath_llama_firstnames,
        fpath_lastnames=cons.fpath_llama_lastnames,
        fpath_countrieseurope=cons.fpath_countrieseurope,
        fpath_domain_email=cons.fpath_domain_email
        )

    # generate random entity counts for each user
    random_entity_counts = gen_random_entity_counts(
        user_obj=user_obj,
        transaction_timescale=programmeparams.transaction_timescale
        )

    # generate random entity values
    device_obj = Device(n_device_hashes=random_entity_counts['n_devices'].sum())
    card_obj = Card(n_card_hashes=random_entity_counts['n_cards'].sum())
    ip_obj = Ip(n_ip_hashes=random_entity_counts['n_ips'].sum())
    transaction_obj = Transaction(n_transaction_hashes=random_entity_counts['n_transactions'].sum(), start_date=programmeparams.transaction_start_date, end_date=programmeparams.transaction_end_date)
    application_obj = Application(n_application_hashes=programmeparams.n_applications)

    # generate user level data
    user_data = gen_user_data(
        random_entity_counts=random_entity_counts,
        user_obj=user_obj,
        device_obj=device_obj,
        card_obj=card_obj,
        ip_obj=ip_obj,
        transaction_obj=transaction_obj,
        application_obj=application_obj,
    )

    # generate transaction level data
    trans_data = gen_trans_data(
        user_data=user_data,
        user_obj=user_obj,
        device_obj=device_obj,
        card_obj=card_obj,
        ip_obj=ip_obj,
        transaction_obj=transaction_obj,
        application_obj=application_obj,
        fpath_countrycrimeindex=cons.fpath_countrycrimeindex
    )

    return {"user_data":user_data, "trans_data":trans_data}
