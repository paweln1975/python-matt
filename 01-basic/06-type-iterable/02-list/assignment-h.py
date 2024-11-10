"""
* Assignment: Type List Insert
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Delete element 'x' from `result`
    2. Do not hardcode the position of `x`
    3. Run doctests - all must succeed

Polish:
    1. Usuń element 'x' z `result`
    2. Nie wpisuj na sztywno pozycji `x`
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
    ['a', 'b', 'c']
"""

result = ['a', 'x', 'b', 'c']


# Delete element 'x' from `result`
# Do not hardcode the position of `x`
# type: list
del result[result.index('x')]

