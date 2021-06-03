#!/usr/bin/python3
"""
This is the module documentation first import json
"""
import json


def load_from_json_file(filename):
    """load from object file"""
    with open(filename, encoding="utf-8") as file:
        json.load(file)
