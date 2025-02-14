
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> mark = User('Mark', 'Watney')
>>> mark
User(firstname='Mark', lastname='Watney')
"""
# endregion

# region Show Types
from typing import Callable
User: type
__repr__: Callable[[object], str]
# endregion

# English
# 1. Modify `User` to overwrite `__repr__()` method
# 2. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `User` aby nadpisać metodę `__repr__()`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self) -> str:
        return f"User(firstname='{self.firstname}', lastname='{self.lastname}')"
