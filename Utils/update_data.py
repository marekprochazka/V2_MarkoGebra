from Static.constants import ERRORS, CACHE, MATH, CHANGES_CACHE, ACTION, CREATE, TYPE, FUNCTION, SCATTER, NAME, INFO
from Globals.variables import Variables as V
from GUI.error_popup import error_popup


def update_data(data, update_fun=None, limits_fun=None):
    data

    # ERRORS ARE ADDED TO DATA IN DECORATORS IF THERE
    # WERE ANY WRONG INPUTS
    if data[ERRORS]:
        error_popup({NAME: ";".join([error[NAME] for error in data[ERRORS]]),
                     INFO: "\n".join([error[INFO] for error in data[ERRORS]])})
    else:
        if data[CHANGES_CACHE][ACTION] == CREATE:
            if V.to_animate == MATH:
                if data[CHANGES_CACHE][TYPE] == SCATTER:
                    V.cache[0].append(data[CACHE])
                else:
                    V.cache[1].append(data[CACHE])
            else:
                V.cache[0].append(data[CACHE])
        else:
            # IF NO ERRORS
            # FINDING RIGHT VALUE IN CACHE BY IT'S id
            # UPDATING THE VALUE
            for index, value in enumerate(V.cache[0]):
                if value[0] == data[CACHE][0]:
                    V.cache[0][index] = data[CACHE]
                    break
            # IF IT'S MATH GRAPHING IT IS NECESSARY TO ALSO CHECK SECOND CACHE
            if V.to_animate == MATH:
                for index, value in enumerate(V.cache[1]):
                    if value[0] == data[CACHE][0]:
                        V.cache[1][index] = data[CACHE]
                        break

        # DATA FOR changes_cache IS PREPARED IN DECORATOR
        # ONLY APPENDING HERE
        V.changes_cache.append(data[CHANGES_CACHE])
        if update_fun:
            update_fun()

        if V.is_auto_update:
            if limits_fun:
                limits_fun(data[CACHE][1], data[CACHE][2])
