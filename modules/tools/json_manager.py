import json
import os
from .search_path import search_path

def read_json(path : str) -> dict:
    with open(file = search_path(path), encoding = 'utf-8', mode= 'r') as file:
        return json.load(file)
    
def write_json(path : str, data : object) -> None:
    if not os.path.exists(os.path.dirname(search_path(path))):
        os.makedirs(os.path.dirname(search_path(path)))
        with open(file = search_path(path), encoding = 'utf-8', mode= 'w') as file:
            return json.dump({}, file, indent = 4)
        
    with open(file = search_path(path), encoding = 'utf-8', mode= 'w') as file:
        return json.dump(data, file, indent = 4)