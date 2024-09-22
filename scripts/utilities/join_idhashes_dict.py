import pandas as pd

def join_idhashes_dict(data, idhashes_dict, idhash_key_name, idhash_val_name):
    """
    """
    idhashes_df = pd.Series(idhashes_dict, name=idhash_val_name).to_frame().reset_index().rename(columns={'index':idhash_key_name})
    idhashes_join = pd.merge(left=data, right=idhashes_df, on=idhash_key_name, how='left')
    return idhashes_join