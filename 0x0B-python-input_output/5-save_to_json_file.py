#!/usr/bin/python3
"""
This is the module documentation first import json
"""
import json


def save_to_json_file(my_obj, filename):
    """ write a object with json"""
    with open(filename, "w", encoding='utf-8') as outfile:
        json_object = json.dumps(my_obj)
        outfile.write(json_object)
