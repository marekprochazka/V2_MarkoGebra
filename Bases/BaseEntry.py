from tkinter.ttk import Entry

# ADDITION TO NORMAL TK ENTRY, JUSTIFY CENTER IS USED ON EVERY ENTRY IN CODE
class BaseEntry(Entry):
    def __init__(self, parent, justify="center", **kwargs):
        super().__init__(parent, justify=justify, **kwargs)
