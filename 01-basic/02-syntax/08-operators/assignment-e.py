"""
* Assignment: Syntax Operators Even
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with result
       of checking if `NUMBER` is even
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z wynikiem
       sprawdzenia czy `NUMBER` jest parzyste
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is bool, \
    'Variable `result` has invalid type, should be bool'

    >>> assert result == 1, \
    'Variable `result` has invalid value, should be 1'

    >>> pprint(result)
    1
"""

NUMBER = 4

# Result of checking if `NUMBER` is even
# type: bool
result = NUMBER % 2 == 0

