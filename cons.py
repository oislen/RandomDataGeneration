import os
# set file locations
domain_email_fpath = os.path.join('.', 'RandomTeleComData', 'data','email-domains.csv')
randomtelecomdata_fpath = os.path.join('.', 'RandomTeleComData', 'data','RandomTeleComData.csv')
# set user level poisson lambda values 
user_config = {'lambda':{'user':20, 'device':0.3, 'card':0.1, 'ip':1.3, 'application':3, 'transaction':5}}
# set proportion of shared entities
shared_entities_dict = {'ip':0.05, 'card':0.005, 'device':0.01}
# set card types
card_types = {'visa':0.5, 'mastercard':0.5}
# set payment channels
payment_channels = {'paypal':0.4, 'adyen':0.3, 'worldpay':0.2, 'docomo':0.1}
# set transaction status
transaction_status = {'successful':0.94, 'pending':0.03, 'rejected':0.03}
# set rejection codes
rejection_codes = {'E900:ConnectionTimeout':0.2, 'E901:SuspectedFraud':0.2, 'E902:AuthenicationFailure':0.2, 'E903:UserCancelled':0.2, 'E904:InsufficientFunds':0.2}
# set flat files
european_populations_url = 'https://raw.githubusercontent.com/ajturner/acetate/master/places/Countries-Europe.csv'
first_names_url = 'https://gist.githubusercontent.com/elifiner/cc90fdd387449158829515782936a9a4/raw/e1a219c33d91b3eecb51ae7b5647d26ed667a11d/first-names.txt'
last_names_url = 'https://gist.githubusercontent.com/elifiner/cc90fdd387449158829515782936a9a4/raw/e1a219c33d91b3eecb51ae7b5647d26ed667a11d/last-names.txt'