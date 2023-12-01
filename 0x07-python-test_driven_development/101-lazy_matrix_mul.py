#!/usr/bin/python3
"""
This function is the lazy_matrix_mul module.

This module supplies the one function, lazy_matrix_mul().
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns a new matrix where each element
    has been divided by div.

    Args:
        m_a (list): list of lists of integers or floats.
        m_b (list): list of lists of integers or floats.
    """

    return np.dot(m_a, m_b)
