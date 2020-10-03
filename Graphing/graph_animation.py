from Globals.variables import Variables as V
from Graphing.setup import a
import numpy as np
from Static.constants import MATH,PIE,BAR,NOISE
from sympy import solveset,Eq,Symbol


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
    
    def animate_graphs(self):


        a.clear()
        a.axis("equal")

        for coord in V.cache[0]:
            a.scatter(coord[1], coord[2], marker=coord[3], color=coord[4], linewidths=float(coord[5]))
        for coord in V.cache[1]:


            x,y = self.cut_y_limits(coord[1])


            # for limit in range(len(y)):
            #     if y[limit] > V.lim1 or y[limit] < V.lim2:
            #         y[limit] = None
            a.plot(x,y , linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))



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

    def cut_y_limits(self, func):
        x = np.linspace(V.lim2,V.lim1,100)
        y = eval(func)
        to_del = []
        for index, value in enumerate(y):
            if value > V.lim1 or value < V.lim2:
                to_del.append(index)
        x = np.delete(x, to_del)
        y = np.delete(y, to_del)

        left_x_lim,right_x_lim = self.add_limit_points(func)
        x = np.insert(x,0,left_x_lim)
        x = np.append(x,right_x_lim)

        y = np.insert(y,0,V.lim2)
        y = np.append(y,V.lim1)


        return x, y

    def add_limit_points(self,func):
        x = Symbol("x")

        lower_lim = complex(list(solveset(Eq(V.lim2,eval(func)),x))[0]).real
        upper_lim = complex(list(solveset(Eq(V.lim1,eval(func)),x))[0]).real
        return lower_lim,upper_lim

