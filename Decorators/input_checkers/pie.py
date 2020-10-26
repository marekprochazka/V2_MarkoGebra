from Static.constants import CACHE, CHANGES_CACHE, ERRORS, ACTION, DATA, ID, NAME, INFO
from Utils.uuid import format_existing_uuid


# CONVERTING DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS
# IF THERE ARE ANY ERRORS THEY ARE ALSO RETURNED
def check_pie_input(fun):
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS: errors}
        try:
            float(cache[1])
        except ValueError:
            checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'Množství' musí být číslo"})
        try:
            float(cache[4])
        except ValueError:
            checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'výstup' musí být číslo"})
        if not checked_data[ERRORS]:
            checked_data[CACHE] = (cache[0],
                                   float(cache[1]),
                                   str(cache[2]),
                                   str(cache[3]),
                                   float(cache[4]))

            checked_data[CHANGES_CACHE] = {ACTION: changes_cache[ACTION],
                                           DATA: (float(cache[1]),
                                                  str(cache[2]),
                                                  str(cache[3]),
                                                  float(cache[4])),
                                           ID: format_existing_uuid(cache[0])}

        return checked_data

    return wrapper
