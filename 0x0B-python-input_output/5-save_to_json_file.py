#!/usr/bin/python3
"""JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """using JSON representation writes an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
