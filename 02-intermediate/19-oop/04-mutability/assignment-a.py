
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass
>>> assert isclass(User)
>>> assert hasattr(User, '__annotations__')

>>> mark = User('mwatney', 'Ares3')
>>> melissa = User('mlewis', 'Nasa1')
>>> assert 'firstname' in vars(mark)
>>> assert 'lastname' in vars(mark)
>>> assert 'groups' in vars(mark)
>>> assert 'firstname' in vars(melissa)
>>> assert 'lastname' in vars(melissa)
>>> assert 'groups' in vars(melissa)
>>> assert mark.groups is not melissa.groups
"""
# endregion

# region Show Types
from typing import Callable
User: type
__init__: Callable[[str, str, list[str]], None]
# endregion

# English
# 1. Create class `User`, with attributes:
#    - `firstname: str` (required)
#    - `lastname: str` (required)
#    - `groups: list[str]` (optional)
# 2. Attributes must be set at the initialization from constructor arguments
# 3. Avoid mutable parameter problem
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `User`, z atrybutami:
#    - `firstname: str` (wymagane)
#    - `lastname: str` (wymagane)
#    - `groups: list[str]` (opcjonalne)
# 2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
# 3. Uniknij problemu mutowalnych parametrów
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups if groups is not None else []
