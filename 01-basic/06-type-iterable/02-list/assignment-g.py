"""
* Assignment: Type List Insert
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Delete last element from `result`
    2. Do not use `getitem` or `slice`
    3. Run doctests - all must succeed

Polish:
    1. Usuń ostatni element z `result`
    2. Nie używaj `getitem` lub `slice`
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
    ['a', 'b']
"""

result = ['a', 'b', 'c']


# Delete last element from `result`
# Do not use `getitem` or `slice`
# type: list
result.pop()

