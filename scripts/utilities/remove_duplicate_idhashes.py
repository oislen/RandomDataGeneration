def remove_duplicate_idhashes(user_data, idhash):
    """"""
    # take deep copy of the data
    tmp_data = user_data.copy()
    # define duplicate idhash column name
    duplicate_idhash = f'duplicate_{idhash}'
    # explode out the idhashes
    user_transaction_hashes = tmp_data[idhash].explode().rename(duplicate_idhash)
    # identify the duplicate idhashes
    duplicated_user_transaction_hashes = user_transaction_hashes[user_transaction_hashes.duplicated()].reset_index().groupby(by = 'index').agg({duplicate_idhash:list})
    # join duplicated idhashes to temp data
    tmp_data = tmp_data.join(duplicated_user_transaction_hashes, how = 'left')
    # remove duplicate id hashes
    tmp_data[idhash] = tmp_data.apply(lambda s: s[idhash] if not s[duplicate_idhash] == s[duplicate_idhash] else [v for v in s[idhash] if v not in s[duplicate_idhash]], axis = 1)
    # drop duplicate id hashes columns
    tmp_data = tmp_data.drop(columns = [duplicate_idhash])
    return tmp_data