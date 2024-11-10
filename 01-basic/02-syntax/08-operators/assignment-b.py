"""
* Assignment: Syntax Operators Mul/Pow
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define variable:
        a. `result_a` with value 2 times 3
        b. `result_b` with value 2 to the power of 3
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną:
        a. `result_a` z wartością 2 razy 3
        b. `result_b` z wartością 2 do potęgi 3
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'

    >>> assert type(result_a) is int, \
    'Variable `result_a` has invalid type, should be int'
    >>> assert type(result_b) is int, \
    'Variable `result_b` has invalid type, should be int'

    >>> assert result_a == 6, \
    'Variable `result_a` has invalid value, should be 6'
    >>> assert result_b == 8, \
    'Variable `result_b` has invalid value, should be 8'

    >>> pprint(result_a)
    6
    >>> pprint(result_b)
    8
"""

# Value 2 times 3
# type: int
result_a = 2 * 3

# Value 2 to the power of 3
# type: int
result_b = 2 ** 3


