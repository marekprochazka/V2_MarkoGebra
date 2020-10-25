
#CALCULATED VALUES
from Static.constants import CACHE, CHANGES_CACHE, ACTION, UPDATE, DATA, ID, ERRORS


def fonts():
    return {"LARGE_FONT": ("Verdana", 12), "SMALL_FONT": ("Verdana", 9), "TINY_FONT": ('Roboto', 7),
            "ITALIC_SMALL": ("Verdana", 9, "italic")}

def data_update_dict_base():
    return {CACHE: (), CHANGES_CACHE: {ACTION: UPDATE, DATA: [], ID: ""}, ERRORS: []}