from Static.constants import DATA_UPDATE_DICT, CACHE, CHANGES_CACHE, TYPE, SCATTER, DATA, ID,ACTION


def make_data_update_dict(id,values,action,type=None):
    data = DATA_UPDATE_DICT
    data[CACHE] = id+values
    if type:
        data[CHANGES_CACHE][TYPE] = SCATTER
    data[CHANGES_CACHE][DATA] = values
    data[CHANGES_CACHE][ID] = id
    data[CHANGES_CACHE][ACTION] = action
    return data