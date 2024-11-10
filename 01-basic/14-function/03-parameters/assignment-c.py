"""
* Assignment: Function Parameters Sum
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `total`:
       a. takes `data: list[int|float]`
       b. returns sum of all values in a list
    2. Do not use built-in `sum()` function
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `total`:
       a. przyjmuje `data: list[int|float]`
       b. zwraca sumę wszystkich wartości z listy
    2. Nie używaj wbudowanej funkcji `sum`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert total is not Ellipsis, \
    'Write solution inside `total` function'
    >>> assert isfunction(total), \
    'Object `total` must be a function'

    >>> total([1,2,3])
    6
    >>> total([1,2,3,4,5,6])
    21
"""
from cgitb import reset


# Define function `total`:
# - takes `data: list[int|float]`
# - returns sum of all values in a list
# Do not use built-in `sum()` function
# type: Callable[[tuple|list|set], int]
def total(number_list):
    result = 0
    for number in number_list:
        result += number
    return result


