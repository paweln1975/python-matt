"""
* Assignment: Syntax Types IsInstance
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with
       result of checking if DATA is an instance of an int
    2. Use `isinstance()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z
       rezultatem sprawdzania czy DATA jest instancją int
    2. Użyj `isinstance()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is bool, \
    'Variable `result` has invalid type, should be bool'

    >>> assert result is True, \
    'Variable `result` has invalid value, should be True'

    >>> pprint(result)
    True
"""

DATA = 1

# With value result of checking if DATA is an instance of an int
# type: bool
result = isinstance(DATA, int)


