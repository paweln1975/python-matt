"""
* Assignment: Function Return None
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify function `empty()`
    2. Function should return value `None`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `empty()`
    2. Funkcja powinna zwracać wartość `None`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert empty is not Ellipsis, \
    'Write solution inside `one` function'
    >>> assert isfunction(empty), \
    'Object `empty` must be a function'

    >>> print(empty())
    None
"""

# Function should return value `1`
# type: Callable[[], None]
def empty():
    return None

