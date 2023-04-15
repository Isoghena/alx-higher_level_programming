#!/usr/bin/python3
"""Defines the class Student."""


class Student:
    """Representation of students."""
    def __init__(self, first_name, last_name, age):
        """Initialize the student."""
        self.first_name = first_name
        self.last_name = last_name
        seld.age = age

    def to_json(self):
        """Returns dictionary representation instance of student."""
        return self.__dict__
