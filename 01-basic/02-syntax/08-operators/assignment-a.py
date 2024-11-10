"""
* Assignment: Syntax Operators Add/Sub
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define variable `result` with
        a. `result_a` with value 1 plus 2
        b. `result_b` with value 1 minus 2
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną:
        a. `result_a` z wartością 1 plus 2
        b. `result_b` z wartością 1 minus 2
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

    >>> assert result_a == 3, \
    'Variable `result_a` has invalid value, should be 3'
    >>> assert result_b == -1, \
    'Variable `result_b` has invalid value, should be -1'

    >>> pprint(result_a)
    3
    >>> pprint(result_b)
    -1
"""


# Value of 1 plus 2
# type: int
result_a = 1 + 2

# Value of 1 minus 2
# type: int
result_b = 1 - 2


