# import numpy as np


ALLOWED_WORDS = ("sin", "cos", "tan", "ln", "pi", "e")
ALLOWED_MARKS = ("+", "-", "*", "/", "(", ")", ".", "x")

WORD_TO_MATH_EQUIVALENT = {
    "sin": "np.sin",
    "cos": "np.cos",
    "tan": "np.tan",
    "ln": "np.log",
    "pi": "np.pi",
    "e": "np.e",
}
