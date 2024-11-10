"""
* Assignment: OOP AbstractClass Implementation
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define class `User` implementing `Account`
    2. Overwrite all abstract methods
    3. Leave `pass` as content
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `User` implementującą `Account`
    2. Nadpisz wszystkie metody abstrakcyjne
    3. Pozostaw `pass` jako treść
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
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
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


# Define class `User` implementing `Account`
# Overwrite all abstract methods
# Leave `pass` as content
class User:
    ...


