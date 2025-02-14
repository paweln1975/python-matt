
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> mark = User('Mark', 'Watney')
>>> mark
User(firstname='Mark', lastname='Watney')

>>> melissa = Admin('Melissa', 'Lewis')
>>> melissa
Admin(firstname='Melissa', lastname='Lewis')
"""
# endregion

# region Show Types
from typing import Callable
User: type
Admin: type
__repr__: Callable[[object], str]
# endregion

# English
# 1. Modify `User` to overwrite `__repr__()` method
# 2. Method should return proper class name on inheritance
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `User` aby nadpisać metodę `__repr__()`
# 2. Metoda powinna zwracać odpowiednią nazwę klasy przy dziedziczeniu
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        classname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        return f'{classname}({firstname=}, {lastname=})'

class Admin(User):
    pass
