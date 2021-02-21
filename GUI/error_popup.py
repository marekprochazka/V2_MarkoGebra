from tkinter import Toplevel

from Static.constants import NAME, INFO
from Bases import BaseLabel
from Static.get_static_path import get_static_path
from tkinter import ttk as t
from Utils.do_restart import do_restart



# TODO UPDATE GUI
def error_popup(error,info=False):
    popup = Toplevel()
    if not info:
        popup.iconbitmap(get_static_path()+"\\images\\error.ico")
    else:
        popup.iconbitmap(get_static_path()+"\\images\\info.ico")
    popup.wm_geometry("400x40+800+600")
    popup.wm_title(error[NAME])
    error_text = BaseLabel(popup,text=error[INFO])
    error_text.pack()
