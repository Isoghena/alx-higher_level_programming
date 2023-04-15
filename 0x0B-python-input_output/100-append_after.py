#!/usr/bin/python3
"""Defines append_after function"""


def appennd_after(filename="", search_string"", new_string=""):
    """appends a new string in file"""
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writlines(line_list)
