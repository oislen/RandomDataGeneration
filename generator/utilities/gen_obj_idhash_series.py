import pandas as pd

def gen_obj_idhash_series(idhashes_props_dict, n_counts_series):
    """Generates a series of entity idhash lists using the entity counts per user Series and idhashes proportions dictionary

    Parameters
    ----------
    idhashes_props_dict : dict
        The idhash proportions dictionary
    n_counts_series : pd.Series
        The entity counts for each uid as Series

    Returns
    -------
    pd.Series
        A Series of lists containing entity idhashes  for each user
    """
    # create an exploded series for idhashes within the entity object
    obj_idhash_series = pd.Series(data=idhashes_props_dict.keys(), index=n_counts_series.apply(lambda x: range(x)).explode().index)
    # group by uid index and collate idhashes as lists
    obj_idhash_agg = obj_idhash_series.groupby(level=0).apply(lambda series: series.to_list())
    return obj_idhash_agg