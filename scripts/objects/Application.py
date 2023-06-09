import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict


class Application:
    """The randomly generated application data model object

    Parameters
    ----------
    n_application_hashes : int
        The number of application hashes to generate

    Attributes
    ----------
    n_application_hashes : int
        The number of application hashes generated
    lam : float
        The lambda parameter of the squared poisson distribution used to generate the application hash counts
    application_hashes_cnts_dict : dict
        The application hash counts dictionary
    application_hashes_props_dict : dict
        The application hash proportions dictionary
    application_hashes_prices_dict : dict
        The application hash prices dictionary
    """

    def __init__(self, n_application_hashes):
        self.n_application_hashes = n_application_hashes
        self.lam = cons.data_model_poisson_lambda_params["application"]
        self.application_hashes_cnts_dict = gen_idhash_cnt_dict(
            idhash_type="hash", n=self.n_application_hashes, lam=self.lam
        )
        self.application_hashes_props_dict = cnt2prop_dict(
            self.application_hashes_cnts_dict
        )
        self.application_hashes_prices_dict = self.gen_application_prices(
            list(self.application_hashes_cnts_dict.keys())
        )

    def gen_application_prices(self, application_hashes, loc=0, scale=2):
        """Generates a dictionary of random application hash prices

        Parameters
        ----------
        application_hashes : list
            The application hashes

        Returns
        -------
        dict
            A dictionary of application hash prices
        """
        # randomly sample application prices from an absolute normal distribution with mean 0 and standard deviation 2
        app_prices = np.round(
            np.abs(np.random.normal(loc=loc, scale=scale, size=len(application_hashes)))
            ** 2,
            2,
        )
        # return the application hashes and prices
        app_prices_dict = dict(zip(application_hashes, app_prices))
        return app_prices_dict
