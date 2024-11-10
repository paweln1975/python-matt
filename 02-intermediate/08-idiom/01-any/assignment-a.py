"""
* Assignment: Idiom Any IsAdmin
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: bool` with the result of checking
       if any user has admin role
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: bool` z wynikiem sprawdzenia
       czy którykolwiek użytkownik ma rolę admin
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is bool, \
    'Variable `result` has invalid type, should be bool'

    >>> result
    True
"""

class User:
    def __init__(self, firstname, lastname, role):
        self.lastname = lastname
        self.firstname = firstname
        self.role = role

    def is_admin(self):
        return self.role == 'admin'


USERS = [
    User('Mark', 'Watney', role='user'),
    User('Melissa', 'Lewis', role='admin'),
    User('Rick', 'Martinez', role='user'),
]

# Define `result: bool` with the result of checking
# if any user has admin role
# type: bool
result = ...

