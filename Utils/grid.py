from Graphing.setup import a
import tkinter.colorchooser as col


# GRID SETTINGS FUNCTIONS THAT ARE CALLED ON FE
class Grid:
    def __init__(self, main):
        self.main = main

    def colorize_grid(self):
        color = col.askcolor()
        a.grid(color=color[1])

    def size_grid(self, size):
        a.grid(linewidth=size)

    def line_grid(self, line):
        a.grid(linestyle=line)
