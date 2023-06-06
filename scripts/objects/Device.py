import string
import numpy as np
import cons
from utilities.gen_idhash_cnt_dict import gen_idhash_cnt_dict
from utilities.cnt2prop_dict import cnt2prop_dict
from utilities.gen_shared_idhashes import gen_shared_idhashes


class Device:
    """The randomly generated device data model object 
    
    Parameters
    ----------
    n_device_hashes : int
        The number of device hashes to generate
    n_device_types : int
        The number of device types to generate
    
    Attributes
    ----------
    n_device_hashes : int
        The number of device hashes generated
    n_device_types : int
        The number of device types generated
    lam : float
        The lambda parameter of the squared poisson distribution used to generate the device hash counts
    prop_shared_device_hashes : float
        The population proportion of shared device hashes
    device_hashes_cnts_dict : dict
        The device hash counts dictionary
    device_hashes_props_dict : dict
        The device hash proportions dictionary
    device_hashes_type_dict : dict
        The device hash types dictionary
    device_hashes_shared_props_dict : dict
        The shared device hash proportions dictionary
    """

    def __init__(self, n_device_hashes, n_device_types):
        self.n_device_hashes = n_device_hashes
        self.n_device_types = n_device_types
        self.lam = cons.poisson_lambda_params["device"]
        self.prop_shared_device_hashes = cons.shared_entities_dict["device"]
        self.device_hashes_cnts_dict = gen_idhash_cnt_dict(
            idhash_type="hash", n=self.n_device_hashes, lam=self.lam
        )
        self.device_hashes_props_dict = cnt2prop_dict(self.device_hashes_cnts_dict)
        self.device_hashes_type_dict = self.gen_device_type(
            list(self.device_hashes_cnts_dict.keys()),
            n_device_types=self.n_device_types,
        )
        self.device_hashes_shared_props_dict = gen_shared_idhashes(
            self.device_hashes_cnts_dict, self.prop_shared_device_hashes
        )

    def gen_device_type(self, device_hashes, n_device_types):
        """Generates a dictionary of random device types
        
        Parameters
        ----------
        device_hashes : list
            The device hashes
        n_device_types : int
            The number of available device types to generated
        
        Returns
        -------
        dict
            A dictionary of device hash types
        """
        # create an empty list to hold the different device types
        device_types = []
        # define a list of letters and digits
        letters = list(set(string.ascii_letters.upper()))
        digits = list(string.digits)
        # iterate up to the number of devices
        for i in range(n_device_types):
            # generate a device type name
            prefix = "".join(np.random.choice(letters, size=3, replace=False))
            suffix = "".join(np.random.choice(digits, size=3, replace=False))
            device_type = f"{prefix}-{suffix}"
            # append device type name to device types list
            device_types.append(device_type)
        # randomly choose different device types
        device_types = list(np.random.choice(a=device_types, size=len(device_hashes)))
        # return device hashes and types
        device_hashes_type_dict = dict(zip(device_hashes, device_types))
        return device_hashes_type_dict
