from Static.constants import CACHE, CHANGES_CACHE, ERRORS, DATA, ACTION, ID, TYPE
from Utils.uuid import format_existing_uuid


def check_scatter(fun):
    def wrapper(*args,**kwargs):
        data = fun(*args,**kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS:[]}
        try:
            checked_data[CACHE] = (cache[0],
                                   int(cache[1]),
                                   int(cache[2]),
                                   str(cache[3]),
                                   str(cache[4]),
                                   float(cache[5]))
        except:
            checked_data[ERRORS] = errors.append("error")

        try:
            checked_data[CHANGES_CACHE] = {ACTION: changes_cache[ACTION],
                                           DATA: (int(cache[1]), int(cache[2]), str(cache[3]), str(cache[4]),
                                                  float(cache[5])),
                                           ID: format_existing_uuid(cache[0]),
                                           TYPE: changes_cache[TYPE]}
        except:
            checked_data[ERRORS] = errors.append("error")

        return checked_data

    return wrapper
