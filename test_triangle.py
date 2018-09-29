# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """
        # define multiple sets of tests as functions with names that begin
    """
    def test_right_triangle_a(self):
        """
            # define multiple sets of tests as functions with names that begin
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """
            # define multiple sets of tests as functions with names that begin
        """
        self.assertEqual(classify_triangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """
            # define multiple sets of tests as functions with names that begin
        """
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def test_triangle(self):
        """
            # define multiple sets of tests as functions with names that begin
        """
        self.assertNotEqual(classify_triangle(
            1, 1, 1), 'InvalidInput', "111 should not receive a InvalidInput")

    def testvalid_triangle(self):
        """
            # define multiple sets of tests as functions with names that begin
        """
        self.assertEqual(classify_triangle(50, 3, 4),
                         'NotATriangle', 'This is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
