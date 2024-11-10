"""
* Assignment: Function Usecase Len
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define function `mylen`:
       a. takes `data: list`
       b. returns number of elements in `data`
    2. Do not use built-in `len()` function
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `mylen`:
       a. przyjmuje `data: list`
       b. zwraca liczbe elementów w `data`
    2. Nie używaj wbudowanej funkcji `len`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert mylen is not Ellipsis, \
    'Write solution inside `mylen` function'
    >>> assert isfunction(mylen), \
    'Object `mylen` must be a function'

    >>> mylen([1,2,3])
    3

    >>> mylen([1,2,3,4,5,6])
    6
"""

# Define function `mylen`:
# - takes `data: list`
# - returns number of elements in `data`
# Do not use built-in `len()` function
# type: Callable[[list], int]
def mylen(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count


