# -*- coding: utf-8 -*-
"""
from https://fiftyexamples.readthedocs.io/en/latest
"""
from functools import reduce


def celsius(f):
    return (float(f) - 32) * 5/9.


def fahrenheit(c):
    return (float(c) * 9/5.) + 32


def find_max(_list):
    return reduce((lambda x, a: x if x > a else a), _list, 0)


def find_max2(_list):
    if len(_list) == 1:
        return _list[0]
    v = find_max2(_list[1:])
    return _list[0] if _list[0] > v else v


def pop_count(value):
    value -= (value >> 1) & 0x55555555
    value = (value & 0x33333333) + ((value >> 2) & 0x33333333)
    return ((((value & 0xF0F0F0F) + (value >> 4 & 0xF0F0F0F))*0x1010101) & 0xFF000000) >> 24

