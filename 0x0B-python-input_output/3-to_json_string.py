#!/usr/bin/python3
"""String-to-JSON function."""
import json


def to_json_string(my_obj):
    """JSON representation of a string object"""
    return json.dumps(my_obj)
