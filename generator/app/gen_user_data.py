import pandas as pd
import numpy as np
from objects.User import User
from objects.Device import Device
from objects.Card import Card
from objects.Ip import Ip
from objects.Transaction import Transaction
from objects.Application import Application
from utilities.gen_obj_idhash_series import gen_obj_idhash_series
from utilities.join_idhashes_dict import join_idhashes_dict
from utilities.gen_random_hash import gen_random_hash
from beartype import beartype

@beartype
def gen_user_data(
    random_entity_counts:pd.DataFrame,
    user_obj:User,
    device_obj:Device,
    card_obj:Card,
    ip_obj:Ip,
    transaction_obj:Transaction,
    application_obj:Application
    ) -> pd.DataFrame:
    """
    Generates random user level telecom payments data

    Parameters
    ----------
    random_entity_counts : pd.DataFrame
        The randomly generated entities count data
    user_obj : class
        The random user data model object
    device_obj : class
        The random device data model object
    card_obj : class
        The random card data model object
    ip_obj : class
        The random ip data model object
    transaction_obj : class
        The random transaction data model object
    application_obj : class
        The random application data model object

    Returns
    -------
    pandas.DataFrame
        The random user level telecom payments data
    """
    # take a deep copy of the data
    user_data = random_entity_counts.copy()
    # add user data
    user_data = join_idhashes_dict(data=user_data, idhashes_dict=user_obj.user_ids_firstname_dict, idhash_key_name='uid', idhash_val_name='firstname')
    user_data = join_idhashes_dict(data=user_data, idhashes_dict=user_obj.user_ids_lastname_dict, idhash_key_name='uid', idhash_val_name='lastname')
    user_data = join_idhashes_dict(data=user_data, idhashes_dict=user_obj.user_ids_dates_dict, idhash_key_name='uid', idhash_val_name='registration_date')
    user_data = join_idhashes_dict(data=user_data, idhashes_dict=user_obj.user_ids_country_code_dict, idhash_key_name='uid', idhash_val_name='registration_country_code_alpha')
    user_data = join_idhashes_dict(data=user_data, idhashes_dict=user_obj.user_ids_email_domain_dict, idhash_key_name='uid', idhash_val_name='email_domain')
    userid_date_country_code = user_data['registration_date'].dt.strftime('%Y%m%d') + user_data['registration_country_code_alpha'].astype(str)
    zero_pad = (userid_date_country_code.str.len() - 11).abs().apply(lambda x: '0'*x)
    user_data['userid'] = userid_date_country_code + zero_pad + user_data['uid'].astype(str).str[-5:]
    # add hash data lists
    user_data['device_hash'] = gen_obj_idhash_series(idhashes_props_dict=device_obj.device_hashes_props_dict, n_counts_series=user_data['n_devices'])
    user_data['card_hash'] = gen_obj_idhash_series(idhashes_props_dict=card_obj.card_hashes_props_dict, n_counts_series=user_data['n_cards'])
    user_data['ip_hash'] = gen_obj_idhash_series(idhashes_props_dict=ip_obj.ip_hashes_props_dict, n_counts_series=user_data['n_ips'])
    user_data['transaction_hash'] = gen_obj_idhash_series(idhashes_props_dict=transaction_obj.transaction_hashes_props_dict, n_counts_series=user_data['n_transactions'])
    user_data['application_hash'] = user_data['n_applications'].apply(lambda x: list(np.random.choice(a = list(application_obj.application_hashes_props_dict.keys()), p = list(application_obj.application_hashes_props_dict.values()), replace = True, size = x)))
    # drop excess columns
    drop_columns = ['n_devices', 'n_cards', 'n_ips', 'n_applications', 'n_transactions']
    user_data = user_data.drop(columns = drop_columns)
    # create a hash value for the dataset (to distinguish between different iterations)
    user_data['itr_hash'] = gen_random_hash(size=1)[0]
    return user_data