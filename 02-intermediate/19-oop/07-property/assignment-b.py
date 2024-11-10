"""
* Assignment: OOP Property Age
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define property `age` in class `User`
    2. Accessing `age` should return user's age in full years
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj property `age` w klasie `User`
    2. Dostęp do `age` powinien zwrócić wiek użytkownika w pełnych latach
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * date.today()
    * timedelta.days
    * int()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from datetime import date
    >>> age = date.today().year - 2000

    >>> mark = User(
    ...     firstname='Mark',
    ...     lastname='Watney',
    ...     birthdate=date(2000, 1, 1))

    >>> assert hasattr(mark, 'age'), \
    'Define property `age`'

    >>> assert mark.age == age, \
    f'Invalid age "{mark.age}", should be "{age}"'
"""

from datetime import date

YEAR = 365.25

# Define property `age` in class `User`
# Accessing `age` should return user's age in full years
# type: Callable[[Self], int]
class User:
    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate


