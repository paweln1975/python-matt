"""
* Assignment: OOP Override Super
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use class `User`
    2. Use class `Admin` inheriting from `User`
    3. In `Admin.login()` method call `login()` method of a parent class
    4. Use `super()` method
    5. Do not change inheritance
    6. Run doctests - all must succeed

Polish:
    1. Użyj klasy `User`
    2. Użyj klasy `Admin` dziedziczącej po `User`
    3. W metodzie `Admin.login()` wywołaj metodę `login()` klasy nadrzędnej
    4. Użyj metody `super()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User('Mark', 'Watney')
    >>> mark.login()
    User login

    >>> melissa = User('Melissa', 'Lewis')
    >>> melissa.login()
    User login
"""


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def login(self):
        print('User login')


# In `Admin.login()` method call `login()` method of a parent class
# Use `super()` method
# Do not change inheritance
class Admin(User):
    def login(self):
        super().login()


