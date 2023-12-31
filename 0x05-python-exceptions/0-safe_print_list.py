#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elememts of a list

    Args:
        my_list (list): The list to print elements from.
        x (int): the number of elements of my_list
    """
    t = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            t += 1
        except IndexError:
            break
    print("")
    return (t)
