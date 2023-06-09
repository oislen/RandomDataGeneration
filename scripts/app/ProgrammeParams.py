import numpy as np
import cons

class ProgrammeParams():
    
    def __init__(self, factor = 1, randomseed = None, debug_mode = False, n_users = 1372, n_applications = 16472, n_device_types = 53, registration_start_date = '2020-01-01', registration_end_date = '2021-12-31', transaction_start_date = '2021-01-01', transaction_end_date = '2021-12-31'):
        # if running in debug mode
        if debug_mode:
            # take programme parameters from constants file
            self.factor = cons.programme_parameters_factor
            self.randomseed = cons.programme_parameters_randomseed
            self.debug_mode = cons.debug_mode
            self.n_users = int(np.round(cons.programme_parameters_n_users * cons.programme_parameters_factor))
            self.n_applications = cons.programme_parameters_n_applications
            self.n_device_types = cons.programme_parameters_n_device_types
            self.registration_start_date = cons.programme_parameters_registration_start_date
            self.registration_end_date = cons.programme_parameters_registration_end_date
            self.transaction_start_date = cons.programme_parameters_transaction_start_date
            self.transaction_end_date = cons.programme_parameters_transaction_end_date
        else:
            # take programme parameters from class parameters
            self.factor = factor
            self.randomseed = randomseed
            self.debug_mode = debug_mode
            self.n_users = int(np.round(n_users * factor))
            self.n_applications = n_applications
            self.n_device_types = n_device_types
            self.registration_start_date = registration_start_date
            self.registration_end_date = registration_end_date
            self.transaction_start_date = transaction_start_date
            self.transaction_end_date = transaction_end_date
        # extract out the entity user ratios
        self.card_user_ratio = cons.entity_user_ratios['card']
        self.device_user_ratio = cons.entity_user_ratios['device']
        self.transaction_user_ratio = cons.entity_user_ratios['transaction']
        self.ip_user_ratio = cons.entity_user_ratios['ip']
        # determine the number of each entity
        self.n_cards = int(np.round(self.n_users * self.card_user_ratio))
        self.n_devices = int(np.round(self.n_users * self.device_user_ratio))
        self.n_transactions = int(np.round(self.n_users * self.transaction_user_ratio))
        self.n_ips = int(np.round(self.n_users * self.ip_user_ratio))