from Globals.variables import Variables as V
from Graphing.setup import a
import numpy as np
from Static.constants import MATH, PIE, BAR, NOISE, MAX, MIN, X, Y
from Utils.replace_for_math import replace_for_math


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
        # SETTING LIMITS OF 'X' AND 'Y' FROM VARIABLES (BASE -30,30)
        a.set_xlim([V.limits[X][MIN], V.limits[X][MAX]])
        a.set_ylim([V.limits[Y][MIN], V.limits[Y][MAX]])
        a.set_aspect('equal')

        for coord in V.cache[0]:
            a.scatter(coord[1], coord[2], marker=coord[3], color=coord[4], linewidths=float(coord[5]))
        for coord in V.cache[1]:
            function = replace_for_math(coord[1])
            if self.__zero_x(function):
                x = np.linspace(V.limits[X][MIN], V.limits[X][MAX], 1000)
                y = eval(function)

                a.plot(x, y, linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))
            else:
                if V.limits[X][MIN] < 0:
                    x1 = np.linspace(V.limits[X][MIN], -0.000000001, 500)
                    y1 = eval(function, {"x": x1})
                    a.plot(x1, y1, linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))
                if V.limits[X][MAX] > 0:
                    x2 = np.linspace(0.000000001, V.limits[X][MAX], 500)
                    y2 = eval(function, {"x": x2})
                    a.plot(x2, y2, linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))



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
        if V.live_noise:
            a.scatter(V.live_noise[0][:,0],V.live_noise[0][:,1],color=V.live_noise[1], marker=V.live_noise[2])
        for val in V.cache[0]:
            a.scatter(val[-1][:,0],val[-1][:,1],color=val[4], marker=val[5])

    def __zero_x(self, fun):
        try:
            x = 0
            eval(fun)
            return True
        except ZeroDivisionError:
            return False
