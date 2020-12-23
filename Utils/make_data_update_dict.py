from Static.constants import CACHE, CHANGES_CACHE, TYPE, DATA, ID, ACTION, ERRORS
from Globals.calculated import data_update_dict_base

# DICT FORMATTED FOR DATA UPDATE FUNCTION
def make_data_update_dict(id,values,action,type=None, noise=False, **kwargs):
    data = data_update_dict_base()
    if not noise:
        data[CACHE] = id+values
    else:
        data[CACHE] = id + values + (kwargs.get("noise_data"), )
    if type:
        data[CHANGES_CACHE][TYPE] = type
    data[CHANGES_CACHE][DATA] = values
    data[CHANGES_CACHE][ID] = id
    data[CHANGES_CACHE][ACTION] = action
    data[ERRORS] = []
    return data
