"""
* Assignment: OOP Field Define
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify instance `mark`
    2. Add field `firstname` with value 'Mark'
    3. Add field `lastname` with value 'Watney'
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj instancję `mark`
    2. Dodaj pole `firstname` o wartości 'Mark'
    3. Dodaj pole `lastname` o wartości 'Watney'
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert isinstance(mark, User)
    >>> assert hasattr(mark, 'firstname')
    >>> assert hasattr(mark, 'lastname')
    >>> assert getattr(mark, 'firstname') == 'Mark'
    >>> assert getattr(mark, 'lastname') == 'Watney'
"""

class User:
    pass

mark = User()

# Modify instance `mark`
# Add field `firstname` with value 'Mark'
# type: str
mark.firstname = 'Mark'

# Modify instance `mark`
# Add field `lastname` with value 'Watney'
# type: str
mark.lastname = 'Watney'

