import numpy as np
import pandas as pd

def round_trans_amount(amounts):
    """Rounds transaction amounts to have store price like remainders such as 1.99, 3.45, and 2.5

    Parameters
    ----------
    amounts : np.array
        The transaction amounts to round
    
    Returns
    -------
    np.array
        The rounded transaction amounts with store rice like remainders
    """
    round_dict = {0.01:0.4, 0.5:0.1, 0.45:0.1, 0.51:0.1, 0.41:0.1, 0.71:0.1, 1:0.1}
    remainder = np.random.choice(a=list(round_dict.keys()), size=amounts.shape[0], replace=True, p=list(round_dict.values()))
    rounded_amounts = np.round(np.ceil(amounts) - remainder, 2)
    rounded_amounts = pd.Series(rounded_amounts).apply(lambda x: max(0, x)).values
    return rounded_amounts