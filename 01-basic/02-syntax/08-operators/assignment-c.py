"""
* Assignment: Syntax Operators Division
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define variable:
        a. `result_a` with value 10 divided by 8 (truediv)
        b. `result_b` with value 10 divided by 8 (floordiv)
        c. `result_c` with a reminder of 10 divided by 8 (modulo)
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną:
        a. `result_a` z wartością 10 podzielone przez 8 (truediv)
        b. `result_b` z wartością 10 podzielone przez 8 (floordiv)
        c. `result_c` z resztą z dzielenia 10 przez 8 (modulo)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'

    >>> assert type(result_a) is float, \
    'Variable `result_a` has invalid type, should be float'
    >>> assert type(result_b) is int, \
    'Variable `result_b` has invalid type, should be int'
    >>> assert type(result_c) is int, \
    'Variable `result_c` has invalid type, should be int'

    >>> assert result_a == 1.25, \
    'Variable `result_a` has invalid value, should be 1.25'
    >>> assert result_b == 1, \
    'Variable `result_b` has invalid value, should be 1'
    >>> assert result_c == 2, \
    'Variable `result_c` has invalid value, should be 2'

    >>> pprint(result_a)
    1.25
    >>> pprint(result_b)
    1
    >>> pprint(result_c)
    2
"""

# value 10 divided by 8 (truediv)
# type: float
result_a = 10 / 8

# value 10 divided by 8 (floordiv)
# type: int
result_b = 10 // 8

# reminder of 10 divided by 8 (modulo)
# type: int
result_c = 10 % 8


