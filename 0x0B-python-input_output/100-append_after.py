#!/usr/bin/python3
"""Txt file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line 

    Args:
        filename (str): File name
        search_string (str): The string to search
        new_string (str): The string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
