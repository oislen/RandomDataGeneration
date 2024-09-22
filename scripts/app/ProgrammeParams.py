import numpy as np
import cons

class ProgrammeParams():
    
    def __init__(self, factor = 1, randomseed = None, debug_mode = False, n_users = 2000, n_applications = 20000, n_device_types = 200, registration_start_date = '2020-01-01', registration_end_date = '2020-12-31', transaction_start_date = '2021-01-01', transaction_end_date = '2021-12-31'):
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