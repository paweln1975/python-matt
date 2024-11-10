"""
* Assignment: Type List Insert
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Delete all elements from `result`
    2. Run doctests - all must succeed

Polish:
    1. Usuń wszystkie elementy `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> assert 'x' not in result, \
    'Variable `result` should not contain `x`'

    >>> result
    []
"""

result = ['a', 'b', 'c']


# Delete all elements from `result`
# type: list
result.clear()

