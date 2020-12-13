from Utils.generate_seed import generate_seed
import numpy as np

def generate_new_noise(dispersion: float, quantity: int):
    r_seed = generate_seed()
    np.random.seed(r_seed)
    generation = np.random.random((quantity, 2))
    generation = np.floor(((generation * 2) - 1) * dispersion)
    return generation, r_seed


def generate_with_seed():
    pass


print(generate_new_noise(50, 153))
