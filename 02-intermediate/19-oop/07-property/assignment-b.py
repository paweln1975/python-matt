
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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
# endregion

# region Show Imports
from datetime import date
# endregion

# region Show Types
User: type
age: property
# endregion

YEAR = 365.25

# English
# 1. Define property `age` in class `User`
# 2. Accessing `age` should return user's age in full years
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj property `age` w klasie `User`
# 2. Dostęp do `age` powinien zwrócić wiek użytkownika w pełnych latach
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `date.today()`
# - `timedelta.days`
# - `int()`
# endregion

# %% Your code
class User:
    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    @property
    def age(self):
        diff = date.today() - self.birthdate
        return int(diff.days / YEAR)
