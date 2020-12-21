import tkinter.ttk as t
from Bases import BaseEntry, BaseRow, BaseLabel
from Static.constants import SCATTER, POINT_MARKERS, UPDATE
from Decorators.input_checkers import check_scatter_input
from Bases import BaseColorPicker


# VALUE = [id,x,y,marker,color,size]
# VALUE IS IN FORM AS IT IS SAVED IN CACHE AND IN DATABASE

class ScatterRow(BaseRow):
    def __init__(self, parent, scatter_value, controller):
        super().__init__(parent, scatter_value, controller)
        # IN MATH METHOD ANOTHER PARAMETER HAS TO BE DEFINED IN THE changes_cache
        # AND THAT IS TYPE
        # TYPE TELLS TO WHICH OF TWO TABLES (scatter, function) THIS VALUE BELONGS
        self.type = SCATTER

        # GUI OF A ROW
        # TEXT LABELS
        self.text_x = BaseLabel(self.parent, text="X:")
        self.text_y = BaseLabel(self.parent, text="Y:")
        self.text_size = BaseLabel(self.parent, text="Vel.:")

        # ENTRIES OF COORDINATES
        self.entry_x, self.entry_y = BaseEntry(self.parent, width=13, numbers=True), BaseEntry(self.parent, width=13, numbers=True)
        self.entry_x.insert(0, self.value[1])
        self.entry_y.insert(0, self.value[2])

        # MARKER PICKER
        self.marker_multiselect = t.Combobox(self.parent, values=POINT_MARKERS, state="readonly",
                                             width=5)
        self.marker_multiselect.current(POINT_MARKERS.index(self.value[3]))

        # COLOR PICKER
        # COLOR PICKER COULDN'T BE WRITTEN IN BaseRow, BECAUSE EACH
        # METHOD HAS COLOR SAVED ON DIFFERENT POSITION (DIFFERENT DATABASE FIELD)
        self.col_but = BaseColorPicker(self.parent, color=self.value[4], width=10)

        # ENTRY OF SIZE
        self.entry_size = BaseEntry(self.parent, width=8)
        self.entry_size.insert(0, self.value[5])

        # PLACING WITH GRID
        # del_but AND save_but ARE DEFINED IN BaseRow
        self.text_x.grid(row=0, column=0)
        self.entry_x.grid(row=0, column=1)
        self.text_y.grid(row=0, column=2)
        self.entry_y.grid(row=0, column=3)
        self.marker_multiselect.grid(row=0, column=4, padx=8)
        self.text_size.grid(row=0, column=5)
        self.entry_size.grid(row=0, column=6, padx=4)
        self.col_but.grid(row=0, column=7, padx=4)
        self.del_but.grid(row=0, column=8, padx=4)
        self.save_but.grid(row=0, column=9, padx=4)

    # COLLECTING DATA AND SENDING THEM THROUGH
    # THE CHECKING DECORATOR THAT CONVERTS
    # RAW DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS

    # collect_data FUNCTION IS USED IN BASE AS PARAMETER TO update_data FUNCTION
    @check_scatter_input
    def collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.uuid import format_existing_uuid
        id = format_existing_uuid(self.value[0])
        x = self.entry_x.get()
        y = self.entry_y.get()
        marker = self.marker_multiselect.get()
        color = self.col_but["bg"]
        size = self.entry_size.get()
        data = make_data_update_dict(id=id, values=(x, y, marker, color, size), action=UPDATE, type=SCATTER)
        return data
