from Static.function_input_constants import ALLOWED_WORDS, WORD_TO_MATH_EQUIVALENT


def replace_for_math(fun: str):
    function = fun
    for value in ALLOWED_WORDS:
        function = function.replace(value, WORD_TO_MATH_EQUIVALENT[value])
    return function