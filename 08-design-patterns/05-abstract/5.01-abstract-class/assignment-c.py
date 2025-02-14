"""
Name: OOP AbstractClass Implement
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isabstract, isclass, ismethod, signature

>>> assert isclass(Account)
>>> assert isabstract(Account)
>>> assert hasattr(Account, '__init__')
>>> assert hasattr(Account, 'login')
>>> assert hasattr(Account, 'logout')
>>> assert hasattr(Account.login, '__isabstractmethod__')
>>> assert hasattr(Account.logout, '__isabstractmethod__')
>>> assert Account.login.__isabstractmethod__ == True
>>> assert Account.logout.__isabstractmethod__ == True

>>> Account.__annotations__
{'firstname': <class 'str'>, 'lastname': <class 'str'>}

>>> Account.__init__.__annotations__
{'firstname': <class 'str'>, 'lastname': <class 'str'>, 'return': None}

>>> Account.login.__annotations__
{'username': <class 'str'>, 'password': <class 'str'>, 'return': None}

>>> Account.logout.__annotations__
{'return': None}

>>> assert isclass(User)
>>> result = User(firstname='Mark', lastname='Watney')

>>> result.__annotations__
{'firstname': <class 'str'>, 'lastname': <class 'str'>}

>>> assert hasattr(result, '__init__')
>>> assert hasattr(result, 'logout')
>>> assert hasattr(result, 'login')

>>> assert ismethod(result.__init__)
>>> assert ismethod(result.logout)
>>> assert ismethod(result.login)

>>> signature(result.__init__)  # doctest: +NORMALIZE_WHITESPACE
<Signature (firstname: str, lastname: str) -> None>
>>> signature(result.login)
<Signature (username: str, password: str) -> None>
>>> signature(result.logout)
<Signature () -> None>

>>> assert result.login('mwatney', 'Ares3') is None, 'Do not implement login() method'
>>> assert result.logout() is None, 'Do not implement logout() method'

"""

# %% SetUp

from abc import ABC, abstractmethod

Account: type
User: type
login: abstractmethod
logout: abstractmethod

class Account(ABC):
    firstname: str
    lastname: str

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @abstractmethod
    def login(self, username: str, password: str) -> None:
        ...

    @abstractmethod
    def logout(self) -> None:
        ...

# English
# 1. Define class `User` implementing `Account`
# 2. Overwrite all abstract methods, leave `pass` as content
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `User` implementującą `Account`
# 2. Nadpisz wszystkie metody abstrakcyjne, pozostaw `pass` jako treść
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class User:
    pass