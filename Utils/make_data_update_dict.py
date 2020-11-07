from Static.constants import CACHE, CHANGES_CACHE, TYPE, DATA, ID,ACTION
from Globals.calculated import data_update_dict_base

def make_data_update_dict(id,values,action,type=None):
    data = data_update_dict_base()
    data[CACHE] = id+values
    if type:
        data[CHANGES_CACHE][TYPE] = type
    data[CHANGES_CACHE][DATA] = values
    data[CHANGES_CACHE][ID] = id
    data[CHANGES_CACHE][ACTION] = action
    return data