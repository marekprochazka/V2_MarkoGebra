from tkinter import Button

from Utils.ask_color import ask_color


# BUTTON THAT IS CHANGING IT'S BG COLOR AFTER CLICKING USED AS COLOR PICKER
class BaseColorPicker(Button):
    def __init__(self, parent, color="blue", special_command=None, *args, **kwargs):
        if not special_command:
            super().__init__(parent, bg=color, command=lambda: self.config(bg=ask_color()), *args, **kwargs)
        else:
            super().__init__(parent, bg=color, command=lambda: special_command(), *args, **kwargs)
