import tkinter.ttk as t
from Static.constants import UPDATE, DATA, ID, ACTION, CACHE, CHANGES_CACHE, ERRORS, MATH, DELETE, TYPE
from Globals.variables import Variables as V

class BaseRow:
    def __init__(self, parent, scatter_value, controller, *args, **kwargs):
        # LINK TO ListView CLASS BECAUSE IN delete_value IS NECESSARY
        # TO CALL update_list_view
        self.controller = controller

        # CONTAINER FROM LIST
        self.parent = parent

        # VALUE FROM CACHE
        self.value = scatter_value

        # None if IT'S NOT MATH GRAPHING
        # IN MATH NECESSARY KEY IN changes_cache
        self.type = None

        # DEFINITIONS OF del_but AND save_but
        self.del_but = t.Button(self.parent, text="SMAZAT",
                                command=lambda id=self.value[0]: self.delete_value(id, type=self.type),
                                width=10)
        from Utils.update_data import update_data

        self.save_but = t.Button(self.parent, text="ULOŽIT",
                                 command=lambda: update_data(self.collect_data()),
                                 width=10)

    #   collect_data FUNCTION IS REWRITTEN IN EACH DIFFERENT ROW BUT NEEDS TO ALSO BE DEFINED HERE
    def collect_data(self):
        pass

    def delete_value(self, id, type=None):
        from Utils.uuid import format_existing_uuid
        # FINDING RIGHT VALUE IN CACHE BY IT'S id
        # DELETING THE VALUE
        for index, value in enumerate(V.cache[0]):
            if value[0] == id:
                V.cache[0].pop(index)
        # IF IT'S MATH GRAPHING IT SE NECESSARY TO ALSO CHECK SECOND CACHE
        if V.to_animate == MATH:
            for index, value in enumerate(V.cache[1]):
                if value[0] == id:
                    V.cache[1].pop(index)
                    break

        # TYPE IS NOT None ONLY IF IT'S MATH GRAPHING
        # IF IT'S MATH GRAPHING ADD TYPE TO changes_cache
        if type:
            V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(id), TYPE: type})
        else:
            V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(id)})

        # UPDATING LIST VIEW BECAUSE cache WAS CHANGED
        self.controller.update_list_view()

    def save_changes(self, collector):
        # collect_data FUNCTION OF A PARTICULAR ROW
        data = collector()

        # ERRORS ARE ADDED TO DATA IN DECORATORS IF THERE
        # WERE ANY WRONG INPUTS
        if data[ERRORS]:
            print(data[ERRORS])
        else:
            # IF NO ERRORS
            # FINDING RIGHT VALUE IN CACHE BY IT'S id
            # UPDATING THE VALUE
            for index, value in enumerate(V.cache[0]):
                if value[0] == data[CACHE][0]:
                    V.cache[0][index] = data[CACHE]
                    break
            # IF IT'S MATH GRAPHING IT SE NECESSARY TO ALSO CHECK SECOND CACHE
            if V.to_animate == MATH:
                for index, value in enumerate(V.cache[1]):
                    if value[0] == data[CACHE][0]:
                        V.cache[1][index] = data[CACHE]
                        break

            # DATA FOR changes_cache IS PREPARED IN DECORATOR
            # ONLY APPENDING HERE
            V.changes_cache.append(data[CHANGES_CACHE])

    def data_dict(self):
        return {CACHE: (), CHANGES_CACHE: {ACTION: UPDATE, DATA: [], ID: ""}, ERRORS: []}
