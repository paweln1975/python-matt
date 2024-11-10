"""
* Assignment: Function Return Dict
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify function `get_data()`
    2. Function should return a dict:
       {'firstname': 'Mark', 'lastname': 'Watney'}
    3. Do not use built-in function `locals()`
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `get_data`
    2. Funkcja powinna zwracać dict:
       {'firstname': 'Mark', 'lastname': 'Watney'}
    3. Nie używaj wbudowanej funkcji `locals()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert get_data is not Ellipsis, \
    'Write solution inside `get_data` function'
    >>> assert isfunction(get_data), \
    'Object `get_data` must be a function'

    >>> get_data()
    {'firstname': 'Mark', 'lastname': 'Watney'}
"""

# Function should return a dict:
# {'firstname': 'Mark', 'lastname': 'Watney'}
def get_data():
    firstname = 'Mark'
    lastname = 'Watney'
    return dict(firstname=firstname, lastname=lastname)
