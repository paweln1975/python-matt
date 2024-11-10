"""
* Assignment: OOP Stringify Str
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use class `User`
    2. Define `__str__` method for printing instance information
    3. Method should display attributes and their values
       example: `Mark Watney`
    3. Run doctests - all must succeed

Polish:
    1. Użyj klasy `User`
    2. Zdefiniuj metodę `__str__` do informaji o instancji
    3. Method should display attributes and their values
       example: `Mark Watney`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')
    >>> assert hasattr(User, '__str__')

    >>> mark = User('Mark', 'Watney')
    >>> result = str(mark)
    >>> pprint(result)
    'Mark Watney'
"""

# Define `__str__` method for printing instance information
# Method should display attributes and their values
# example: `Mark Watney`
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        firstname = self.firstname
        lastname = self.lastname
        return f'User({firstname=}, {lastname=})'

