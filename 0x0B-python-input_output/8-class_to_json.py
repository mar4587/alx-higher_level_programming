#!/usr/bin/python3

"""This module containing the function
class_to_json"""


def class_to_json(obj):
    """This returns the dictionary description with simple data structure,
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (MyClass): object.

    Returns:
        dict: The dictionary
    """
    # print("type of obj --> {}".format(type(obj)))
    return obj.__dict__
