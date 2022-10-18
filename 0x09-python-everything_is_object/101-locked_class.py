#!/usr/bin/python3

class LockedClass:
    """
    prevents creation of new LockedClass instance other than 'first_name'.
    """

    __slots__ = ["first_name"]
