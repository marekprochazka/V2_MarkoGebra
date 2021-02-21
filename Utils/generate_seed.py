from random import randint, seed
from time import time
def generate_seed():
    seed(round(time()*1000))
    return randint(1,2**32-1)