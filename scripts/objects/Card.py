import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_country_codes_dict import gen_country_codes_dict
from utilities.gen_shared_idhashes import gen_shared_idhashes


class Card:
    """The randomly generated card data model object 
    
    Parameters
    ----------
    n_card_hashes : int
        The number of card hashes to generate
    
    Attributes
    ----------
    n_card_hashes : int
        The number of card hashes generated
    card_types_dict : dict
        The population proportions of card types 
    lam : float
        The lambda parameter of the squared poisson distribution used to generate the card hash counts
    prop_shared_card_hashes : float
        The population proportion of shared card hashes
    card_hashes_cnts_dict : dict
        The card hash counts dictionary
    card_hashes_props_dict : dict
        The card hash proportions dictionary
    card_hashes_type_dict : dict
        The card hash types dictionary
    card_hashes_country_code_dict : dict
        The card hash country codes dictionary
    card_hashes_shared_props_dict : dict
        The shared card hash proportions dictionary
    """

    def __init__(self, n_card_hashes):
        self.n_card_hashes = n_card_hashes
        self.card_types_dict = cons.card_types_dict
        self.lam = cons.poisson_lambda_params["card"]
        self.prop_shared_card_hashes = cons.shared_entities_dict["card"]
        self.card_hashes_cnts_dict = gen_idhash_cnt_dict(
            idhash_type="hash", n=self.n_card_hashes, lam=self.lam
        )
        self.card_hashes_props_dict = cnt2prop_dict(self.card_hashes_cnts_dict)
        self.card_hashes_type_dict = self.gen_card_type(
            list(self.card_hashes_cnts_dict.keys()), self.card_types_dict
        )
        self.card_hashes_country_code_dict = gen_country_codes_dict(
            self.card_hashes_cnts_dict
        )
        self.card_hashes_shared_props_dict = gen_shared_idhashes(
            self.card_hashes_cnts_dict, self.prop_shared_card_hashes
        )

    def gen_card_type(self, card_hashes, card_types_dict):
        """Generates a dictionary of random card types
        
        Parameters
        ----------
        card_hashes : list
            The card hashes
        card_types_dict : dict
            The population proportions of card types 
        
        Returns
        -------
        dict
            A dictionary of card hash prices
        """
        # randomly choose card types based on the population proportions of card types
        card_types = np.random.choice(
            a=list(card_types_dict.keys()),
            p=list(card_types_dict.values()),
            size=len(card_hashes),
            replace=True,
        )
        # return the card hashes and card types
        card_hashes_type_dict = dict(zip(card_hashes, card_types))
        return card_hashes_type_dict
