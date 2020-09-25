import pickle
from Globals.variables import Variables as V
from Static.constants import GRAPHING_METHOD,MAX_WIDTH,MAX_HEIGHT
from Data.path import get_path
import numpy

class ShowFrame:
    def __init__(self,main):
        self.main = main
        self.data = dict

    def show_Setup_Frame(self,cont=None):
        self.data = self.__load_data()
        print(self.data)
        to_animate = 2
        V.new_math["SC"] = numpy.append(V.new_math["SC"],{"foo":2,1:"foo"})
        self.__append_data(to_animate)
        self.__save_data()





    def __load_data(self):
        with open(get_path() + "\data.pkl", "rb") as pckl:
            return pickle.load(pckl)
    def __save_data(self):
        with open(get_path() + "\data.pkl", "wb") as pckl:
            pickle.dump(self.data,pckl)
    def __append_data(self, to_animate:int):
        self.data[to_animate] = "foo"
    def __clear_data(self):
        with open(get_path() + "\data.pkl", "wb") as pckl:
            pickle.dump({},pckl)




