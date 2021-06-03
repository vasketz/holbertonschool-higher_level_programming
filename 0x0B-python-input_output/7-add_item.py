#!/usr/bin/python3
""" 
This is the module documentation first import 
"""


import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


arg = sys.argv[1:]
filename = "add_item.json"


try:
    objec = load_from_json_file(filename)
    save_to_json_file(objec + arg, filename)
except:
    save_to_jason_file([] + arg, filename)
