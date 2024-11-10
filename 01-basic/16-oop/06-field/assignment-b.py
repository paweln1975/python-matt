"""
* Assignment: OOP Field Define
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify instance `mark`
    2. Add field `is_authenticated` with value False
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj instancję `mark`
    2. Dodaj pole `is_authenticated` o wartości False
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert isinstance(mark, User)
    >>> assert hasattr(mark, 'is_authenticated')
    >>> assert getattr(mark, 'is_authenticated') is False
"""

class User:
    pass

mark = User()

# Modify instance `mark`
# Add field `is_authenticated` with value False
# type: bool
mark.is_authenticated = False


