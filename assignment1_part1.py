#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 1 Part 1"""

def listDivide(numbers=[], divide=2):
    
    count = 0

    for num in numbers:
        if (num % divide) == 0:
            count += 1
    
    return count