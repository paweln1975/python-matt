"""
* Assignment: Type List Insert
* Type: class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variables:
        a. `result_a` with shallow copy of `data` (by reference)
        b. `result_b` with deep copy of `data` (by value)
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne:
        a. `result_a` z płytką kopią `data` (przez referencję)
        b. `result_b` z głęboką kopią `data` (przez wartość)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'

    >>> assert type(result_a) is list, \
    'Variable `result_a` has invalid type, should be list'
    >>> assert type(result_b) is list, \
    'Variable `result_b` has invalid type, should be list'

    >>> assert 'x' not in result_a, \
    'Variable `result_a` should not contain `x`'
    >>> assert 'x' not in result_b, \
    'Variable `result_b` should not contain `x`'

    >>> assert result_a == data, \
    'Variable `result_a` should be identical to `data`'
    >>> assert result_b == data, \
    'Variable `result_b` should be identical to `data`'

    >>> assert result_a is data, \
    'Variable `result_a` should be shallow copy of `data`'

    >>> assert result_b is not data, \
    'Variable `result_b` shouldn be deep copy of `data`'

    >>> result_a
    ['a', 'b', 'c']
    >>> result_b
    ['a', 'b', 'c']
"""

data = ['a', 'b', 'c']


# Shallow copy of `data` (by reference)
# type: list
result_a = data

# Deep copy of `data` (by value)
# type: list
result_b = data.copy()


