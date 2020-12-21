from tkinter import Button
from Bases import BaseEntry, BaseRow, BaseLabel
from Static.constants import CACHE, CHANGES_CACHE, DATA, ID, UPDATE
from Bases import BaseColorPicker
from Utils.uuid import format_existing_uuid

# VALUE = [id,slice,activity,color,explode]
# VALUE IS IN FORM AS IT IS SAVED IN CACHE AND IN DATABASE


class PieRow(BaseRow):
    def __init__(self, parent, pie_value, controller):
        super().__init__(parent, pie_value, controller)

        # GUI OF A ROW
        # TEXT LABELS
        self.text_slice = BaseLabel(self.parent, text="Množství:")
        self.text_activity = BaseLabel(self.parent, text="Název:")
        self.text_explode = BaseLabel(self.parent, text="Výstup:")

        # ENTRIES
        self.entry_slice = BaseEntry(self.parent, width=8, floating=True)
        self.entry_slice.insert(0, self.value[1])
        self.entry_activity = BaseEntry(self.parent, width=12)
        self.entry_activity.insert(0, self.value[2])
        self.entry_explode = BaseEntry(self.parent, width=8, floating=True)
        self.entry_explode.insert(0, self.value[4])

        # COLOR PICKER
        # COLOR PICKER COULDN'T BE WRITTEN IN BaseRow, BECAUSE EACH
        # METHOD HAS COLOR SAVED ON DIFFERENT POSITION (DIFFERENT DATABASE FIELD)
        self.col_but = BaseColorPicker(self.parent, color=self.value[3], width=10)

        # PLACING WITH GRID
        # del_but AND save_but ARE DEFINED IN BaseRow
        self.text_slice.grid(row=0, column=0)
        self.entry_slice.grid(row=0, column=1, padx=2)
        self.text_activity.grid(row=0, column=2)
        self.entry_activity.grid(row=0, column=3, padx=2)
        self.text_explode.grid(row=0, column=4)
        self.entry_explode.grid(row=0, column=5, padx=2)
        self.col_but.grid(row=0, column=6, padx=3)
        self.del_but.grid(row=0, column=7, padx=3)
        self.save_but.grid(row=0, column=8, padx=3)

    # COLLECTING DATA AND SENDING THEM THROUGH
    # THE CHECKING DECORATOR THAT CONVERTS
    # RAW DATA TO DATABASE AND GRAPHING FRIENDLY FORMATS

    # collect_data FUNCTION IS USED IN BASE AS PARAMETER TO update_data FUNCTION
    def collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.uuid import format_existing_uuid
        id = format_existing_uuid(self.value[0])
        slice = float(self.entry_slice.get())
        activity = self.entry_activity.get()
        color = self.col_but["bg"]
        explode = float(self.entry_explode.get())
        data = make_data_update_dict(values=(slice, activity, color, explode), action=UPDATE, id=id)
        return data
