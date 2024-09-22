import pandas as pd

def gen_obj_idhash_series(idhashes_props_dict, n_counts_series):
    """
    """
    # create an exploded series for idhashes within the entity object
    obj_idhash_series = pd.Series(data=idhashes_props_dict.keys(), index=n_counts_series.apply(lambda x: range(x)).explode().index)
    # group by uid index and collate idhashes as lists
    obj_idhash_agg = obj_idhash_series.groupby(level=0).apply(lambda series: series.to_list())
    return obj_idhash_agg