"""
The absolute difference between two integers, a and b, is written as |a-b|. The maximum absolute difference between
two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in
__elements.

The Difference class is started for you in the editor. It has a private integer array(elements) for storing
non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.

Task
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements
and stores it in the  instance variable.
"""

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        if len(self.__elements) < 2:
            self.maximumDifference = 0
        else:
            min_element = min(self.__elements)
            max_element = max(self.__elements)
            self.maximumDifference = abs(max_element - min_element)
