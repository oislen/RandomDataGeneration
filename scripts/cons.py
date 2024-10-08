import os
import platform

# set file paths and locations with repo
fpath_root_dir = 'E:\\GitHub' if platform.system() == 'Windows' else '/home/ubuntu' 
fpath_repo_dir = os.path.join(fpath_root_dir, 'RandomTelecomPayments')
fpath_randomtelecomtransdata = os.path.join(fpath_repo_dir, 'data','RandomTelecomPayments.csv')
fpath_randomtelecomusersdata = os.path.join(fpath_repo_dir, 'data','RandomTelecomUsers.parquet')
fpath_arch_randomtelecomdata = os.path.join(fpath_repo_dir, 'data', 'arch', 'RandomTelecomPayments.csv')
fpath_domain_email = os.path.join(fpath_repo_dir, 'scripts', 'ref', 'email-domains.csv')
fpath_countrycrimeindex = os.path.join(fpath_repo_dir, 'scripts', 'ref', 'country_crime_index.csv')
fpath_countrieseurope = os.path.join(fpath_repo_dir, 'scripts', 'ref', 'Countries-Europe.csv')
fpath_firstnames = os.path.join(fpath_repo_dir, 'scripts', 'ref', 'first-names.txt')
fpath_lastnames = os.path.join(fpath_repo_dir, 'scripts', 'ref', 'last-names.txt')
fpath_smartphones = os.path.join(fpath_repo_dir, 'scripts', 'ref', 'smartphones.csv')
fpath_unittest_user_data = os.path.join(fpath_repo_dir, 'data', 'unittest', 'user_data.pickle')
fpath_unittest_transaction_data = os.path.join(fpath_repo_dir, 'data', 'unittest', 'transaction_data.pickle')
fpath_aws_session_token = os.path.join(fpath_repo_dir, '.creds','sessionToken.json')

# set url links to files available online
url_european_populations = 'https://raw.githubusercontent.com/ajturner/acetate/master/places/Countries-Europe.csv'
url_country_populations = 'https://raw.githubusercontent.com/ajturner/acetate/master/places/Countries.csv'
url_first_names = 'https://gist.githubusercontent.com/elifiner/cc90fdd387449158829515782936a9a4/raw/e1a219c33d91b3eecb51ae7b5647d26ed667a11d/first-names.txt'
url_last_names = 'https://gist.githubusercontent.com/elifiner/cc90fdd387449158829515782936a9a4/raw/e1a219c33d91b3eecb51ae7b5647d26ed667a11d/last-names.txt'

# set unittest constants
unittest_seed = 42
unittest_n_entities = 4
unittest_n_device_types = 10
unittest_gen_test_dfs = False
unittest_debug_mode = True
unittest_n_users = 100
unittest_registration_start_date = '2020-01-01'
unittest_registration_end_date = '2020-12-31'
unittest_transaction_start_date = '2021-01-01'
unittest_transaction_end_date = '2021-12-31'

# set data model constants
date_date_strftime = "%Y-%m-%d"
data_model_entity_user_ratios = {'card':1.3, 'device':2.5, 'transaction':5.3, 'ip':4.3}
data_model_poisson_params = {'user':{'lambda':20, 'power':1}, 'device':{'lambda':0.2, 'power':2}, 'card':{'lambda':0.1, 'power':2}, 'ip':{'lambda':1.3, 'power':2}, 'application':{'lambda':1, 'power':2}, 'transaction':{'lambda':5, 'power':2}}
data_model_shared_entities_dict = {'ip':0.05, 'card':0.005, 'device':0.01}
data_model_null_rates = {'card':0.05}
data_model_card_types_dict = {'visa':0.5, 'mastercard':0.5}
data_model_payment_channels = {'paypal':0.4, 'adyen':0.15, 'appstore':0.25, 'worldpay':0.15, 'docomo':0.05}
data_model_transaction_status = {'successful':0.94, 'pending':0.03, 'rejected':0.03}
data_model_inconsistent_country_codes_rejection_rate = {1:0.001, 2:0.005, 3:0.01}
data_model_non_card_trans_methods = {'wallet':0.95, 'points':0.05}
data_model_rejection_codes_fraud = {'E900:ConnectionTimeout':0.1, 'E901:SuspectedFraud':0.55, 'E902:AuthenicationFailure':0.2, 'E903:UserCancelled':0.05, 'E904:InsufficientFunds':0.1}
data_model_rejection_codes_connection = {'E900:ConnectionTimeout':0.45, 'E901:SuspectedFraud':0.1, 'E902:AuthenicationFailure':0.2, 'E903:UserCancelled':0.15, 'E904:InsufficientFunds':0.1}
data_model_rejection_codes_user = {'E900:ConnectionTimeout':0.05, 'E901:SuspectedFraud':0.1, 'E902:AuthenicationFailure':0.1, 'E903:UserCancelled':0.45, 'E904:InsufficientFunds':0.3}
data_model_rejection_codes_funds = {'E900:ConnectionTimeout':0.1, 'E901:SuspectedFraud':0.1, 'E902:AuthenicationFailure':0.1, 'E903:UserCancelled':0.25, 'E904:InsufficientFunds':0.45}
data_model_rejection_codes_authentication = {'E900:ConnectionTimeout':0.25, 'E901:SuspectedFraud':0.05, 'E902:AuthenicationFailure':0.45, 'E903:UserCancelled':0.15, 'E904:InsufficientFunds':0.1}