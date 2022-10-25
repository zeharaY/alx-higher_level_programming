#!/usr/bin/python3
"""Class Student."""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializing new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): ge of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the Student.
	Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
