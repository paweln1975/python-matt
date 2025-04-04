import math
import os
import random
import re
import sys

def print_weird(n: int):
    """
    Given an integer, performs the following conditional actions:

    If  is odd, print Weird
    If  is even and in the inclusive range of  to , print Not Weird
    If  is even and in the inclusive range of  to , print Weird
    If  is even and greater than , print Not Weird
    :param n:
    :return:

    >>> print_weird(3)
    Weird
    >>> print_weird(24)
    Not Weird
    >>> print_weird(18)
    Weird
    >>> print_weird(22)
    Not Weird
    >>> print_weird(2)
    Not Weird
    """
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")