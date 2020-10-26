from Static.constants import CACHE, CHANGES_CACHE, ERRORS, ACTION, DATA, ID, TYPE, NAME, INFO
from Utils.uuid import format_existing_uuid


# CONVERTING DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS
# IF THERE ARE ANY ERRORS THEY ARE ALSO RETURNED
def check_function_input(fun):
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS: errors}
        # TODO function checkers
        try:
            float(cache[4])
        except ValueError:
            checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'Vel.' musí být číslo"})
        if not checked_data[ERRORS]:
            checked_data[CACHE] = (cache[0],
                                   str(cache[1]),
                                   str(cache[2]),
                                   str(cache[3]),
                                   float(cache[4]))

            checked_data[CHANGES_CACHE] = {
                ACTION: changes_cache[ACTION],
                DATA: (str(cache[1]), str(cache[2]), str(cache[3]), float(cache[4])),
                ID: format_existing_uuid(cache[0]),
                TYPE: changes_cache[TYPE]
            }

        return checked_data

    return wrapper
