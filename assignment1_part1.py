#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 1 Part 1"""


def listDivide(numbers=[], divide=2):
    """This function that divdes list values by divide var

    Args:
        numbers (list): list of int
        divide (int): num divided by. Default to 2
    """
    count = 0

    for num in numbers:
        if (num % divide) == 0:
            count += 1
    return count


class ListDivideException(Exception):
    """ Error Object that invalidates list divide"""
    pass


def testListDivide():
    """This function that tests the listDivide function.
        Raise exception if error found.

    Args:
        none

    Returns:
        ""No error if any

    Examples:

        >>> testListDivide()
    """    
    if listDivide([1,2,3,4,5]) != 2:
        raise ListDivideException

    if listDivide([2,4,6,8,10]) != 5:
        raise ListDivideException

    if listDivide([30, 54, 63,98, 100], divide=10) != 2:
        raise ListDivideException

    if listDivide([]) != 0:
        raise ListDivideException

    if listDivide([1,2,3,4,5], 1) != 5:
        raise ListDivideException