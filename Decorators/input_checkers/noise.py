from Static.constants import CACHE, ERRORS, NAME, INFO


def noise_input_controller(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        cache = data[CACHE]
        if not cache[2]:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'Rozptyl' musí být vyplněna"})
        if not cache[3]:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'Množství' musí být vyplněna"})
        return data

    return wrapper
