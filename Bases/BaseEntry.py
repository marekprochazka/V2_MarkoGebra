from tkinter.ttk import Entry


class BaseEntry(Entry):
    def __init__(self, parent, justify="center", **kwargs):
        super().__init__(parent, justify=justify, **kwargs)
