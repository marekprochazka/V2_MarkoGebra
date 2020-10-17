from Globals.variables import Variables as V
from math import floor
import numpy as np

#TODO
class NoiseUpdate:
    def __init__(self,main):
        self.main = main

    def create_basic_gen(self, number, dispersion, col):
        V.basic_gen = [np.random.rand(number), np.random.rand(number)]
        self.update_dispersion(dispersion, col)

    def update_dispersion(self, dispersion, col):
        V.noises[0] = [[floor(V.basic_gen[0][indx] * dispersion), floor(V.basic_gen[1][indx] * dispersion), ".", col, 1] for
                     indx, gn in enumerate(V.basic_gen[0])]

    def lock_noise(self, disper, num):
        V.noises.append(V.noises[0])
        V.dispersion.append(disper)
        V.number.append(num)
        V.coordinates_all_list.append([num, disper, V.noises[-1][0][2], V.noises[-1][0][3], V.noises[-1][0][4]])
        self.main.update_list_view()