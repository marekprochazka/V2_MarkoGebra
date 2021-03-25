from Static.constants import CACHE, ERRORS, NAME, INFO


def pie_input_controller(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        cache = data[CACHE]
        if not cache[1]:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'množství' musí být vyplněna"})
        if not cache[4] and cache[4] != 0.:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'výstup' musí být vyplněna"})
        return data

    return wrapper
