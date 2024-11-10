"""
* Assignment: OOP ClassVar Instance
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify class User
    2. Add instance variable:
        a. `age`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę User
    2. Dodaj pole instancji:
        a. `age`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)

    >>> fields = User.__dict__
    >>> assert 'firstname' not in fields
    >>> assert 'lastname' not in fields
    >>> assert 'age' not in fields

    >>> fields = User('Mark', 'Watney', 40).__dict__
    >>> assert 'firstname' in fields
    >>> assert 'lastname' in fields
    >>> assert 'age' in fields
    >>> assert fields['firstname'] == 'Mark'
    >>> assert fields['lastname'] == 'Watney'
    >>> assert fields['age'] == 40
"""


# Modify class User
# Add instance variable `age`
# type: type[User]
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


