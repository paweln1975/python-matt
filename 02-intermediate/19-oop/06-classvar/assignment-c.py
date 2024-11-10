"""
* Assignment: OOP ClassVar Validate
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify class User
    2. Use `AGE_MIN` and `AGE_MAX` to validate `age`
    3. On `age` out of range, raise `ValueError('Invalid age')`
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę User
    2. Użyj `AGE_MIN` i `AGE_MAX` do walidacji `age`
    3. Przy `age` spoza zakresu, podnieś `ValueError('Invalid age')`
    4. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> mark = User('Mark', 'Watney', 40)
    >>> melissa = User('Melissa', 'Lewis', 66)
    Traceback (most recent call last):
    ValueError: Invalid age
    >>> rick = User('Rick', 'Martinez', 17)
    Traceback (most recent call last):
    ValueError: Invalid age
"""


# Modify class User
# Use AGE_MIN and AGE_MAX to validate age
# On age out of range, raise ValueError('Invalid age')
# type: type[User]
class User:
    AGE_MIN = 18
    AGE_MAX = 65

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


