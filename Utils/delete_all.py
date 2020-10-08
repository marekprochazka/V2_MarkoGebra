from Globals.variables import Variables as V
from Static.constants import ID, DELETE, ACTION, MATH, TYPE, SCATTER, FUNCTION
from Utils.uuid import format_existing_uuid


class DeleteAll:
    def __init__(self, main):
        self.main = main

    # FUNCTION THAT MANAGES DELETING ALL ACTUAL DATA IN GRAPH
    # FUNCTION IS CALLED BY BUTTON ON FE
    def delete_all(self):
        # MAKING CACHED CHANGE FOR EACH VALUE IN GRAPH
        if V.to_animate == MATH:
            for scatter in V.cache[0]:
                V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(scatter[0]), TYPE: SCATTER})
            for func in V.cache[1]:
                V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(func[0]), TYPE: FUNCTION})
        else:
            for value in V.cache[0]:
                V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(value[0])})
        # EMPTYING GRAPH CACHE (MATH GRAPHING NEEDS SPECIAL FORMAT
        # THAT IS NORMALLY MADE AUTOMATICALLY BY DATA LOADING BUT HERE IT'S REQUIRED TO BE HARD CODED)
        V.cache = [[], []] if V.to_animate == MATH else []
        self.main.update_table()
