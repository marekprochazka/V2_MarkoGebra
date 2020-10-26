from tkinter import Button

from Utils.ask_color import ask_color


class BaseColorPicker(Button):
    def __init__(self, parent, color="blue", *args, **kwargs):
        super().__init__(parent, bg=color, command=lambda: self.config(bg=ask_color()), *args, **kwargs)
