import os
import platform

# set debug mode
debug_mode = True

# set file paths and locations with repo
fpath_root_dir = 'E:\\GitHub' if platform.system() == 'Windows' else '/home/ubuntu' 
fpath_randomtelecomdata = os.path.join(fpath_root_dir, 'RandomTelecomPayments', 'data','RandomTelecomPayments.csv')
fpath_domain_email = os.path.join(fpath_root_dir, 'RandomTelecomPayments', 'scripts', 'ref', 'email-domains.csv')
fpath_countrycrimeindex = os.path.join(fpath_root_dir, 'RandomTelecomPayments', 'scripts', 'ref', 'country_crime_index.csv')
fpath_countrieseurope = os.path.join(fpath_root_dir, 'RandomTelecomPayments', 'scripts', 'ref', 'Countries-Europe.csv')
fpath_firstnames = os.path.join(fpath_root_dir, 'RandomTelecomPayments', 'scripts', 'ref', 'first-names.txt')
fpath_lastnames = os.path.join(fpath_root_dir, 'RandomTelecomPayments', 'scripts', 'ref', 'last-names.txt')

# set url links to files available online
url_european_populations = 'https://raw.githubusercontent.com/ajturner/acetate/master/places/Countries-Europe.csv'
url_first_names = 'https://gist.githubusercontent.com/elifiner/cc90fdd387449158829515782936a9a4/raw/e1a219c33d91b3eecb51ae7b5647d26ed667a11d/first-names.txt'
url_last_names = 'https://gist.githubusercontent.com/elifiner/cc90fdd387449158829515782936a9a4/raw/e1a219c33d91b3eecb51ae7b5647d26ed667a11d/last-names.txt'

# set programme parameters
programme_parameters_factor = 0.5
programme_parameters_randomseed = 1
programme_parameters_nitr = 3
programme_parameters_n_users = 1372
programme_parameters_n_device_types = 53
programme_parameters_n_applications = 1642
programme_parameters_registration_start_date = '2020-01-01'
programme_parameters_registration_end_date = '2021-12-31'
programme_parameters_transaction_start_date = '2021-01-01'
programme_parameters_transaction_end_date = '2021-12-31'

# set unittest constants
unittest_seed = 42
unittest_n_entities = 4
unittest_n_device_types = 10

# set entities to users ratios
entity_user_ratios = {'card':1.3, 'device':2.5, 'transaction':5.3, 'ip':4.3}
# set user level poisson lambda values 
poisson_lambda_params = {'user':20, 'device':0.3, 'card':0.1, 'ip':1.3, 'application':3, 'transaction':5}
# set proportion of shared entities
shared_entities_dict = {'ip':0.05, 'card':0.005, 'device':0.01}
# set null rates
null_rates = {'ip':0.07, 'card':0.05,'device':0.05}
# set card types
card_types_dict = {'visa':0.5, 'mastercard':0.5}
# set payment channels
payment_channels = {'paypal':0.4, 'adyen':0.3, 'worldpay':0.2, 'docomo':0.1}
# set transaction status
transaction_status = {'successful':0.94, 'pending':0.03, 'rejected':0.03}
# set rejection codes
rejection_codes = {'E900:ConnectionTimeout':0.2, 'E901:SuspectedFraud':0.2, 'E902:AuthenicationFailure':0.2, 'E903:UserCancelled':0.2, 'E904:InsufficientFunds':0.2}
# set rejection rates based on inconsistent country codes
inconsistent_country_codes_rejection_rate = {1:0.001, 2:0.005, 3:0.01}