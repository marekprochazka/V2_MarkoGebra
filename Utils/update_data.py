from Static.constants import ERRORS, CACHE, MATH, CHANGES_CACHE
from Globals.variables import Variables as V

def update_data(collector):
    # collect_data FUNCTION OF A PARTICULAR ROW
    data = collector()

    # ERRORS ARE ADDED TO DATA IN DECORATORS IF THERE
    # WERE ANY WRONG INPUTS
    if data[ERRORS]:
        print(data[ERRORS])
    else:
        # IF NO ERRORS
        # FINDING RIGHT VALUE IN CACHE BY IT'S id
        # UPDATING THE VALUE
        for index, value in enumerate(V.cache[0]):
            if value[0] == data[CACHE][0]:
                V.cache[0][index] = data[CACHE]
                break
        # IF IT'S MATH GRAPHING IT SE NECESSARY TO ALSO CHECK SECOND CACHE
        if V.to_animate == MATH:
            for index, value in enumerate(V.cache[1]):
                if value[0] == data[CACHE][0]:
                    V.cache[1][index] = data[CACHE]
                    break

        # DATA FOR changes_cache IS PREPARED IN DECORATOR
        # ONLY APPENDING HERE
        V.changes_cache.append(data[CHANGES_CACHE])