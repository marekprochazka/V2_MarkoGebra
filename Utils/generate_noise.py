from Utils.generate_seed import generate_seed
from random import randint, seed
import numpy as np


def generate_noise(dispersion: int, quantity: int):
    r_seed = generate_seed()
    seed(r_seed)
    generation = [[randint(-dispersion, dispersion), randint(-dispersion, dispersion)] for _ in range(quantity)]
    return np.array(generation), r_seed


# print(generate_noise(50, 150))
