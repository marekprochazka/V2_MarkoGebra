from Utils.generate_seed import generate_seed
import numpy as np

def generate_noise(dispersion: float, quantity: int, seed=None):
    if not seed:
        r_seed = generate_seed()
    else: r_seed = seed
    np.random.seed(r_seed)
    generation = np.random.random((quantity, 2))
    generation = np.floor(((generation * 2) - 1) * dispersion)
    return generation, r_seed





# print(generate_noise(50, 153))
