#!/usr/bin/env python3

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

from functools import reduce


sum_list = lambda lst: reduce(lambda x,y: x+y, lst)
mul_list = lambda lst: reduce(lambda x,y: x*y, lst)
rev_list = lambda lst: reduce(lambda x,y: [y]+x, lst,[])
