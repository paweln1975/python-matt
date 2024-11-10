"""
* Assignment: OOP Instance One
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create instance `mark` of a class `Account`
    1. Run doctests - all must succeed

Polish:
    1. Stwórz instancję `mark` klasy `Account`
    1. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isinstance(mark, Account)
"""

class Account:
    pass


# Create instance `mark` of a class `Account`
# type: Account
mark = Account()


