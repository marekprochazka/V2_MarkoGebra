# import numpy as np
# import mpmath as m

ALLOWED_WORDS = ("sin", "cos", "tan", "cotg", "ln", "pi", "e")
ALLOWED_MARKS = ("+", "-", "*", "/", "(", ")", ".", "x")

WORD_TO_MATH_EQUIVALENT = {
    "sin": "np.sin",
    "cos": "np.cos",
    "tan": "np.tan",
    "cotg": "m.cot",
    "ln": "np.log",
    "pi": "np.pi",
    "e": "np.e",
}
