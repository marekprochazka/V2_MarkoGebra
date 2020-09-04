from Globals.variables import Variables as V
from Graphing.setup import a
import numpy as np

class GraphAnimation:
    def Go(self, i):
        if V.to_animate == 1:
            self.animate_graphs()
        elif V.to_animate == 2:
            self.animate_pie()
        elif V.to_animate == 3:
            self.animate_bar()
        elif V.to_animate == 4:
            self.animate_noise()

    def animate_graphs(i):
        a.clear()
        a.axis("equal")

        for coord in V.coordinates_scatter:
            a.scatter(coord[0], coord[1], marker=coord[2], color=coord[3], linewidths=float(coord[4]))
        for coord in V.coordinates_plot:
            x = np.arange(2, V.lim1, 0.5)
            y = eval(coord[1])

            for limit in range(len(y)):
                if y[limit] > V.lim1 or y[limit] < V.lim2:
                    y[limit] = None
            a.plot(x, y, linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))

    def animate_pie(i):
        a.clear()
        a.pie(V.slices, labels=V.activities, colors=V.cols, explode=V.explode, startangle=V.start_angle)

    def animate_bar(self):
        a.clear()
        a.axis("auto")
        for bar in V.bars:
            a.bar([str(bar[0])], [int(bar[1])], color=bar[2], width=float(bar[3]))

    def animate_noise(self):
        a.clear()
        a.axis("equal")
        for noise in V.noises:
            for coord in noise:
                a.scatter(coord[0], coord[1], marker=coord[2], color=coord[3], linewidths=float(coord[4]))

