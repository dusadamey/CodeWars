# https://www.codewars.com/kata/5a023c426975981341000014/

'''
Instructions:

You are given two angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
'''


def other_angle(a, b):
    return 180 - (a + b)
