"""
* Assignment: Function Arguments Power
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `power`:
        a. parameter `a: int` - first number (required)
        b. parameter `b: int` - second number (optional)
        c. returns: power of the first argument to the second
    2. If only one argument was passed,
       consider second equal to the first one
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `power`:
        a. parametr `a: int` - pierwsza liczba (wymagany)
        b. parametr `b: int` - druga liczba (opcjonalny)
        c. zwraca: wynik pierwszego argumentu do potęgi drugiego
    2. Jeżeli tylko jeden argument był podany,
       przyjmij drugi równy pierwszemu
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert power is not Ellipsis, \
    'Write solution inside `power` function'
    >>> assert isfunction(power), \
    'Object `power` must be a function'

    >>> power(4, 3)
    64
    >>> power(3)
    27
"""


# Define function `power`:
# - parameter `a: int` - first number (required)
# - parameter `b: int` - second number (optional)
# - returns: power of the first argument to the second
# If only one argument was passed,
# consider second equal to the first one
# type: Callable[[int, int], int]
def power(a, b=None):
    return a ** b if b is not None else a ** a
