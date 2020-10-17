from Static.constants import CACHE, CHANGES_CACHE, ERRORS, ACTION, DATA, ID
from Utils.uuid import format_existing_uuid

def check_pie_input(fun):
    def wrapper(*args,**kwargs):
        data = fun(*args,**kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS:errors}

        try:
            checked_data[CACHE]=(cache[0],
                                 float(cache[1]),
                                 str(cache[2]),
                                 str(cache[3]),
                                 float(cache[4]))
        except:
            checked_data[ERRORS].append("cache error")

        try:
            checked_data[CHANGES_CACHE] = {ACTION:changes_cache[ACTION],
                                           DATA:(float(cache[1]),
                                                 str(cache[2]),
                                                 str(cache[3]),
                                                 float(cache[4])),
                                           ID:format_existing_uuid(cache[0])}
        except:
            checked_data[ERRORS].append("changes error")

        return checked_data

    return wrapper