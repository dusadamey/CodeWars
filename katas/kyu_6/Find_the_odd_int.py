# https://www.codewars.com/kata/54da5a58ea159efa38000836/

'''
Instructions :

Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''


def find_it(seq):
    for i in seq:
        if seq.count(i)%2:
            return i
