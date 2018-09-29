# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

Mike Buglione
I pledge my honor that I abide by the stevens honor systems
"""


def classify_triangle(a_side, b_side, c_side):
    '''
    triangle tester
    '''
    a_side, b_side, c_side = sorted(
        [a_side, b_side, c_side])  # sorts the values in the triangle
    # require that the input values be >= 0 and <= 200

    a_side_valid = a_side > 200 or a_side <= 0
    b_side_valid = b_side > 200 or b_side <= 0
    c_side_valid = c_side > 200 or c_side <= 0
    abc_inst = not(isinstance(a_side, int) and isinstance(
        b_side, int) and isinstance(c_side, int))
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type

    if a_side_valid or b_side_valid or c_side_valid or abc_inst:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    a_side_test = (a_side >= (b_side + c_side))
    b_side_test = (b_side >= (a_side + c_side))
    c_side_test = (c_side >= (a_side + b_side))

    if a_side_test or b_side_test or c_side_test:
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a_side == b_side and b_side == c_side:
        return 'Equilateral'
    if ((a_side * a_side) + (b_side * b_side)) == (c_side * c_side):
        return 'Right'
    if (a_side != b_side) and (b_side != c_side) and (c_side != a_side):
        return 'Scalene'

    return 'Isoceles'
