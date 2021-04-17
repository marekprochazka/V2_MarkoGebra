from Data.path import get_data_path
import json

def get_last_graphing_method():
    with open(get_data_path() + "\\data.json", "r") as f:
        data = json.load(f)
        return data["last_method"]