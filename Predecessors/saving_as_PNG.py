from tkinter import Toplevel, filedialog
from PIL import Image
from Graphing.setup import graphSubPlot, graphFigure
from tkinter import ttk as t
import numpy as np


# TODO MAYBE SHOULD BE MOVED TO GUI, OR AT LEAST PART OF IT
# TODO CREATE SAVER COMPONENT THAT WILL BE IMPLEMENTED TO FUNCTION SAVER AS NEW INSTANCE
# PNG SAVER POPUP GUI AND BACKEND FUNCTIONALITY
class SavingAsPNG:
    def __init__(self, main):
        self.main = main

    # EDITED EXIT FUNCTION
    def __callback(self, top):
        self.exit_top(top)

    # ACTUAL EXIT FUNCTION
    def exit_top(self, top):
        graphSubPlot.axes.get_xaxis().set_visible(True)
        graphSubPlot.axes.get_yaxis().set_visible(True)
        top.destroy()

    # POPUP GUI
    def saver(self):
        top = Toplevel()
        top.wm_geometry("400x400")
        top.wm_title("Uložit graf")
        top.minsize(400, 400)
        top.maxsize(400, 400)

        top.protocol("WM_DELETE_WINDOW", lambda: self.__callback(top))

        name_label = t.Label(top, text="Název souboru:")
        name_label.grid(row=0, column=0, padx=8)
        name = t.Entry(top)
        name.grid(row=0, column=1, sticky="we")
        name_png = t.Label(top, text=".png")
        name_png.grid(row=0, column=2, sticky="w")
        direct_button = t.Button(top, text="Umístění", command=lambda: self.find_dir(direct, top))
        direct_button.grid(row=1, column=0, columnspan=2, sticky="we")
        direct = t.Label(top, text="")
        direct.grid(row=1, column=2)
        is_grid_label = t.Label(top, text="Neukládat s popisem os: ")
        is_grid_label.grid(row=2, column=0)
        is_grid = t.Checkbutton(top, command=lambda: self.is_grid_func(is_grid.state()))
        is_grid.grid(row=2, column=1)
        send = t.Button(top, text="Uložit", command=lambda: self.save_as_img(direct["text"], name.get(), top))
        send.grid(row=3, column=0, columnspan=2, sticky="we")
        go_back = t.Button(top, text="Zrušit", command=lambda: self.exit_top(top))
        go_back.grid(row=3, column=2)

    # DIRECTORY DIALOG
    def find_dir(self, dir_label, top):
        file = filedialog.askdirectory()
        if file:
            dir_label["text"] = file
        top.lift()

    # ON/OFF GRID SWITCH
    def is_grid_func(self, state):
        if "selected" in state:
            graphSubPlot.axes.get_xaxis().set_visible(False)
            graphSubPlot.axes.get_yaxis().set_visible(False)
        else:
            graphSubPlot.axes.get_xaxis().set_visible(True)
            graphSubPlot.axes.get_yaxis().set_visible(True)

    # ACTUAL SAVING
    def save_as_img(self, file, name, top):
        w, h = graphFigure.canvas.get_width_height()
        buf = np.frombuffer(graphFigure.canvas.tostring_argb(), dtype=np.uint8)
        buf.shape = (w, h, 4)
        buf = np.roll(buf, 3, axis=2)
        w, h, d = buf.shape
        im = Image.frombytes("RGBA", (w, h), buf.tostring())
        im.save(f"{file}/{name}.png")
        top.destroy()
        graphSubPlot.axes.get_xaxis().set_visible(True)
        graphSubPlot.axes.get_yaxis().set_visible(True)
