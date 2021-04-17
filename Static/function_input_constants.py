# import numpy as np


ALLOWED_WORDS = ("sin", "cos", "tan", "ln", "pi", "e")
ALLOWED_MARKS = ("+", "-", "*", "/", "(", ")", ".", "x")
ALLOWED_WORDS_FOR_INPUT = ("s", "i", "n", "c", "o", "s", "t", "a", "n", "l", "n", "p", "i", "e")

WORD_TO_MATH_EQUIVALENT = {
    "sin": "np.sin",
    "cos": "np.cos",
    "tan": "np.tan",
    "ln": "np.log",
    "pi": "np.pi",
    "e": "np.e",
}
