# set user level poisson lambda values 
user_config = {'lambda':{'device':0.3, 'card':0.8, 'ip':15, 'country':0.2, 'application':3, 'transaction':5}}
# set payment channels
payment_channels = {'paypal':0.4, 'adyen':0.3, 'worldpay':0.2, 'docomo':0.1}
# set null value rates
null_rates = {'device':0.1, 'card':0.1, 'ip':0.1, 'application':0.1}
# set proportion of shared entities
shared_entities_dict = {'ip':0.05, 'card':0.01, 'device':0.01}