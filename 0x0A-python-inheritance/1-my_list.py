#!/usr/bin/python3
"""Inherited list class MyList."""

class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        """Print a sorted list in ascending order"""
        print(sorted(self))
