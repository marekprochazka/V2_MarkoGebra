from tkinter import *
import tkinter.ttk as t
from tkinter.ttk import Button
import tkinter.colorchooser as col
from colormap import rgb2hex
from math import floor
from tkinter import filedialog
from PIL import Image
import json
from numpy import sin, cos, tan, pi
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as anim
from matplotlib import style as st
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import webbrowser
# Ver. Alpha 1.6
#


from Static.constants import *
from Globals.calculated import *
from Globals.variables import Variables as V
from GUI.base import Base
from Utils import DeleteAll, Saving, ShowFrame, UpdateTable, Grid, graph_update
from Graphing.graph_animation import GraphAnimation
from Console.console import Console
mp.use("TkAgg")
with open("graphstyle.txt", "r") as style:
    st.use(style)

# st.use('ggplot')

import numpy as np

# f = plt.figure(figsize=(4.5, 4.5), dpi=100)
from Graphing.setup import *



class MarkoGebra(Base,DeleteAll,Saving,ShowFrame,UpdateTable,Grid,graph_update.MathUpdate,graph_update.PieUpdate,graph_update.NoiseUpdate,graph_update.BarUpdate,Console):
    def __init__(self):

        self.to_inherit = (DeleteAll,Saving,ShowFrame,UpdateTable,Grid,graph_update.MathUpdate,graph_update.PieUpdate,graph_update.NoiseUpdate,graph_update.BarUpdate,Console)
        self.doInherit()
        Base.__init__(self)


    def doInherit(self):
        for cls in self.to_inherit:
            cls.__init__(self,main=self)

    def on_exit(self):
        self.show_Setup_Frame()
        self.destroy()

    def openHelp(self):
        webbrowser.open(url="https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270", new=1)
        webbrowser.open(url="D:\Věci\Programování\Dlohodoba_prace_main_2020\web\index.html", new=1)



aniObj = GraphAnimation()
aniFun = aniObj.Go

app = MarkoGebra()

ani = anim.FuncAnimation(f, aniFun, interval=1000, blit=False)
app.protocol("WM_DELETE_WINDOW", app.on_exit)
app.mainloop()
