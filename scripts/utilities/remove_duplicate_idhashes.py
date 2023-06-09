def remove_duplicate_idhashes(user_data, idhash_col):
    """Removes duplicate idhashes from a given idhash column

    Parameters
    ----------
    user_data : pandas.DataFrame
        The user level telecom payments data
    idhash_col : str
        The column with duplicate idhashes to be removed

    Returns
    -------
    pandas.DataFrame
        A user level telecom data with the duplicate idhashes removed from the specified idhash column
    """
    # take deep copy of the data
    tmp_data = user_data.copy()
    # define duplicate idhash column name
    duplicate_idhash_col = f'duplicate_{idhash_col}'
    # explode out the idhashes
    user_transaction_hashes = tmp_data[idhash_col].explode().rename(duplicate_idhash_col)
    # identify the duplicate idhashes
    duplicated_user_transaction_hashes = user_transaction_hashes[user_transaction_hashes.duplicated()].reset_index().groupby(by = 'index').agg({duplicate_idhash_col:list})
    # join duplicated idhashes to temp data
    tmp_data = tmp_data.join(duplicated_user_transaction_hashes, how = 'left')
    # remove duplicate id hashes
    tmp_data[idhash_col] = tmp_data.apply(lambda s: s[idhash_col] if not s[duplicate_idhash_col] == s[duplicate_idhash_col] else [v for v in s[idhash_col] if v not in s[duplicate_idhash_col]], axis = 1)
    # drop duplicate id hashes columns
    tmp_data = tmp_data.drop(columns = [duplicate_idhash_col])
    return tmp_data