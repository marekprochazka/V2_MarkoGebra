from Static.constants import CACHE, CHANGES_CACHE, ERRORS, ACTION, DATA, ID, TYPE, NAME, INFO
from Utils.uuid import format_existing_uuid
from Static.function_input_constants import *
from Utils.replace_for_math import replace_for_math

# NECESSARY TO BE IMPORTED BECAUSE OF EVAL CHECK
import numpy as np




# CONVERTING DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS
# IF THERE ARE ANY ERRORS THEY ARE ALSO RETURNED
def check_function_input(fun):
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS: errors}

        forbidden_characters = has_forbidden_character(cache[1])
        if forbidden_characters:
            checked_data[ERRORS].append(
                {NAME: "CharacterError", INFO: f"Neplatný znak(y): {';'.join(forbidden_characters)}"})

        else:
            replaced_func = replace_for_math(cache[1])
            if evaluate_function_error(replaced_func):
                checked_data[ERRORS].append({NAME: "SyntaxError", INFO: "Neplatná syntaxe"})

            else:

                try:
                    float(cache[4])
                except ValueError:
                    checked_data[ERRORS].append({NAME: "ValueError", INFO: "Hodnota 'Vel.' musí být číslo"})
                if not checked_data[ERRORS]:
                    checked_data[CACHE] = (cache[0],
                                           str(cache[1]),
                                           str(cache[2]),
                                           str(cache[3]),
                                           float(cache[4]))

                    checked_data[CHANGES_CACHE] = {
                        ACTION: changes_cache[ACTION],
                        DATA: (str(cache[1]), str(cache[2]), str(cache[3]), float(cache[4])),
                        ID: format_existing_uuid(cache[0]),
                        TYPE: changes_cache[TYPE]
                    }

        return checked_data

    return wrapper


def has_forbidden_character(fun: str):
    function_string = fun
    error_chars = []
    for value in ALLOWED_WORDS:
        function_string = function_string.replace(value, "")
    for value in ALLOWED_MARKS:
        function_string = function_string.replace(value, "")
    for value in function_string:
        if not value.isdigit():
            error_chars.append(value)
    if not error_chars:
        return False
    return error_chars


def evaluate_function_error(fun):
    try:
        x = 1
        eval(fun)
        return False
    except SyntaxError:
        return True


