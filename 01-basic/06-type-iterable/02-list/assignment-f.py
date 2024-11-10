"""
* Assignment: Type List Reverse
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Reverse order of `result` (do not sort)
    2. Run doctests - all must succeed

Polish:
    1. Odwróć kolejność `result` (nie sortuj)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> result
    ['b', 'a', 'c']
"""

result = ['c', 'a', 'b']


# Reverse order of `result` (do not sort)
# type: list
result.reverse()

