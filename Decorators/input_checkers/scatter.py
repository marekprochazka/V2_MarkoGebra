from Static.constants import CACHE, CHANGES_CACHE, ERRORS, DATA, ACTION, ID, TYPE, INFO, NAME
from Utils.uuid import format_existing_uuid


# CONVERTING DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS
# IF THERE ARE ANY ERRORS THEY ARE ALSO RETURNED
def check_scatter_input(fun):
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS: errors}
        try:
            int(cache[1])
        except ValueError:
            checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'x' musí být celé číslo"})
        try:
            int(cache[2])
        except ValueError:
            checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'y' musí být celé číslo"})
        try:
            float(cache[5])
        except:
            checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'Vel.' musí být číslo číslo"})

        if not checked_data[ERRORS]:
            checked_data[CACHE] = (cache[0],
                                   int(cache[1]),
                                   int(cache[2]),
                                   str(cache[3]),
                                   str(cache[4]),
                                   float(cache[5]))

            checked_data[CHANGES_CACHE] = {ACTION: changes_cache[ACTION],
                                           DATA: (int(cache[1]), int(cache[2]), str(cache[3]), str(cache[4]),
                                                  float(cache[5])),
                                           ID: format_existing_uuid(cache[0]),
                                           TYPE: changes_cache[TYPE]}

        return checked_data

    return wrapper
