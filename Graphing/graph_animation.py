from Globals.variables import Variables as V
from Graphing.setup import a
import numpy as np
from Static.constants import MATH, PIE, BAR, NOISE, MAX, MIN, X, Y


# GRAPHING METHODS ARE MANAGED IN THIS CLASS
class GraphAnimation:
    def Go(self, i):
        # FUNCTION WILL KNOW WHAT GRAPHING METHOD CALL BY VARAIBLE "to_animate" THAT IS MANAGED IN "new_show_frame.py"
        if V.to_animate == MATH:
            self.animate_graphs()
        elif V.to_animate == PIE:
            self.animate_pie()
        elif V.to_animate == BAR:
            self.animate_bar()
        elif V.to_animate == NOISE:
            self.animate_noise()

    # EACH FUNCTION WILL TAKE DATA FROM CACHE AND PUT IT INTO GRAPHING IN RIGHT FORMAT

    # MATH
    def animate_graphs(self):


        a.clear()
        #SETTING LIMITS OF 'X' AND 'Y' FROM VARIABLES (BASE -30,30)
        a.set_xlim([V.limits[X][MIN], V.limits[X][MAX]])
        a.set_ylim([V.limits[Y][MIN], V.limits[Y][MAX]])
        a.set_aspect('equal')

        for coord in V.cache[0]:
            a.scatter(coord[1], coord[2], marker=coord[3], color=coord[4], linewidths=float(coord[5]))
        for coord in V.cache[1]:
            x = np.linspace(V.limits[X][MIN], V.limits[X][MAX], 100)
            y = eval(coord[1])

            a.plot(x, y, linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))

    # PIE
    def animate_pie(i):
        a.clear()
        slices, activities, cols, explode = [], [], [], []
        for val in V.cache[0]:
            slices.append(val[1])
            activities.append(val[2])
            cols.append(val[3])
            explode.append(val[4])
        a.pie(slices, labels=activities, colors=cols, explode=explode, startangle=V.start_angle, normalize=True)

    # BAR
    def animate_bar(self):
        a.clear()
        a.axis("auto")
        for bar in V.cache[0]:
            a.bar(str(bar[1]), int(bar[2]), color=bar[3], width=float(bar[4]))

    # NOISE
    # TODO
    def animate_noise(self):
        a.clear()
        a.axis("equal")
        for noise in V.noises:
            for coord in noise:
                a.scatter(coord[0], coord[1], marker=coord[2], color=coord[3], linewidths=float(coord[4]))
