#!/usr/bin/python3
"""Defines JSON file reading function"""
import json


def load_from_json_file(filename):
    """Creates an obj fron JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
