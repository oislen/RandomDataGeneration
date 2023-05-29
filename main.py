import random
import pandas as pd
import numpy as np
import utilities as utl
import cons
import objects as objs

# set number of users to random generate
factor = 1
n_users = int(np.round(1372 * factor))
n_devices = int(np.round(n_users * 2.5))
n_applications = int(np.round(n_users * 1.8))
n_transactions = int(np.round(n_users * 5.3))
n_device_types = 53
start_date = '2021-01-01'
end_date = '2021-12-31'

# generate Device and Application objects
device_obj = objs.Device(n_device_hashes = n_devices, n_device_types = n_device_types)
application_obj = objs.Application(n_application_hashes = n_applications)
transaction_obj = objs.Transaction(n_transaction_hashes = n_transactions, start_date = start_date, end_date = end_date)

# generate counts per entity at user level
user_agg_data = pd.DataFrame()
user_agg_data['userid'] = np.random.choice(a = range(100000, 1000000), size = n_users, replace = False)
user_agg_data['n_devices'] = np.random.poisson(lam = cons.user_config['lambda']['device'], size = n_users) + 1
user_agg_data['n_cards'] = np.random.poisson(lam = cons.user_config['lambda']['card'], size = n_users) + 1
user_agg_data['n_ips'] = np.random.poisson(lam = cons.user_config['lambda']['ip'], size = n_users) + 1
user_agg_data['n_applications'] = np.random.poisson(lam = cons.user_config['lambda']['application'], size = n_users) + 1
user_agg_data['n_countries'] = np.random.poisson(lam = cons.user_config['lambda']['country'], size = n_users) + 1
user_agg_data['n_transactions'] = np.random.poisson(lam = cons.user_config['lambda']['transaction'], size = n_users) + 1

# generate user level data 
user_data = user_agg_data.copy()
user_data['device_hash'] = user_data['n_devices'].apply(lambda x: np.random.choice(a = list(device_obj.device_hashes_props_dict.keys()), p = list(device_obj.device_hashes_props_dict.values()), replace = True, size = x))
user_data['card_hash'] = user_data['n_cards'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['ip_hash'] = user_data['n_ips'].apply(lambda x: utl.gen_random_hash(size = x, nbytes = 16))
user_data['transaction_hash'] = user_data['n_transactions'].apply(lambda x: np.random.choice(a = list(transaction_obj.transaction_hashes_props_dict.keys()), p = list(transaction_obj.transaction_hashes_props_dict.values()), replace = False, size = x))
user_data['application_hash'] = user_data['n_applications'].apply(lambda x: np.random.choice(a = list(application_obj.application_hashes_props_dict.keys()), p = list(application_obj.application_hashes_props_dict.values()), replace = True, size = x))
drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_applications', 'n_countries', 'n_transactions']
user_data = user_data.drop(columns = drop_columns)

# generate transaction level data
trans_data = user_data.explode('transaction_hash')
trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['device_type'] = trans_data['device_hash'].replace(device_obj.device_hashes_type_dict)
trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['application_hash'] = trans_data['application_hash'].apply(lambda x: np.random.choice(x, size = 1)[0])
trans_data['transaction_amount'] = trans_data['application_hash'].replace(application_obj.application_hashes_prices_dict)
trans_data['payment_channel'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_payment_channel_dict)
trans_data['transaction_date'] = trans_data['transaction_hash'].replace(transaction_obj.transaction_hashes_dates_dict)
# randomly shuffle data
trans_data = trans_data.sample(n = trans_data.shape[0], replace = False)

# add shared entities
shared_ip = np.random.choice(a = trans_data['ip_hash'].unique(), size = int(np.round(trans_data['ip_hash'].nunique() * cons.shared_entities_dict['ip'])))
shared_card = np.random.choice(a = trans_data['card_hash'].unique(), size = int(np.round(trans_data['card_hash'].nunique() * cons.shared_entities_dict['card'])))
shared_device = np.random.choice(a = trans_data['device_hash'].unique(), size = int(np.round(trans_data['device_hash'].nunique() * cons.shared_entities_dict['device'])))
trans_data['ip_hash'] = trans_data['ip_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['ip'] else x)
trans_data['card_hash'] = trans_data['card_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['card'] else x)
trans_data['device_hash'] = trans_data['device_hash'].apply(lambda x: random.choice(shared_ip) if random.uniform(0, 1) <= cons.shared_entities_dict['device'] else x)

trans_data.head()