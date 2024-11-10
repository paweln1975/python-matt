"""
* Assignment: OOP Inheritance None
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 2 min

English:
    1. Define class `Account` inheriting from object
    2. Define class `User` inheriting from object
    3. Define class `Admin` inheriting from object
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Account` dziedziczącą po object
    2. Zdefiniuj klasę `User` dziedziczącą po object
    3. Zdefiniuj klasę `Admin` dziedziczącą po object
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert issubclass(Account, object)
    >>> assert issubclass(Account, Account)
    >>> assert not issubclass(Account, User)
    >>> assert not issubclass(Account, Admin)

    >>> assert isclass(User)
    >>> assert issubclass(User, object)
    >>> assert not issubclass(User, Account)
    >>> assert issubclass(User, User)
    >>> assert not issubclass(User, Admin)

    >>> assert isclass(Admin)
    >>> assert issubclass(Admin, object)
    >>> assert not issubclass(Admin, Account)
    >>> assert not issubclass(Admin, User)
    >>> assert issubclass(Admin, Admin)
"""

# Define class `Account` inheriting from object
class Account():
    pass

# Define class `User` inheriting from object
class User():
    pass

# Define class `Admin` inheriting from object
class Admin():
    pass


