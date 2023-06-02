import numpy as np
from app.ProgrammeParams import ProgrammeParams
from app.gen_user_agg_data import gen_user_agg_data
from app.gen_user_data import gen_user_data
from app.gen_trans_data import gen_trans_data
from objects.Application import Application
from objects.Card import Card
from objects.Device import Device
from objects.Ip import Ip
from objects.Transaction import Transaction
from objects.User import User


def gen_random_telecom_data(factor=1, randomseed=None):
    """Generates random telecommunications data

    Parameters
    ----------
    factor : float
        The controls the number of users and corresponding number of data model entities to generate
    randomseed : int
        A random seed for reproducible results, default is None

    Returns
    -------
    pandas.DataFrame
        A random telecommunication payments dataset
    """

    # initalise programme parameters
    programmeparams = ProgrammeParams(factor=factor, randomseed=randomseed)

    # set random seed
    np.random.seed(seed=programmeparams.randomseed)

    # generate random applications
    application_obj = Application(n_application_hashes=programmeparams.n_applications)

    # generate random cards
    card_obj = Card(n_card_hashes=programmeparams.n_cards)

    # generate random devices
    device_obj = Device(
        n_device_hashes=programmeparams.n_devices,
        n_device_types=programmeparams.n_device_types,
    )

    # generate random ips
    ip_obj = Ip(n_ip_hashes=programmeparams.n_ips)

    # generate random transactions
    transaction_obj = Transaction(
        n_transaction_hashes=programmeparams.n_transactions,
        start_date=programmeparams.transaction_start_date,
        end_date=programmeparams.transaction_end_date,
    )

    # generate random users
    user_obj = User(
        n_user_ids=programmeparams.n_users,
        start_date=programmeparams.registration_start_date,
        end_date=programmeparams.registration_end_date,
    )

    # generate counts per entity at user level
    user_agg_data = gen_user_agg_data(
        user_obj=user_obj,
        device_obj=device_obj,
        card_obj=card_obj,
        ip_obj=ip_obj,
        transaction_obj=transaction_obj,
        application_obj=application_obj,
    )

    # generate user level data
    user_data = gen_user_data(
        user_agg_data=user_agg_data,
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
        device_obj=device_obj,
        card_obj=card_obj,
        ip_obj=ip_obj,
        transaction_obj=transaction_obj,
        application_obj=application_obj,
    )

    return trans_data
