import numpy as np

def gen_trans_error_codes(trans_data, trans_status_col, rejection_codes):
    """"""
    tmp_data = trans_data.copy()
    tmp_data['transaction_error_code'] = np.nan
    failed_transactions_filter = tmp_data[trans_status_col] == 'rejected'
    random_error_codes = np.random.choice(a = list(rejection_codes.keys()), p = list(rejection_codes.values()), size = failed_transactions_filter.sum(), replace = True)
    tmp_data.loc[failed_transactions_filter, 'transaction_error_code'] = random_error_codes
    return tmp_data['transaction_error_code']