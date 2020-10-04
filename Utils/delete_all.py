from Globals.variables import Variables as V
from Static.constants import ID, DELETE, ACTION, MATH, TYPE, SCATTER, FUNCTION
from Utils.uuid import format_existing_uuid

class DeleteAll:
    def __init__(self, main):
        self.main = main

    def delete_all(self):
        if V.to_animate == MATH:
            for scatter in V.cache[0]:
                V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(scatter[0]), TYPE: SCATTER})
            for func in V.cache[1]:
                V.changes_cache.append({ACTION: DELETE, ID:format_existing_uuid(func[0]), TYPE: FUNCTION})
        else:
            for value in V.cache[0]:
                V.changes_cache.append({ACTION: DELETE, ID:format_existing_uuid(value[0])})
        V.cache = [[], []] if V.to_animate == MATH else []
        self.main.update_table()
