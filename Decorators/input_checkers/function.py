from Static.constants import CACHE, CHANGES_CACHE, ERRORS, ACTION, DATA, ID, TYPE, NAME, INFO
from Utils.uuid import format_existing_uuid
from Static.function_input_constants import *

import numpy as np
import mpmath as m

# CONVERTING DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS
# IF THERE ARE ANY ERRORS THEY ARE ALSO RETURNED
def check_function_input(fun):
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        cache = data[CACHE]
        changes_cache = data[CHANGES_CACHE]
        errors = data[ERRORS]
        checked_data = {ERRORS: errors}
        # TODO function checkers
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

def replace_for_math(fun:str):
    function = fun
    for value in ALLOWED_WORDS:
        function = function.replace(value,WORD_TO_MATH_EQUIVALENT[value])
    return function

def evaluate_function(fun):
    try:
        x = 1
        return eval(fun)
    except SyntaxError:
        return SyntaxError

print(ALLOWED_WORDS)
print(ALLOWED_MARKS)
fn = "x+1*ln(10.15)***e+sin(20)"
print(has_forbidden_character(fn))
new_fn = replace_for_math(fn)
print(new_fn)
print(evaluate_function(new_fn))