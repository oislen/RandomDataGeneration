import numpy as np
import random
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

def gen_random_telecom_data(n_users=1, random_seed=None):
    """Generates random telecommunications data

    Parameters
    ----------
    n_users : float
        The number of users to generate random telecom payments data for
    random_seed : int
        A set random seed for reproducible results, default is None

    Returns
    -------
    pandas.DataFrame
        A random telecommunication payments dataset
    """

    # initalise programme parameters
    programmeparams = ProgrammeParams(n_users=n_users, random_seed=random_seed)

    # set random seed
    random.seed(programmeparams.random_seed)
    np.random.seed(seed=programmeparams.random_seed)

    # generate random users
    user_obj = User(n_user_ids=programmeparams.n_users, start_date=programmeparams.registration_start_date, end_date=programmeparams.registration_end_date)

    # generate random entity counts for each user
    random_entity_counts = gen_random_entity_counts(user_obj)

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
    )

    return {"user_data":user_data, "trans_data":trans_data}
