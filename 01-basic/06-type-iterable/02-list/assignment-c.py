"""
* Assignment: Type List Append
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Insert character 'x' at the end of `result`
    2. Run doctests - all must succeed

Polish:
    1. Wstaw znak 'x' na końcu `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> result
    ['a', 'b', 'c', 'x']
"""

result = ['a', 'b', 'c']


# Insert string 'x' at the end of `result`
# type: list
result.append('x')

