from Graphing.setup import a
from Utils.ask_color import ask_color

# GRID SETTINGS FUNCTIONS THAT ARE CALLED ON FE
class Grid:
    def __init__(self, main):
        self.main = main

    def colorize_grid(self):
        a.grid(color=ask_color())

    def size_grid(self, size):
        a.grid(linewidth=size)

    def line_grid(self, line):
        a.grid(linestyle=line)
