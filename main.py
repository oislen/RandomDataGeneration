import random
import numpy as np
import os
import sys

# set file path for custom python modules
sys.path.append(os.path.join(os.getcwd(), 'RandomTeleComData'))
# load constants
import cons
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

# set number of users to random generate
factor = 1
n_users = int(np.round(1372 * factor))
n_cards = int(np.round(n_users * 1.3))
n_devices = int(np.round(n_users * 2.5))
n_transactions = int(np.round(n_users * 5.3))
n_ips = int(np.round(n_users * 4.3))
n_applications = 16472
n_device_types = 53
registration_start_date = '2020-01-01'
registration_end_date = '2021-12-31'
transaction_start_date = '2021-01-01'
transaction_end_date = '2021-12-31'

# generate Device and Application objects
application_obj = Application(n_application_hashes = n_applications)
card_obj = Card(n_card_hashes = n_cards)
device_obj = Device(n_device_hashes = n_devices, n_device_types = n_device_types)
ip_obj = Ip(n_ip_hashes = n_ips)
transaction_obj = Transaction(n_transaction_hashes = n_transactions, start_date = transaction_start_date, end_date = transaction_end_date)
user_obj = User(n_user_ids = n_users, start_date = registration_start_date, end_date = registration_end_date)

# generate counts per entity at user level
user_agg_data = gen_user_agg_data(user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj)
# generate user level data 
user_data =  gen_user_data(user_agg_data, user_obj, device_obj, card_obj, ip_obj, transaction_obj, application_obj)
# generate transaction level data
trans_data = gen_trans_data(user_data, device_obj, card_obj, ip_obj, transaction_obj, application_obj)

# print out head of data
trans_data.head()

# write data to disk
#trans_data.to_csv(cons.randomtelecomdata_fpath, index = False)