#!/usr/bin/python3
"""This is the module documentation."""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


arg = sys.argv[1:]
filename = "add_item.json"

objec = load_from_json_file(filename)
for i in arg:
    objec.append(i)
save_to_json_file(objec, filename)

try:
    load_from_json_dile(filename)
except:
    save_to_jason_file(arg, filename)
