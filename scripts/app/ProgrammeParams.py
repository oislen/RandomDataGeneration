import numpy as np

class ProgrammeParams():
    
    def __init__(self, factor = 1, n_applications = 16472, n_device_types = 53, registration_start_date = '2020-01-01', registration_end_date = '2021-12-31', transaction_start_date = '2021-01-01', transaction_end_date = '2021-12-31', randomseed = None):
        self.factor = factor
        self.n_users = int(np.round(1372 * self.factor))
        self.n_cards = int(np.round(self.n_users * 1.3))
        self.n_devices = int(np.round(self.n_users * 2.5))
        self.n_transactions = int(np.round(self.n_users * 5.3))
        self.n_ips = int(np.round(self.n_users * 4.3))
        self.n_applications = n_applications
        self.n_device_types = n_device_types
        self.registration_start_date = registration_start_date
        self.registration_end_date = registration_end_date
        self.transaction_start_date = transaction_start_date
        self.transaction_end_date = transaction_end_date
        self.randomseed = randomseed