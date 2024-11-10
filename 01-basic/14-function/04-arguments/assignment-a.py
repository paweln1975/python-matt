
"""
* Assignment: Function Arguments Sequence
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `total`:
        a. parameter: list of integers (required)
        b. return: sum only even numbers
    2. Use `even()` to check if number is even
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `total`:
        a. parametr: lists liczb całkowitych (wymagany)
        b. zwraca: sumę tylko parzystych liczb
    2. Użyj `even()` do sprawdzenia czy liczba jest parzysta
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert total is not Ellipsis, \
    'Write solution inside `total` function'
    >>> assert isfunction(total), \
    'Object `total` must be a function'

    >>> data = [1, 2, 3, 4]
    >>> total(data)
    6

    >>> data = [2, -1, 0, 2]
    >>> total(data)
    4

    >>> data = list(range(0,101))
    >>> total(data)
    2550
"""

def even(x):
    return x % 2 == 0


# Define function `total()`:
# - parameter: sequence of integers
# - return: sum only even numbers
# Use `even()` to check if number is even
# type: Callable[[list[int]], int]
def total(interable):
    return sum(x for x in interable if even(x))

