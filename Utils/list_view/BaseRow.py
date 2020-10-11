import tkinter.ttk as t

class BaseRow:
    def __init__(self, parent, scatter_value):
        self.parent = parent
        self.value = scatter_value

        self.del_but = t.Button(self.parent, text="DELETE",
                                command=lambda id=self.value[0]: self.delete_value(id),
                                width=10)
        self.save_but = t.Button(self.parent, text="SAVE",
                                 command=lambda id=self.value[0]: self.save_changes(id),
                                 width=10)

    def change_color(self, id):
        print(id)

    def delete_value(self, id):
        print(id)

    def save_changes(self, id):
        print(id)
