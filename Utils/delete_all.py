from Globals.variables import Variables as V
class DeleteAll:
    def __init__(self,main):
        self.main = main

    def delete_all(self):
        if V.to_animate == 1:
            V.coordinates_all_list = []
            V.coordinates_plot = []
            V.coordinates_scatter = []
            self.main.update_table()
        elif V.to_animate == 2:
            V.slices = []
            V.cols = []
            V.activities = []
            V.explode = []
            V.coordinates_all_list = []
            self.main.update_table()
        elif V.to_animate == 3:
            V.bars = []
            V.coordinates_all_list = []
            self.main.update_table()
        elif V.to_animate == 4:
            V.coordinates_all_list = []
            V.noises = []
            V.dispersion = []
            V.number = []
            V.basic_gen = []
            self.main.update_table()