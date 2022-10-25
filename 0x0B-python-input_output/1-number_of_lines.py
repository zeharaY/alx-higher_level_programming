#!/usr/bin/python3
"""Text file line-counting function."""


def number_of_lines(filename=""):
    """Returns number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
