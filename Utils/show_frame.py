from Globals.variables import Variables as V
from Static.constants import GRAPHING_METHOD,MAX_WIDTH,MAX_HEIGHT
import json


class ShowFrame:

    def __init__(self,main):
        self.main = main

    def show_Setup_Frame(self, cont=None):
        if V.to_animate == 1:
            with(open("math.json", "w")) as save:
                save.truncate()
                data = [V.coordinates_scatter, [x[2:] for x in V.coordinates_plot]]
                json.dump(data, save)

        if V.to_animate == 2:
            with(open("pie.json", "w")) as save:
                save.truncate()
                data = [V.slices, V.cols, V.activities, V.explode]
                json.dump(data, save)

        if V.to_animate == 3:
            with(open("bar.json", "w")) as save:
                save.truncate()
                data = [V.bars, V.coordinates_all_list]
                json.dump(data, save)

        if V.to_animate == 4:
            with(open("noise.json", "w")) as save:
                save.truncate()
                data = [V.noises[1:], V.coordinates_all_list, V.dispersion, V.number]

                json.dump(data, save)

        if cont != None:
            new_frame = cont(self.main.SetupContainer, self.main)
            V.to_animate = GRAPHING_METHOD[new_frame.old_type]

            if self.main._frame is not None:
                for child in self.main._frame.winfo_children():
                    child.destroy()
                self.main._frame.destroy()
            self.main._frame = new_frame
            self.main._frame.place(x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15, height=MAX_HEIGHT * 45, width=MAX_WIDTH * .40)

        V.coordinates_plot = []
        V.coordinates_scatter = []
        V.slices = []
        V.cols = []
        V.activities = []
        V.explode = []
        V.start_angle = 90
        V.bars = []
        V.noises = [[[0, 0, ".", "#fff", 1], [0, 0, ".", "#fff", 1]]]
        V.dispersion = []
        V.number = []
        V.basic_gen = []

        V.coordinates_all_list = []

        if V.to_animate == 1:
            with(open("math.json", "r")) as save:
                data = json.loads(save.read())
                if data[0] != []:
                    for val in data[0]:
                        self.main.add_point_scatter(val[0], val[1], val[2], val[3], val[4])
                if data[0] != []:
                    for val in data[1]:
                        self.main.add_plot_from_function(val[3], val[0], val[1], val[2])

        elif V.to_animate == 2:
            with(open("pie.json", "r")) as save:
                data = json.loads(save.read())
                if data != [[], [], [], []]:
                    for index in range(len(data[0])):
                        self.main.add_pie_data(data=[data[0][index], data[2][index], data[1][index]],
                                          expl=int(data[3][index]))

        elif V.to_animate == 3:
            with(open("bar.json", "r")) as save:
                data = json.loads(save.read())
                if data != [[], []]:
                    V.bars = data[0]
                    V.coordinates_all_list = data[1]

        elif V.to_animate == 4:
            with(open("noise.json", "r")) as save:
                data = json.loads(save.read())
                if data != [[], [], [], []]:
                    V.noises = [[[0, 0, ".", "#fff", 1], [0, 0, ".", "#fff", 1]]] + data[0]
                    V.coordinates_all_list = data[1]
                    V.dispersion = data[2]
                    V.number = data[3]

        self.main.update_table()