#!/usr/bin/python3
"""Defines JSON file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write obj to text file with JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
