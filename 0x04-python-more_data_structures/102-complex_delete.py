#!/usr/bin/python3

def complex_delete(my_dict, value):
    """This function deletes keys with a specific value in a dictionary"""
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value == v:
            my_dict.pop(k)
    return my_dict
