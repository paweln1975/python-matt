"""
* Assignment: Star Signature Class
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use class `User`
    2. Refactor method `__init__()` to require passing arguments:
        a. Positional-only: `firstname` and `lastname`
        b. Keyword-only: `birthdate`
    3. Run doctests - all must succeed

Polish:
    1. Użyj klasę `User`
    2. Zrefaktoruj metodę `__init__()` aby wymagała podawanie argumentów:
        a. Tylko pozycyjne: `firstname` i `lastname`
        b. Tylko nazwanie (keyword): `birthdate`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)

    >>> mark = User('Mark', 'Watney', birthdate='2000-01-02')
    >>> assert isinstance(mark, User)

    >>> User('Mark', 'Watney', '2000-01-02')
    Traceback (most recent call last):
    TypeError: User.__init__() takes 3 positional arguments but 4 were given

    >>> User('Mark', lastname='Watney', birthdate='2000-01-02')
    Traceback (most recent call last):
    TypeError: User.__init__() got some positional-only arguments passed as keyword arguments: 'lastname'

    >>> User(firstname='Mark', lastname='Watney', birthdate='2000-01-02')
    Traceback (most recent call last):
    TypeError: User.__init__() got some positional-only arguments passed as keyword arguments: 'firstname, lastname'
"""


# Refactor method `__init__()` to require passing arguments:
# - Positional-only: `firstname` and `lastname`
# - Keyword-only: `birthdate`
# type: type[User]
class User:
    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate


