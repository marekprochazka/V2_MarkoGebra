from Bases import BaseRow, BaseLabel, BaseEntry
import tkinter.ttk as t
from Static.constants import LINE_MARKERS, FUNCTION, CACHE, CHANGES_CACHE, ID, DATA, TYPE, UPDATE
from Decorators.input_checkers import check_function_input
from Bases import BaseColorPicker


# VALUE = [id, func,line,color,size]
# VALUE IS IN FORM AS IT IS SAVED IN CACHE AND IN DATABASE


class FunctionRow(BaseRow):
    def __init__(self, parent, func_value, controller):
        super().__init__(parent, func_value, controller)
        # IN MATH METHOD ANOTHER PARAMETER HAS TO BE DEFINED IN THE changes_cache
        # AND THAT IS TYPE
        # TYPE TELLS TO WHICH OF TWO TABLES (scatter, function) THIS VALUE BELONGS
        self.type = FUNCTION

        # GUI OF A ROW
        # TEXT LABELS
        self.text_fun = BaseLabel(self.parent, text="Funkce:")
        self.text_size = BaseLabel(self.parent, text="Vel.:")

        # ENTRY OF FUNCTION
        self.entry_fun = BaseEntry(self.parent, function=True, width=23)
        self.entry_fun.insert(0, self.value[1])

        # LINE PICKER
        self.line_multiselect = t.Combobox(self.parent, values=LINE_MARKERS, state="readonly",
                                           width=5)
        self.line_multiselect.current(LINE_MARKERS.index(self.value[2]))

        # COLOR PICKER
        # COLOR PICKER COULDN'T BE WRITTEN IN BaseRow, BECAUSE EACH
        # METHOD HAS COLOR SAVED ON DIFFERENT POSITION (DIFFERENT DATABASE FIELD)
        self.col_but = BaseColorPicker(self.parent, color=self.value[3], width=10)

        # ENTRY OF SIZE
        self.entry_size = BaseEntry(self.parent, width=8, floating=True)
        self.entry_size.insert(0, self.value[4])

        # PLACING WITH GRID
        # del_but AND save_but ARE DEFINED IN BaseRow
        self.text_fun.grid(row=0, column=0)
        self.entry_fun.grid(row=0, column=1, padx=2)
        self.line_multiselect.grid(row=0, column=2, padx=8)
        self.text_size.grid(row=0, column=3)
        self.entry_size.grid(row=0, column=4, padx=4)
        self.col_but.grid(row=0, column=5, padx=4)
        self.del_but.grid(row=0, column=6, padx=4)
        self.save_but.grid(row=0, column=7, padx=4)

    # COLLECTING DATA AND SENDING THEM THROUGH
    # THE CHECKING DECORATOR THAT CONVERTS
    # RAW DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS

    # collect_data FUNCTION IS USED IN BASE AS PARAMETER TO update_data FUNCTION
    @check_function_input
    def collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.uuid import format_existing_uuid
        id = format_existing_uuid(self.value[0])
        func = self.entry_fun.get()
        line = self.line_multiselect.get()
        color = self.col_but["bg"]
        size = self.entry_size.get()
        data = make_data_update_dict(type=FUNCTION, values=(func, line, color, size), action=UPDATE, id=id)
        return data
