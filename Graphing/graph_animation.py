from Globals.variables import Variables as V
from Graphing.setup import a
import numpy as np
from Static.constants import MATH,PIE,BAR,NOISE

class GraphAnimation:
    def Go(self, i):
        if V.to_animate == MATH:
            self.animate_graphs()
        elif V.to_animate == PIE:
            self.animate_pie()
        elif V.to_animate == BAR:
            self.animate_bar()
        elif V.to_animate == NOISE:
            self.animate_noise()
    
    def animate_graphs(i):
        a.clear()
        a.axis("equal")

        for coord in V.cache[0]:
            a.scatter(coord[1], coord[2], marker=coord[3], color=coord[4], linewidths=float(coord[5]))
        for coord in V.cache[1]:
            x = np.linspace(-5,5,100)



            # for limit in range(len(y)):
            #     if y[limit] > V.lim1 or y[limit] < V.lim2:
            #         y[limit] = None
            a.plot(x, eval(coord[1]), linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))

    def animate_pie(i):
        a.clear()
        slices,activities,cols,explode = [],[],[],[]
        for val in V.cache[0]:
            slices.append(val[1])
            activities.append(val[2])
            cols.append(val[3])
            explode.append(val[4])
        a.pie(slices, labels=activities, colors=cols, explode=explode, startangle=V.start_angle)

    def animate_bar(self):
        a.clear()
        a.axis("auto")
        for bar in V.cache[0]:
            a.bar([str(bar[1])], [int(bar[2])], color=bar[3], width=float(bar[4]))

    #TODO
    def animate_noise(self):
        a.clear()
        a.axis("equal")
        for noise in V.noises:
            for coord in noise:
                a.scatter(coord[0], coord[1], marker=coord[2], color=coord[3], linewidths=float(coord[4]))

