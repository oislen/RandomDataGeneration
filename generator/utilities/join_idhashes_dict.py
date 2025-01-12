import pandas as pd

def join_idhashes_dict(data, idhashes_dict, idhash_key_name, idhash_val_name):
    """Joins an entity attribute dictionary to either the user or transaction data

    Parameters
    ----------
    data : pd.DataFrame
        The user or transaction data
    idhashes_dict : Dictionary
        The entity attribute dictionary with an idhash as the key for joining to the user or transaction data
    idhash_key_name : String
        The name of the idhash key for joining to the user or transaction data
    idhash_val_name : String
        The name to set for the idhash attribute when joining to the user or transaction data

    Returns
    -------
    pd.DataFrame
        The user or transaction data returned with the joined idhash attribute dictionary values
    """
    idhashes_df = pd.Series(idhashes_dict, name=idhash_val_name).to_frame().reset_index().rename(columns={'index':idhash_key_name})
    idhashes_join = pd.merge(left=data, right=idhashes_df, on=idhash_key_name, how='left')
    return idhashes_join