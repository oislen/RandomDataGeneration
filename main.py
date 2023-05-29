# TODO:
# 3. Add null values
# 4. change to device and application dictionaries to python classes
# 5. rewrite using polars / dask

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utilities as utl
import cons
from datetime import datetime

# set number of users to random generate
n = 1000

# generate random devices
device_hashes_dict = utl.gen_hash_dict(n_hashes = n)
device_props_dict = utl.cnt2prop_dict(device_hashes_dict)
device_type_dict = utl.gen_device_type(device_hashes_dict, n_device_types = 20)

# generate random applications
application_hashes_dict = utl.gen_hash_dict(n_hashes = n)
application_hashes_props_dict = utl.cnt2prop_dict(application_hashes_dict)
application_hash_prices_dict = utl.gen_application_prices(application_hashes_dict)

# generate counts per entity at user level
user_data = pd.DataFrame()
user_data['userid'] = np.random.choice(a = range(100000, 1000000), size = n, replace = False)
user_data['n_devices'] = np.random.poisson(lam = cons.user_config['lambda']['device'], size = n) + 1
user_data['n_cards'] = np.random.poisson(lam = cons.user_config['lambda']['card'], size = n) + 1
user_data['n_ips'] = np.random.poisson(lam = cons.user_config['lambda']['ip'], size = n) + 1
user_data['n_applications'] = np.random.poisson(lam = cons.user_config['lambda']['application'], size = n) + 1
user_data['n_countries'] = np.random.poisson(lam = cons.user_config['lambda']['country'], size = n) + 1
user_data['n_transactions'] = np.random.poisson(lam = cons.user_config['lambda']['transaction'], size = n) + 1

# generate entities from 
user_data['device_hash'] = user_data['n_devices'].apply(lambda x: np.random.choice(a = list(device_props_dict.keys()), p = list(device_props_dict.values()), replace = True, size = x))
user_data['card_hash'] = user_data['n_cards'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['ip_hash'] = user_data['n_ips'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['trans_hash'] = user_data['n_transactions'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['application_hash'] = user_data['n_applications'].apply(lambda x: np.random.choice(a = list(application_hashes_props_dict.keys()), p = list(application_hashes_props_dict.values()), replace = True, size = x))

# explode out transactions
drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_applications', 'n_countries', 'n_transactions']
trans_data = user_data.explode('trans_hash').drop(columns = drop_columns)
trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['device_type'] = trans_data['device_hash'].replace(device_type_dict)
trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['application_hash'] = trans_data['application_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])

# randomly shuffle data
trans_data = trans_data.sample(n = trans_data.shape[0], replace = False)

# add transaction amount
trans_data['transaction_amount'] = trans_data['application_hash'].replace(application_hash_prices_dict)
# add payment channel
trans_data['payment_channel'] = trans_data.apply(lambda s: np.random.choice(a = list(cons.payment_channels.keys()), p = list(cons.payment_channels.values()), replace = True, size = 1)[0], axis = 1)
# add transaction date
dates = pd.date_range(datetime.strptime('2021-01-01', '%Y-%m-%d'), datetime.strptime('2021-12-31', '%Y-%m-%d') - pd.Timedelta(days=1),freq='d')
trans_data['transaction_date'] = trans_data.apply(lambda s: np.random.choice(a = dates, replace = True, size = 1)[0], axis = 1)

# add shared entities
shared_ip = np.random.choice(a = trans_data['ip_hash'].unique(), size = int(np.round(trans_data['ip_hash'].nunique() * cons.shared_entities_dict['ip'])))
shared_card = np.random.choice(a = trans_data['card_hash'].unique(), size = int(np.round(trans_data['card_hash'].nunique() * cons.shared_entities_dict['card'])))
shared_device = np.random.choice(a = trans_data['device_hash'].unique(), size = int(np.round(trans_data['device_hash'].nunique() * cons.shared_entities_dict['device'])))
# add shared entities
trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['ip'] else x)
trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['card'] else x)
trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['device'] else x)

trans_data.head()