# TODO:
# 1. Add payment channel, transaction amount, application id
# 2. Add shared entities i.e. shared device hashes, ip hashes and card hashes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utilities as utl
import cons

# generate random devices
device_props_dict = utl.cnt2prop_dict(utl.gen_device_type(n_device_types = 20))

# set number of users to random generate
n = 1000

# generate counts per entity at user level
user_data = pd.DataFrame()
user_data['userid'] = np.random.choice(a = range(100000, 1000000), size = n, replace = False)
user_data['n_devices'] = np.random.poisson(lam = cons.user_config['lambda']['device'], size = n) + 1
user_data['n_cards'] = np.random.poisson(lam = cons.user_config['lambda']['card'], size = n) + 1
user_data['n_ips'] = np.random.poisson(lam = cons.user_config['lambda']['ip'], size = n) + 1
user_data['n_countries'] = np.random.poisson(lam = cons.user_config['lambda']['country'], size = n) + 1
user_data['n_transactions'] = np.random.poisson(lam = cons.user_config['lambda']['transaction'], size = n) + 1

# generate entities from 
user_data['device_hash'] = user_data['n_devices'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['device_type'] = user_data['n_devices'].apply(lambda x: np.random.choice(a = list(device_props_dict.keys()), p = list(device_props_dict.values()), replace = True, size = x))
user_data['card_hash'] = user_data['n_cards'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['ip_hash'] = user_data['n_ips'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['trans_hash'] = user_data['n_transactions'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))

# explode out transactions
drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_countries', 'n_transactions']
trans_data = user_data.explode('trans_hash').drop(columns = drop_columns)
trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['device_type'] = trans_data['device_type'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])

# randomly shuffle data
trans_data = trans_data.sample(n = trans_data.shape[0], replace = False)

trans_data.head()