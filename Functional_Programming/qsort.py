#!/usr/bin/env python3

def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

numbers = (1,6,3,32,85,23,9,123,23,336)

print(qsort1(numbers))
