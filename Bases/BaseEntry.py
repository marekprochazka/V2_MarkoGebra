from tkinter.ttk import Entry

class BaseEntry(Entry):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,justify="center",**kwargs)



