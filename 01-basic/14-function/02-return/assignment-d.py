"""
* Assignment: Function Return Tuple
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify function `get_user()`
    2. Function should return a tuple: 'Mark', 'Watney'
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `get_user`
    2. Funkcja powinna zwracać krotkę: 'Mark', 'Watney'
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert get_user is not Ellipsis, \
    'Write solution inside `get_user` function'
    >>> assert isfunction(get_user), \
    'Object `get_user` must be a function'

    >>> get_user()
    ('Mark', 'Watney')
"""

# Function should return a tuple: 'Mark', 'Watney'
# type: Callable[[], tuple[str,str]]
def get_user():
    return 'Mark', 'Watney'

