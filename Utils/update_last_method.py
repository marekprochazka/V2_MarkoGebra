from Globals.variables import Variables as V
from Data.path import get_data_path
import json

def update_last_method():
    with open(get_data_path()+"\\data.json","r+") as f:
        data = json.load(f)
        data["last_method"] = V.currentMethod

        f.seek(0)
        json.dump(data, f)
        f.truncate()