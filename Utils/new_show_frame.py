from Globals.variables import Variables as V
from Static.constants import GRAPHING_METHOD, MAX_WIDTH, MAX_HEIGHT, MATH, BAR, PIE
from Data.functions import UPDATE_FUNCTIONS

from Static.constants import ACTION,CREATE,UPDATE,DELETE,ID,DATA,TYPE,SCATTER,FUNCTION
from Utils.uuid import generate_uuid,format_existing_uuid

class ShowFrame:
    def __init__(self, main):
        self.main = main


    def show_Setup_Frame(self, cont=None):
        # SAVING PREVIOUS
        if V.to_animate != None: UPDATE_FUNCTIONS[V.to_animate](V.changes_cache)

tst = ShowFrame("aaaa")
V.to_animate = MATH
V.changes_cache.append({ACTION:CREATE,DATA:(1,2,":-)","red",7),ID:generate_uuid(),TYPE:SCATTER})
V.changes_cache.append({ACTION:CREATE,DATA:("x**2","solid","red",2),ID:generate_uuid(),TYPE:FUNCTION})
print((V.changes_cache))
tst.show_Setup_Frame()
