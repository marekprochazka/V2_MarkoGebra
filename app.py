from tkinter import *
import matplotlib as mp
import matplotlib.animation as anim
from matplotlib import style as st
import webbrowser




from GUI.base import Base
from Utils import DeleteAll, Saving, ShowFrame, UpdateTable, Grid, graph_update
from Graphing.graph_animation import GraphAnimation
from Console.console import Console

mp.use("TkAgg")
with open("graphstyle.txt", "r") as style:
    st.use(style)

# st.use('ggplot')



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


if __name__ == '__main__':

    aniObj = GraphAnimation()
    aniFun = aniObj.Go

    app = MarkoGebra()

    ani = anim.FuncAnimation(f, aniFun, interval=1000, blit=False)
    app.protocol("WM_DELETE_WINDOW", app.on_exit)
    app.mainloop()
