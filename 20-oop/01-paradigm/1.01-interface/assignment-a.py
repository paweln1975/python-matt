"""
Name: OOP AbstractInterface Define
Difficulty: easy
Lines: 9
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isfunction

>>> assert hasattr(Account, '__init__')
>>> assert hasattr(Account, 'login')
>>> assert hasattr(Account, 'logout')

>>> assert isfunction(Account.__init__)
>>> assert isfunction(Account.login)
>>> assert isfunction(Account.logout)

>>> mark = Account(username='mwatney', password='Ares3')
Traceback (most recent call last):
NotImplementedError

>>> Account.login(None)
Traceback (most recent call last):
NotImplementedError

>>> Account.logout(None)
Traceback (most recent call last):
NotImplementedError

"""

# %% SetUp

from typing import Callable
Account: type
__init__: Callable[[object, str, str], Exception]
login: Callable[[object], Exception]
logout: Callable[[object], Exception]

# English
# 1. Define interface `Account` with:
#    - Methods: `__init__()`, `login()`, `logout()`
#    - Init parameters: `username`, `password`
# 2. All methods must raise exception `NotImplementedError`
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj interfejs `Account` z:
#    - Metody: `__init__()`, `login()`, `logout()`
#    - Parametry init: `username`, `password`
# 2. Wszystkie metody muszą podnosić wyjątek `NotImplementedError`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
