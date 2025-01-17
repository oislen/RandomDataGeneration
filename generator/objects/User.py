import cons
import numpy as np
import pandas as pd
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_country_codes_dict import gen_country_codes_dict
from utilities.gen_dates_dict import gen_dates_dict
from beartype import beartype

class User:

    @beartype
    def __init__(
        self,
        n_user_ids:int,
        start_date:str,
        end_date:str,
        fpath_firstnames:str=cons.fpath_firstnames,
        fpath_lastnames:str=cons.fpath_lastnames,
        fpath_countrieseurope:str=cons.fpath_countrieseurope,
        fpath_domain_email:str=cons.fpath_domain_email
        ):
        """
        The randomly generated user data model object

        Parameters
        ----------
        n_user_ids : int
            The number of user uids to generate
        start_date : str
            The start date to generate users from
        end_date : str
            The end date to generate users till
        fpath_firstnames : str
            The full file path to the first names reference data, default is cons.fpath_firstnames.
        fpath_lastnames : str
            The full file path to the last names reference data, default is cons.fpath_lastnames.
        fpath_countrieseurope : str
            The full file path to the europe countries reference data, default is cons.fpath_countrieseurope.
        fpath_domain_email : str
            The full file path to the email domain reference daa, default is cons.fpath_domain_email.

        Attributes
        ----------
        n_user_ids : int
            The number of user ids generated
        start_date : str
            The date user ids are generated from, must be of the form '%Y-%m-%d'
        end_date : str
            The date user ids are generated till, must be of the form '%Y-%m-%d'
        lam : float
            The lambda parameter of the squared poisson distribution used to generate the user ids counts
        user_ids_cnts_dict : dict
            The user id counts dictionary
        user_ids_props_dict : dict
            The user id proportions dictionary
        user_ids_firstname_dict : dict
            The user id first names dictionary
        user_ids_lastname_dict : dict
            The user id last names dictionary
        user_ids_country_code_dict : dict
            The user id country codes dictionary
        user_ids_email_domain_dict : dict
            The user id email domains dictionary
        user_ids_dates_dict : dict
            The user id dates dictionary
        """
        self.n_user_ids = n_user_ids
        self.start_date = start_date
        self.end_date = end_date
        self.fpath_firstnames = fpath_firstnames
        self.fpath_lastnames = fpath_lastnames
        self.fpath_countrieseurope = fpath_countrieseurope
        self.fpath_domain_email = fpath_domain_email
        self.lam = cons.data_model_poisson_params["user"]["lambda"]
        self.power = cons.data_model_poisson_params["user"]["power"]
        self.user_ids_cnts_dict = gen_idhash_cnt_dict(idhash_type="id", n=self.n_user_ids, lam=self.lam)
        self.user_ids_props_dict = cnt2prop_dict(self.user_ids_cnts_dict)
        self.user_ids_country_code_dict = gen_country_codes_dict(self.user_ids_cnts_dict, self.fpath_countrieseurope)
        self.user_ids_firstname_dict = self.gen_user_firstname(self.fpath_firstnames)
        self.user_ids_lastname_dict = self.gen_user_lastname(self.fpath_lastnames)
        self.user_ids_email_domain_dict = self.gen_user_email_domain(self.fpath_domain_email)
        self.user_ids_dates_dict = gen_dates_dict(self.user_ids_cnts_dict, start_date=self.start_date, end_date=self.end_date)

    @beartype
    def gen_user_firstname(
        self,
        fpath_firstnames:str
        ) -> dict:
        """
        Generates a dictionary of random user id first names

        Parameters
        ----------
        fpath_firstnames : str
            The file path to the first names reference file

        Returns
        -------
        dict
            A dictionary of user id first names
        """
        # load in list of first names
        first_name_data = pd.read_csv(fpath_firstnames, header=None)
        # extract the user ids
        user_ids_list = list(self.user_ids_cnts_dict.keys())
        # randomly sample the first name list
        user_firstname_list = first_name_data[0].sample(n=self.n_user_ids, replace=True)
        # return the user ids first names
        user_ids_firstname_dict = dict(zip(user_ids_list, user_firstname_list))
        return user_ids_firstname_dict

    @beartype
    def gen_user_lastname(
        self,
        fpath_lastnames:str
        ) -> dict:
        """
        Generates a dictionary of random user id last names.

        Parameters
        ----------
        fpath_lastnames : str
            The file path to the last names reference file.

        Returns
        -------
        dict
            A dictionary of user id last names.
        """
        # load in list of last names
        last_name_data = pd.read_csv(fpath_lastnames, header=None)
        # extract the user ids
        user_ids_list = list(self.user_ids_cnts_dict.keys())
        # randomly sample the last name list
        user_lastname_list = last_name_data[0].sample(n=self.n_user_ids, replace=True)
        # return the user ids last names
        user_ids_lastname_dict = dict(zip(user_ids_list, user_lastname_list))
        return user_ids_lastname_dict

    @beartype
    def gen_user_email_domain(
        self,
        fpath_domain_email:str
        ) -> dict:
        """
        Generates a dictionary of random user id email domains

        Parameters
        ----------
        fpath_domain_email : str
            The file path to the email domains reference file

        Returns
        -------
        dict
            A dictionary of user id email domains
        """
        # load domain names data
        email_domain_data = pd.read_csv(fpath_domain_email, index_col=0)
        # calculate the proportion of email domains
        email_domain_data["proportion"] = email_domain_data["proportion"].divide(email_domain_data["proportion"].sum())
        # convert email domain proportions to a dictionary
        email_domain_dict = email_domain_data.set_index("domain").to_dict()["proportion"]
        # extract the user ids
        user_ids_list = list(self.user_ids_cnts_dict.keys())
        # randomly choose the email domains based on proportions
        user_email_domain_list = list(
            np.random.choice(
                a=list(email_domain_dict.keys()),
                p=list(email_domain_dict.values()),
                replace=True,
                size=len(user_ids_list),
            )
        )
        # return the user ids email domains
        user_ids_email_domain_dict = dict(zip(user_ids_list, user_email_domain_list))
        return user_ids_email_domain_dict
