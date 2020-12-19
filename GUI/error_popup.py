from tkinter import Toplevel

from Static.constants import NAME, INFO
from Bases import BaseLabel

# TODO UPDATE GUI
def error_popup(error):
    popup = Toplevel()
    popup.wm_geometry("400x40+800+600")
    popup.wm_title(error[NAME])
    error_text = BaseLabel(popup,text=error[INFO])
    error_text.pack()