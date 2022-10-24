#!/usr/bin/python3
"""Inherited class-checking function."""

def inherits_from(obj, a_class):
    """Checks whether an object is an inherited from the class.

    Args:
        obj (any): Object to check.
        a_class (type): the class the object to be checked with
    Returns:
        True or False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
