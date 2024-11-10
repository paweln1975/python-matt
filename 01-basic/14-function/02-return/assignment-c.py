"""
* Assignment: Function Return Expression
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify function `add()`
    2. Function should return sum of `1` and `2`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `add()`
    2. Funkcja powinna zwracać sumę `1` i `2`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert add is not Ellipsis, \
    'Write solution inside `add` function'
    >>> assert isfunction(add), \
    'Object `add` must be a function'

    >>> add()
    3
"""

# Function should return sum of `1` and `2`
# type: Callable[[], int]
def add():
    return 1 + 2

