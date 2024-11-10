"""
* Assignment: Function Usecase Max
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Define function `mymax`:
       a. takes `data: list[int|float]`
       b. returns the greatest value in `data`
    2. Do not use built-in function `max()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `mymax`:
       a. przyjmuje `data: list[int|float]`
       b. zwraca tuplę z największą wartością z `data`
    2. Nie używaj wbudowanej funkcji `max()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert mymax is not Ellipsis, \
    'Write solution inside `mymax` function'
    >>> assert isfunction(mymax), \
    'Object `mymax` must be a function'

    >>> mymax([3,1,2])
    3

    >>> mymax([3,1,2,6,4,5])
    6
"""

# Define function `mymax`:
# - takes `data: list[int|float]`
# - returns tuple with min and max value from `data`
# Do not use built-in `min()` and `max()` functions
# type: Callable[[list[int|float]], int]
def mymax(iterable):
    current_max = None
    for v in iterable:
        if current_max is None:
            current_max = v
            continue
        if v > current_max:
            current_max = v
    return current_max


