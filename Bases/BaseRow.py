import tkinter.ttk as t
from Static.constants import UPDATE, DATA, ID, ACTION, CACHE, CHANGES_CACHE, ERRORS, MATH, DELETE, TYPE
from Globals.variables import Variables as V


class BaseRow:
    def __init__(self, parent, scatter_value, controller, *args, **kwargs):
        self.controller = controller
        self.parent = parent
        self.value = scatter_value
        self.type = None

        self.del_but = t.Button(self.parent, text="SMAZAT",
                                command=lambda id=self.value[0]: self.delete_value(id, type=self.type),
                                width=10)
        self.save_but = t.Button(self.parent, text="ULOŽIT",
                                 command=lambda: self.save_changes(self.collect_data),
                                 width=10)

    def collect_data(self):
        pass

    def delete_value(self, id, type=None):
        from Utils.uuid import format_existing_uuid
        for index, value in enumerate(V.cache[0]):
            if value[0] == id:
                V.cache[0].pop(index)
        if V.to_animate == MATH:
            for index, value in enumerate(V.cache[1]):
                if value[0] == id:
                    V.cache[1].pop(index)
                    break
        if type:
            V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(id), TYPE: type})
        else:
            V.changes_cache.append({ACTION: DELETE, ID: format_existing_uuid(id)})

        self.controller.update_list_view()

    def save_changes(self, collector):
        data = collector()
        if data[ERRORS]:
            print("CHYBAAA")
        else:

            for index, value in enumerate(V.cache[0]):
                if value[0] == data[CACHE][0]:
                    V.cache[0][index] = data[CACHE]
                    break
            if V.to_animate == MATH:
                for index, value in enumerate(V.cache[1]):
                    if value[0] == data[CACHE][0]:
                        V.cache[1][index] = data[CACHE]
                        break

            V.changes_cache.append(data[CHANGES_CACHE])

    def data_dict(self):
        return {CACHE: (), CHANGES_CACHE: {ACTION: UPDATE, DATA: [], ID: ""}, ERRORS: []}
