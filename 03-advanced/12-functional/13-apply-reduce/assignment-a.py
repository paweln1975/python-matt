"""
* Assignment: Iterator Reduce Evaluate
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result: int` with sum of `data`
    2. Note, that all the time you are working on a data stream
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: int` ze sumą z `data`
    2. Zwróć uwagę, że cały czas pracujesz na strumieniu danych
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(odd), \
    'Object `odd` must be a function'
    >>> assert isfunction(cube), \
    'Object `cube` must be a function'
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is int, \
    'Variable `result` has invalid type, should be int'

    >>> result
    1225
"""

def odd(x):
    return x % 2


def cube(x):
    return x ** 3


data = range(0, 10)
data = filter(odd, data)
data = map(cube, data)

# Calculate sum of `data`
# Use reduce()
# type: int
result = ...

