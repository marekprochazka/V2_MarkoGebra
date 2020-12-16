from Static.constants import CACHE, CHANGES_CACHE, ERRORS, NAME, INFO, ACTION, DATA, ID


def check_noise_input(fun):
    def wrapper(*args,**kwargs):
        data = fun(*args,**kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS: errors}
        if not isinstance(cache[2],int):
            checked_data[ERRORS].append({NAME: "TODO ERROR", INFO: "Hodnota 'Rozptyl' musí být celé číslo"})
        if not isinstance(cache[3],int):
            checked_data[ERRORS].append({NAME: "TODO ERROR", INFO: "Hodnota 'Počet' musí být celé číslo"})
        if not checked_data[ERRORS]:
            checked_data[CACHE] = cache
            checked_data[CHANGES_CACHE] = changes_cache

        return checked_data
    return wrapper

