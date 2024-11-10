"""
* Assignment: Syntax Types Type
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with
       result of type cheking of variable DATA
    2. Use `type()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z
       rezultatem sprawdzania typu zmiennej DATA
    2. Użyj `type()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is type, \
    'Variable `result` has invalid type, should be type'

    >>> assert result is int, \
    'Variable `result` has invalid value, should be int'

    >>> pprint(result)
    <class 'int'>
"""

DATA = 1

# With value result of type cheking of DATA
# type: type[int]
result = type(DATA)



