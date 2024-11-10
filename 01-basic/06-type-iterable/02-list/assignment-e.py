"""
* Assignment: Type List Sort
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Sort `result`
    2. Run doctests - all must succeed

Polish:
    1. Posortuj `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> result
    ['a', 'b', 'c']
"""

result = ['c', 'a', 'b']


# Sort `result`
# type: list
result.sort()

