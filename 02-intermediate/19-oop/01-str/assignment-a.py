
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> mark = User('Mark', 'Watney')
>>> print(mark)
Mark Watney

>>> melissa = User('Melissa', 'Lewis')
>>> print(melissa)
Melissa Lewis
"""
# endregion

# region Show Types
from typing import Callable
User: type
__str__: Callable[[object], str]
# endregion

# English
# 1. Modify `User` to overwrite `__str__()` method
# 2. Printing object should return firstname and lastname,
#    example: Mark Watney
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `User` aby nadpisać metodę `__str__()`
# 2. Wypisanie obiektu powinno zwrócić imię i nazwisko,
#    przykład: Mark Watney
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
