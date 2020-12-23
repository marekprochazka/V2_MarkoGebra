from Static.constants import CACHE, ERRORS, NAME, INFO


def scatter_input_controller(func):
    def wrapper(*args,**kwargs):
        data = func(*args, **kwargs)
        cache = data[CACHE]
        if not cache[1]:
            data[ERRORS].append({NAME: "input error", INFO:"Hodnota 'x' musí být vyplněna"})
        if not cache[2]:
            data[ERRORS].append({NAME: "input error", INFO:"Hodnota 'y' musí být vyplněna"})
        if not cache[5]:
            data[ERRORS].append({NAME: "input error", INFO:"Hodnota 'velikost' musí být vyplněna"})
        return data
    return wrapper
