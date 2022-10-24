#!/usr/bin/python3
"""Class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check whether an object is an instance or inherited from a class.

    Args:
        obj (any): Object to check.
        a_class (type): the class the object to be checked with
    Returns:
        True or False.
    """
    if isinstance(obj, a_class):
        return True
    return False
