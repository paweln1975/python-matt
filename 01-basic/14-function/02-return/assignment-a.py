"""
* Assignment: Function Return Int
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify function `one()`
    2. Function should return value `1`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `one()`
    2. Funkcja powinna zwracać wartość `1`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert one is not Ellipsis, \
    'Write solution inside `one` function'
    >>> assert isfunction(one), \
    'Object `one` must be a function'

    >>> one()
    1
"""

# Function should return value `1`
# type: Callable[[], int]
def one():
    return 1

