"""
* Assignment: Syntax Operators Increment
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Increment variable `result` by 1
    2. Use `+=` operator
    3. Run doctests - all must succeed

Polish:
    1. Zwiększ zmienną `result` o 1
    2. Użyj operatora `+=`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is int, \
    'Variable `result` has invalid type, should be int'

    >>> assert result == 1, \
    'Variable `result` has invalid value, should be 1'

    >>> pprint(result)
    1
"""

result = 0

# Increment result by 1
# Use `+=` operator
# type: int
result += 1


