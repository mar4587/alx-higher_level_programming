#!/usr/bin/python3

"""This module containing the function
load_from_json_file"""
import json


def load_from_json_file(filename):
    """This creates an Object from a “JSON file”.

    Args:
        filename (str): name of the file.

    Returns:
        object: the object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
