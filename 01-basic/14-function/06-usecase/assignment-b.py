"""
* Assignment: Function Usecase Min
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Define function `mymin`:
       a. takes `data: list[int|float]`
       b. returns lowest value in `data`
    2. Do not use built-in function `min()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `mymin`:
       a. przyjmuje `data: list[int|float]`
       b. zwraca tuplę z najmniejszą wartością z `data`
    2. Nie używaj wbudowanej funkcji `min()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert mymin is not Ellipsis, \
    'Write solution inside `mymin` function'
    >>> assert isfunction(mymin), \
    'Object `mymin` must be a function'

    >>> mymin([3,1,2])
    1

    >>> mymin([3,1,2,6,4,5])
    1
"""

# Define function `mymin`:
# - takes `data: list[int|float]`
# - returns tuple with min and max value from `data`
# Do not use built-in `min()` and `max()` functions
# type: Callable[[list[int|float]], int]
def mymin(iterable):
    current_min = None
    for v in iterable:
        if current_min is None:
            current_min = v
            continue
        if v < current_min:
            current_min = v
    return current_min

