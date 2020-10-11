from tkinter import *
import matplotlib as mp
import matplotlib.animation as anim
from matplotlib import style as st
import webbrowser
from GUI.base import Base
from Utils import DeleteAll, Saving, ShowFrame, ListView, Grid, graph_update, Limits
from Graphing.graph_animation import GraphAnimation
from Console.console import Console

mp.use("TkAgg")  # backend configuration for tkinter

# SET GRAPH STYLE FROM TXT FILE
with open("graphstyle.txt", "r") as style:
    st.use(style)

# st.use('ggplot')


# f = plt.figure(figsize=(4.5, 4.5), dpi=100)
from Graphing.setup import *


# MAIN CLASS THAT IS CALLED INTO MAINLOOP
# BASE = GUI (Frontend)
# REST ARE FUNCTIONALITIES
class MarkoGebra(Base, DeleteAll, Saving, ShowFrame, ListView, Grid, graph_update.MathUpdate, graph_update.PieUpdate,
                 graph_update.NoiseUpdate, graph_update.BarUpdate, Console, Limits):
    def __init__(self):
        self.to_inherit = (
            Base, DeleteAll, Saving, ShowFrame, ListView, Grid, graph_update.MathUpdate, graph_update.PieUpdate,
            graph_update.NoiseUpdate, graph_update.BarUpdate, Console, Limits)
        self.doInherit()

    # TO EACH PARENT CLASS A "self" FROM MAIN CLASS AS MAIN TO MAKE FUNCTIONAL CONNECTION BETWEEN CLASSES FROM HIGHER LEVEL
    def doInherit(self):
        for cls in self.to_inherit:
            cls.__init__(self, main=self)

    # SAVING DATA TO DATABASE IS MADE IN SHOW FRAME
    # THAT'S WHY EXIT METHOD IS MODIFIED
    # TODO MAKE SAVE DATA FUNCIONALITY IN MAYBE SHOW FRAME THAT CAN BE CALLED ALONE HERE
    def on_exit(self):
        self.show_Setup_Frame()
        self.destroy()

    def openHelp(self):
        webbrowser.open(url="https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270", new=1)


if __name__ == '__main__':
    # THIS OBJECT ALLOW DYNAMIC UPDATE OF GRAPH (ANIMATION)
    aniObj = GraphAnimation()
    aniFun = aniObj.Go

    app = MarkoGebra()

    # GRAPH ANIMATION RUN, CHANGED EXIT METHOD, MAINLOOP
    ani = anim.FuncAnimation(f, aniFun, interval=1000, blit=False)
    app.protocol("WM_DELETE_WINDOW", app.on_exit)
    app.mainloop()
