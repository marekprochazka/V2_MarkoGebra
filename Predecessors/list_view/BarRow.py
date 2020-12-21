from Bases import BaseEntry, BaseRow, BaseLabel
from Decorators.input_checkers import check_bar_input
from Static.constants import CACHE, CHANGES_CACHE, DATA, ID
from Bases import BaseColorPicker


# VALUE = [id,name,value,color,width]
# VALUE IS IN FORM AS IT IS SAVED IN CACHE AND IN DATABASE

class BarRow(BaseRow):
    def __init__(self, parent, bar_value, controller):
        super().__init__(parent, bar_value, controller)
        # GUI OF A ROW
        # TEXT LABELS
        self.text_name = BaseLabel(self.parent, text="Název:")
        self.text_value = BaseLabel(self.parent, text="Množstvý:")
        self.text_width = BaseLabel(self.parent, text="Šířka:")

        # ENTRIES
        self.entry_name = BaseEntry(self.parent, width=8)
        self.entry_name.insert(0, self.value[1])
        self.entry_value = BaseEntry(self.parent, width=13, numbers=True)
        self.entry_value.insert(0, self.value[2])
        self.entry_width = BaseEntry(self.parent, width=8,floating=True)
        self.entry_width.insert(0, self.value[4])

        # COLOR PICKER
        # COLOR PICKER COULDN'T BE WRITTEN IN BaseRow, BECAUSE EACH
        # METHOD HAS COLOR SAVED ON DIFFERENT POSITION (DIFFERENT DATABASE FIELD)
        self.col_but = BaseColorPicker(self.parent, color=self.value[3], width=10)

        # PLACING WITH GRID
        # del_but AND save_but ARE DEFINED IN BaseRow
        self.text_value.grid(row=0, column=0)
        self.entry_value.grid(row=0, column=1, padx=2)
        self.text_name.grid(row=0, column=2)
        self.entry_name.grid(row=0, column=3, padx=2)
        self.text_width.grid(row=0, column=4)
        self.entry_width.grid(row=0, column=5, padx=2)
        self.col_but.grid(row=0, column=6, padx=3)
        self.del_but.grid(row=0, column=7, padx=3)
        self.save_but.grid(row=0, column=8, padx=3)

    # COLLECTING DATA AND SENDING THEM THROUGH
    # THE CHECKING DECORATOR THAT CONVERTS
    # RAW DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS

    # collect_data FUNCTION IS USED IN BASE AS PARAMETER TO update_data FUNCTION
    @check_bar_input
    def collect_data(self):
        data = self.data_dict()
        id = self.value[0]
        name = self.entry_name.get()
        value = self.entry_value.get()
        color = self.col_but["bg"]
        width = self.entry_width.get()
        data[CACHE] = (id, name, value, color, width)
        data[CHANGES_CACHE][DATA] = (name, value, color, width)
        data[CHANGES_CACHE][ID] = id
        return data
