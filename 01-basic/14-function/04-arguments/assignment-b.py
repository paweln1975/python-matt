
"""
* Assignment: Function Arguments Divide
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `divide`:
        a. parameter `a: int` - first number (required)
        b. parameter `b: int` - second number (required)
        c. return result of division of both arguments
    2. If division cannot be made
        a. print "Argument `b` cannot be zero"
        b. return None
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `divide`:
        a. parametr `a: int` - pierwsza liczba (wymagany)
        b. parametr `b: int` - druga liczba (wymagany)
        c. zwróć wynik dzielenia obu argumentów
    2. Jeżeli dzielenie nie może być wykonane
        a. wypisz "Argument `b` cannot be zero"
        b. zwróć None
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert divide is not Ellipsis, \
    'Write solution inside `divide` function'
    >>> assert isfunction(divide), \
    'Object `divide` must be a function'

    >>> divide(4, 0)
    Argument `b` cannot be zero

    >>> divide(4, 2)
    2.0
"""

# Define function `divide`:
# - parameter `a: int` - first number (required)
# - parameter `b: int` - second number (required)
# - return result of division of both arguments
# If division cannot be made
# - print "Argument `b` cannot be zero"
# - return None
# type: Callable[[int, int], float]
def divide(a, b):
    if not b:
        print("Argument `b` cannot be zero")
        return None
    return a / b


