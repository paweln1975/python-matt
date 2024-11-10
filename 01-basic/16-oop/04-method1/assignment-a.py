"""
* Assignment: OOP Method One
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify class `User`
    2. Define method `login` in class `User`
    3. Method prints 'User login'
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`
    2. Zdefiniuj metodę `login` w klasie `User`
    3. Metoda wypisuje 'User login'
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(User)
    >>> mark = User()
    >>> assert ismethod(mark.login)

    >>> mark.login()
    User login
"""

# Define method `login` in class `User`
# Method prints 'User login'
class User:
    def login(self):
        print('User login')


