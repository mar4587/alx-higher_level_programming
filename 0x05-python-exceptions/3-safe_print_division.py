#!/usr/bin/python3

def safe_print_dividedision(a, b):

    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        divided = None
    finally:
        print("Inside result: {}".format(div))

    return (div)
