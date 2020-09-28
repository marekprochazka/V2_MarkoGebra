from Globals.variables import Variables as V
from Static.constants import GRAPHING_METHOD, MAX_WIDTH, MAX_HEIGHT, MATH, BAR, PIE, TO_ANIMATExTABLES
from Data.functions import UPDATE_FUNCTIONS, get_tables

from Static.constants import ACTION,CREATE,UPDATE,DELETE,ID,DATA,TYPE,SCATTER,FUNCTION
from Utils.uuid import generate_uuid,format_existing_uuid

class ShowFrame:
    def __init__(self, main):
        self.main = main


    def show_Setup_Frame(self, cont=None):
        # SAVING PREVIOUS
        if V.to_animate != None: UPDATE_FUNCTIONS[V.to_animate](V.changes_cache)

        #CHANGE to_animate TO ACTUAL FRAME
        if cont != None:
            new_frame = cont(self.main.SetupContainer, self.main)
            V.to_animate = GRAPHING_METHOD[new_frame.type]

            #TODO uncomment after GUI connection

            # if self.main._frame is not None:
            #     for child in self.main._frame.winfo_children():
            #         child.destroy()
            #     self.main._frame.destroy()
            # self.main._frame = new_frame
            # self.main._frame.place(x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15, height=MAX_HEIGHT * 45, width=MAX_WIDTH * .40)

        #LODAING DATA TO CACHE
        V.cache = list(get_tables(TO_ANIMATExTABLES[V.to_animate]))


# TESTING
# tst = ShowFrame("aaaa")
# V.to_animate = MATH
# V.changes_cache.append({ACTION:CREATE,DATA:(1,2,":-)","red",7),ID:generate_uuid(),TYPE:SCATTER})
# V.changes_cache.append({ACTION:CREATE,DATA:("x**2","solid","red",2),ID:generate_uuid(),TYPE:FUNCTION})
# print((V.changes_cache))
# tst.show_Setup_Frame()
import numpy
# V.to_animate = MATH
# print(V.cache)
# V.cache = list(get_tables(TO_ANIMATExTABLES[V.to_animate]))
# print(V.cache)