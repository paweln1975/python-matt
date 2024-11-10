"""
* Assignment: Function Return Capture
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with result of `add` function call
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result` z wynikiem wywołania funkcji `compute`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(add), \
    'Object `add` must be a function'
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is int, \
    'Variable `result` has invalid type, should be int'

    >>> result
    3
"""

def add():
    return 1 + 2


# Result of `add` function call
# type: int
result = add()

