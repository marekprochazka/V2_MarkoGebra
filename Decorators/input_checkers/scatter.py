from Static.constants import CACHE, ERRORS, NAME, INFO


def scatter_input_controller(func):
    def wrapper(*args,**kwargs):
        data = func(*args, **kwargs)
        cache = data[CACHE]
        if cache[1] is None:
            data[ERRORS].append({NAME: "input error", INFO:"Hodnota 'x' musí být vyplněna"})
        if cache[2] is None:
            data[ERRORS].append({NAME: "input error", INFO:"Hodnota 'y' musí být vyplněna"})
        if cache[5] is None:
            data[ERRORS].append({NAME: "input error", INFO:"Hodnota 'velikost' musí být vyplněna"})
        return data
    return wrapper
