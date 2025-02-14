"""
Name: OOP AbstractClass Syntax
Difficulty: easy
Lines: 8
Minutes: 3

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass, isabstract, ismethod

>>> assert isclass(Account)
>>> assert isabstract(Account)
>>> assert hasattr(Account, 'login')
>>> assert hasattr(Account, 'logout')
>>> assert hasattr(Account.login, '__isabstractmethod__')
>>> assert hasattr(Account.logout, '__isabstractmethod__')
>>> assert Account.login.__isabstractmethod__ == True
>>> assert Account.logout.__isabstractmethod__ == True

>>> result = Account()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Account without an implementation for abstract methods 'login', 'logout'

"""

# %% SetUp

from abc import ABC, abstractmethod

Account: type
login: abstractmethod
logout: abstractmethod

# English
# 1. Create abstract class `Account`
# 2. Define abstract methods `login()` and `logout()`
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę abstrakcyjną `Account`
# 2. Zdefiniuj metody abstrakcyjne `login()` i `logout()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
