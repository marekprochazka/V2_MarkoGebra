import tkinter.colorchooser as col


def ask_color():
    color = col.askcolor()
    return color[1]
