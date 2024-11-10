"""
* Assignment: OOP ClassVar Class
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify class User
    2. Add class variables:
        a. AGE_MIN (default 18)
        b. AGE_MAX (default 65)
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę User
    2. Dodaj pola klasowe:
        a. AGE_MIN (domyślnie 18)
        b. AGE_MAX (domyślnie 65)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)

    >>> fields = User.__dict__
    >>> assert 'firstname' not in fields
    >>> assert 'lastname' not in fields
    >>> assert 'age' not in fields
    >>> assert 'AGE_MIN' in fields
    >>> assert 'AGE_MAX' in fields
    >>> assert fields['AGE_MIN'] == 18
    >>> assert fields['AGE_MAX'] == 65

    >>> fields = User('Mark', 'Watney', 40).__dict__
    >>> assert 'firstname' in fields
    >>> assert 'lastname' in fields
    >>> assert 'age' in fields
    >>> assert 'AGE_MIN' not in fields
    >>> assert 'AGE_MAX' not in fields
    >>> assert fields['firstname'] == 'Mark'
    >>> assert fields['lastname'] == 'Watney'
    >>> assert fields['age'] == 40
"""


# Modify class User
# Add class variables:
# - AGE_MIN (default 18)
# - AGE_MAX (default 65)
# type: type[User]
class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


