import numpy as np
from ProgrammeParams import ProgrammeParams
# load object classes
from objects.Application import Application
from objects.Card import Card
from objects.Device import Device
from objects.Ip import Ip
from objects.Transaction import Transaction
from objects.User import User
# load utility functions
from utilities.gen_user_agg_data import gen_user_agg_data
from utilities.gen_user_data import gen_user_data
from utilities.gen_trans_data import gen_trans_data

def gen_random_telecom_data(factor = 1, randomseed = None):
    """"""

    # initalise programme parameters
    programmeparams = ProgrammeParams(factor = factor, randomseed = randomseed)

    # set random seed
    np.random.seed(seed = programmeparams.randomseed)
    
    # generate randomised telecom data model objects
    application_obj = Application(n_application_hashes = programmeparams.n_applications)
    card_obj = Card(n_card_hashes = programmeparams.n_cards)
    device_obj = Device(n_device_hashes = programmeparams.n_devices, n_device_types = programmeparams.n_device_types)
    ip_obj = Ip(n_ip_hashes = programmeparams.n_ips)
    transaction_obj = Transaction(n_transaction_hashes = programmeparams.n_transactions, start_date = programmeparams.transaction_start_date, end_date = programmeparams.transaction_end_date)
    user_obj = User(n_user_ids = programmeparams.n_users, start_date = programmeparams.registration_start_date, end_date = programmeparams.registration_end_date)

    # generate counts per entity at user level
    user_agg_data = gen_user_agg_data(user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj)
    # generate user level data 
    user_data =  gen_user_data(user_agg_data, user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj)
    # generate transaction level data
    trans_data = gen_trans_data(user_data, device_obj, card_obj, ip_obj, transaction_obj, application_obj)

    return trans_data