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

