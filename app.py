from tkinter import *
import matplotlib as mp
import matplotlib.animation as anim
from matplotlib import style as st
import webbrowser
from GUI.base import Base
from Predecessors import DeleteAll, SavingAsPNG, ShowFrame, ListView, Grid, Limits
from Graphing.graph_animation import GraphAnimation
from GUI.restart_popup import Restart_popup
from Utils.update_last_method import update_last_method


mp.use("TkAgg")  # backend configuration for tkinter

from Graphing.setup import *


# MAIN CLASS THAT IS CALLED INTO MAINLOOP
# BASE = GUI (Frontend)
# REST ARE FUNCTIONALITIES
class MarkoGebra(Base, DeleteAll, SavingAsPNG, ShowFrame, ListView, Grid, Limits, Restart_popup):
    def __init__(self):
        super().__init__(main=self)

    # SAVING DATA TO DATABASE IS MADE IN SHOW FRAME
    # THAT'S WHY EXIT METHOD IS MODIFIED
    # TODO MAKE SAVE DATA FUNCIONALITY IN MAYBE SHOW FRAME THAT CAN BE CALLED ALONE HERE
    def on_exit(self):
        self.show_methodFrame(exit=True)
        update_last_method()
        self.destroy()

    def on_restart(self):
        from Utils.do_restart import do_restart
        self.show_methodFrame(exit=True)
        update_last_method()
        do_restart()

    def openHelp(self):
        webbrowser.open(url="http://marekprochazka.pythonanywhere.com/", new=1)





if __name__ == '__main__':
    # THIS OBJECT ALLOW DYNAMIC UPDATE OF GRAPH (ANIMATION)
    aniObj = GraphAnimation()
    aniFun = aniObj.Go

    app = MarkoGebra()

    # GRAPH ANIMATION RUN, CHANGED EXIT METHOD, MAINLOOP
    ani = anim.FuncAnimation(graphFigure, aniFun, interval=1000, blit=False)
    app.protocol("WM_DELETE_WINDOW", app.on_exit)
    app.mainloop()
