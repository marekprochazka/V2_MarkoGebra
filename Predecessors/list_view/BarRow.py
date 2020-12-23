from Bases import BaseEntry, BaseRow, BaseLabel
from Decorators.input_checkers import bar_input_controller
from Static.constants import CACHE, CHANGES_CACHE, DATA, ID, UPDATE
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
        self.entry_value = BaseEntry(self.parent, width=13, positive=True)
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
    @bar_input_controller
    def collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.uuid import format_existing_uuid
        id = format_existing_uuid(self.value[0])
        name = self.entry_name.get()
        value = int(self.entry_value.get()) if self.entry_value.get() else None
        color = self.col_but["bg"]
        width = float(self.entry_width.get()) if self.entry_width.get() else None
        data = make_data_update_dict(values=(name, value, color, width),action=UPDATE,id=id)

        return data
