from tkinter.ttk import Label
from Globals.calculated import fonts

# MOST OF LABELS HAVE 'SMALL_FONT', INSTEAD OF ALWAYS WRITING THAT IT'S DEFINED HERE
class BaseLabel(Label):
    def __init__(self, parent, font=fonts()["SMALL_FONT"], **kwargs):
        super().__init__(parent, font=font, **kwargs)
