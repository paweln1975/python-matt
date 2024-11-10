"""
* Assignment: Function Usecase AsTuple
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `astuple`:
       a. takes `data: dict`
       b. returns tuple with `data` values
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `astuple`:
       a. przyjmuje `data: dict`
       b. zwraca tuplę z wartościami z `data`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert astuple is not Ellipsis, \
    'Write solution inside `astuple` function'
    >>> assert isfunction(astuple), \
    'Object `astuple` must be a function'

    >>> astuple({'a':1, 'b':2, 'c':3})
    (1, 2, 3)

    >>> astuple({'firstname':'Mark', 'lastname':'Watney'})
    ('Mark', 'Watney')
"""

# Define function `astuple`:
# - takes `data: list[int|float]`
# - returns tuple with min and max value from `data`
# Do not use built-in `min()` and `max()` functions
# type: Callable[[dict], tuple]
def astuple(dictionary):
    return tuple(dictionary.values())


