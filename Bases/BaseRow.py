import tkinter.ttk as t
from Static.constants import UPDATE, DATA, ID, ACTION, CACHE, CHANGES_CACHE, ERRORS, MATH, DELETE, TYPE
from Globals.variables import Variables as V


# LIST VIEW OF ELEMENTS HAVE SOME SIMILAR LOGIC AND DEFINITIONS NO MATTER THE GRAPHING STYLE
# DEFINED HERE

class BaseRow:
    def __init__(self, parent, value, controller, *args, **kwargs):
        # LINK TO ListView CLASS BECAUSE IN delete_value IS NECESSARY
        # TO CALL update_list_view
        self.controller = controller

        # CONTAINER FROM LIST
        self.parent = parent

        # VALUE FROM CACHE
        self.value = value

        # None if IT'S NOT MATH GRAPHING
        # IN MATH NECESSARY KEY IN changes_cache
        self.type = None

        # MAKING OF Tcl WRAPPER AROUND CALLBACK FUNCTION
        # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html

        # DEFINITIONS OF del_but AND save_but
        self.button_delete = t.Button(self.parent, text="SMAZAT",
                                      command=lambda id=self.value[0]: self.delete_value(id, type=self.type),
                                      width=10)
        from Utils.update_data import update_data

        self.button_save = t.Button(self.parent, text="ULOŽIT",
                                    command=lambda: update_data(self.collect_data(),
                                                                limits_fun=self.controller.auto_update_limits_by_scatter_input),
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
        if V.currentMethod == MATH:
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
        pass

    # MAKING BASE DICT IN FORMAT FOR 'update_data'
    def data_dict(self):
        return {CACHE: (), CHANGES_CACHE: {ACTION: UPDATE, DATA: [], ID: ""}, ERRORS: []}

    # ENTRY INPUT CONTROL
    def __is_digit_callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
