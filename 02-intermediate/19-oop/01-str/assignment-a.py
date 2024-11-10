"""
* Assignment: Operator String Str
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify `User` to overwrite `__str__()` method
    2. Printing object should return firstname and lastname,
       example: Mark Watney
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User` aby nadpisać metodę `__str__()`
    2. Wypisanie obiektu powinno zwrówić imię i nazwisko,
       przykład: Mark Watney
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User('Mark', 'Watney')
    >>> print(mark)
    Mark Watney

    >>> melissa = User('Melissa', 'Lewis')
    >>> print(melissa)
    Melissa Lewis
"""

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# Modify `User` class to overwrite `str()`
# Printing object should return firstname and lastname,
# example: Mark Watney

