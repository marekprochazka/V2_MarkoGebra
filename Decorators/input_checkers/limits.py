from Static.constants import X, Y, MIN, MAX
from Globals.variables import Variables as V


def check_limits_input(fun):
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        if check_value(X, data[X][MIN], data[X][MAX]) & check_value(Y, data[Y][MIN], data[Y][MAX]):
            data[X][MIN] = int(data[X][MIN])
            data[X][MAX] = int(data[X][MAX])
            data[Y][MIN] = int(data[Y][MIN])
            data[Y][MAX] = int(data[Y][MAX])
            V.limits = data

    return wrapper


def check_value(axis, min, max):
    is_ok = True
    try:

        int(min)
    except ValueError:
        is_ok = False
        print(f"Chybný vstup na ose {axis} hodnota {min} je neplatná")
    try:
        int(max)
    except ValueError:
        is_ok = False
        print(f"Chybný vstup na ose {axis} hodnota {max} je neplatná")

    return is_ok
