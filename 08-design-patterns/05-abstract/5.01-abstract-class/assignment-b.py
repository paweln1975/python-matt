"""
Name: OOP AbstractClass Implementation
Difficulty: easy
Lines: 5
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass, isabstract, ismethod

>>> assert isclass(Account)
>>> assert isclass(User)
>>> assert isabstract(Account)
>>> assert not isabstract(User)
>>> assert hasattr(Account, 'login')
>>> assert hasattr(Account, 'logout')
>>> assert hasattr(User, 'login')
>>> assert hasattr(User, 'logout')
>>> assert not hasattr(User.login, '__isabstractmethod__')
>>> assert not hasattr(User.logout, '__isabstractmethod__')
>>> assert hasattr(Account.login, '__isabstractmethod__')
>>> assert hasattr(Account.logout, '__isabstractmethod__')
>>> assert Account.login.__isabstractmethod__ == True
>>> assert Account.logout.__isabstractmethod__ == True

>>> result = Account()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Account without an implementation for abstract methods 'login', 'logout'
>>> result = User()
>>> assert ismethod(result.login)

"""

# %% SetUp

from abc import ABC, abstractmethod

Account: type
User: type
login: abstractmethod
logout: abstractmethod

# English
# 1. Define class `User` inheriting from `Account`
# 2. Overwrite all abstract methods, leave `pass` as content
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `User` dziedziczące po `Account`
# 2. Nadpisz wszystkie metody abstrakcyjne, pozostaw `pass` jako treść
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Account(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

# Define class `User` inheriting from `Account`
# Overwrite all abstract methods, leave `pass` as content
class User:
    pass