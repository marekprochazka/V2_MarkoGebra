from Static.constants import CACHE, ERRORS, NAME, INFO


def bar_input_controller(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        cache = data[CACHE]
        # 1 name , 2 value, 4 width
        if not cache[1]:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'Název' musí být vyplněna"})
        if not cache[2]:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'Množství' musí být vyplněna"})
        if not cache[4]:
            data[ERRORS].append({NAME: "input error", INFO: "Hodnota 'Šířka' musí být vyplněna"})
        return data

    return wrapper
