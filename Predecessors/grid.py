from Graphing.setup import graphSubPlot
from Utils.ask_color import ask_color

# GRID SETTINGS FUNCTIONS THAT ARE CALLED ON FE
class Grid:
    def __init__(self, main):
        self.main = main

    def colorize_grid(self):
        graphSubPlot.grid(color=ask_color())

    def size_grid(self, size):
        graphSubPlot.grid(linewidth=size)

    def line_grid(self, line):
        graphSubPlot.grid(linestyle=line)
