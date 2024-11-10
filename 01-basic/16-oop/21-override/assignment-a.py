"""
* Assignment: OOP Override Method
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Use class `User`
    2. Modify class `Admin` to display `Admin login` in `login()` method
    3. Do not change inheritance
    4. Run doctests - all must succeed

Polish:
    1. Użyj klasy `User`
    2. Zmodyfikuj klasę `Admin` tak aby w metodzie `login()` wyświetlała `Admin login`
    3. Nie zmieniaj dziedziczenia
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User()
    >>> mark.login()
    User login

    >>> melissa = Admin()
    >>> melissa.login()
    Admin login
"""

class User:
    def login(self):
        print('User login')


# Modify class `Admin` to display `Admin login` in `login()` method
# Do not change inheritance
class Admin(User):
    def login(self):
        print('Admin login')



class User:
    def login(self):
        classname = __class__.__name__
        print(f'{classname} login')

class Admin(User):
    pass
