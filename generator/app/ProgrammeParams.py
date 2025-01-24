import cons
from datetime import datetime
from beartype import beartype

class ProgrammeParams():
    
    @beartype
    def __init__(
        self,
        n_users:int=100,
        random_seed:int=None,
        n_applications:int=20000,
        registration_start_date:str=cons.default_registration_start_date,
        registration_end_date:str=cons.default_registration_end_date,
        transaction_start_date:str=cons.default_transaction_start_date,
        transaction_end_date:str=cons.default_transaction_end_date
        ):
        # take programme parameters from class parameters
        self.random_seed = random_seed
        self.n_users = n_users
        self.n_applications = n_applications
        self.registration_start_date = registration_start_date
        self.registration_end_date = registration_end_date
        self.transaction_start_date = transaction_start_date
        self.transaction_end_date = transaction_end_date
        transaction_start_date_strftime = datetime.strptime(self.transaction_start_date, cons.date_date_strftime)
        transaction_end_date_strftime = datetime.strptime(self.transaction_end_date, cons.date_date_strftime)
        self.transaction_timescale = ((transaction_end_date_strftime - transaction_start_date_strftime).days + 1) / 365