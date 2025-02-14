"""
Name: OOP AbstractInterface Implement
Difficulty: easy
Lines: 10
Minutes: 5

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isfunction

>>> assert issubclass(User, Account)
>>> assert hasattr(User, '__init__')
>>> assert hasattr(User, 'login')
>>> assert hasattr(User, 'logout')

>>> assert isfunction(User.__init__)
>>> assert isfunction(User.login)
>>> assert isfunction(User.logout)

>>> User.__annotations__  # doctest: +NORMALIZE_WHITESPACE
{'username': <class 'str'>,
 'password': <class 'str'>}

>>> mark = User(username='mwatney', password='Ares3')
>>> mark.login()
'User login'
>>> mark.logout()
'User logout'

Hints:
`vars(self).values()`

"""

# %% SetUp

from typing import Callable
User: type
__init__: Callable[[object, str, str], Exception]
login: Callable[[object], Exception]
logout: Callable[[object], Exception]

class Account:
    def __init__(self, username: str, password: str) -> None:
        raise NotImplementedError

    def login(self) -> str:
        raise NotImplementedError

    def logout(self) -> str:
        raise NotImplementedError

# English
# 1. Define class `User` implementing `Account`
# 2. Implement methods:
#    - `__init__()` sets fields
#    - `login()` returns 'User login'
#    - `logout()` returns 'User logout'
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `User` implementującą `Account`
# 2. Zaimplementuj metody:
#    - `__init__` ustawia pola klasy
#    - `login()` zwraca 'User login'
#    - `logout()` zwraca 'User logout'
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class User(Account):
    ...