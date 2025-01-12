import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from beartype import beartype

class Application:

    @beartype
    def __init__(
        self, 
        n_application_hashes:int
        ):
        """
        The randomly generated application data model object.

        Parameters
        ----------
        n_application_hashes : int
            The number of application hashes to generate.

        Attributes
        ----------
        n_application_hashes : int
            The number of application hashes generated.
        lam : float
            The lambda parameter of the squared poisson distribution used to generate the application hash counts.
        application_hashes_cnts_dict : dict
            The application hash counts dictionary.
        application_hashes_props_dict : dict
            The application hash proportions dictionary.
        """
        self.n_application_hashes = n_application_hashes
        self.lam = cons.data_model_poisson_params["application"]["lambda"]
        self.power = cons.data_model_poisson_params["application"]["power"]
        self.payment_channels = cons.data_model_payment_channels
        self.application_hashes_cnts_dict = gen_idhash_cnt_dict(idhash_type="hash", n=self.n_application_hashes, lam=self.lam)
        self.application_hashes_props_dict = cnt2prop_dict(self.application_hashes_cnts_dict)
        self.application_hashes_payment_channel_dict = self.gen_transaction_payment_channel(list(self.application_hashes_cnts_dict.keys()), self.payment_channels)

    @beartype
    def gen_transaction_payment_channel(
        self,
        application_hashes:list,
        payment_channels:dict
        ) -> dict:
        """
        Generates a dictionary of random application payment channels.

        Parameters
        ----------
        application_hashes : list
            The application hashes.
        payment_channels : dict
            The population proportion of payment channels.

        Returns
        -------
        dict
            A dictionary of transaction payment channels.
        """
        # randomly sample payment channels based on population proportions
        transactoin_payment_channels = list(
            np.random.choice(
                a=list(payment_channels.keys()),
                p=list(payment_channels.values()),
                replace=True,
                size=len(application_hashes),
            )
        )
        # return payment channels and application hashes
        application_hashes_payment_channels_dict = dict(zip(application_hashes, transactoin_payment_channels))
        return application_hashes_payment_channels_dict
