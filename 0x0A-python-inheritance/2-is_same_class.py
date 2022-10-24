#!/usr/bin/python3
"""Class-checking function."""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a given class.

    Args:
        obj (any): object to check
        a_class (type): the class to be checked with the object
    Returns:
         True or False.
    """
    if type(obj) == a_class:
        return True
    return False
