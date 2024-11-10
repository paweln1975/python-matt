"""
* Assignment: Iterable Tuple Index
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define variable `result` with
       an index of an element `c` in `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result`
       z indeksem elementu `c` w `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is int, \
    'Variable `result` has invalid type, should be int'

    >>> assert result == 2, \
    'Variable `result` has invalid value. Check your calculations.'

    >>> pprint(result)
    2
"""

DATA = ('a', 'b', 'c', 'd')


# Index of an element `c` in `DATA`
# type: int
result = DATA.index('c')

