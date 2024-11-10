"""
* Assignment: Operator String Repr
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify `User` to overwrite `__str__()` method
    2. Method should return proper class name on inheritance
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj metodę `__repr__()`
    2. Metoda powinna zwracać odpowiednią nazwę klasy przy dziedziczeniu
    3. Uruchom doctesty - wszystkie muszą się powieść
"""

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        firstname = self.firstname
        lastname = self.lastname
        return f'User({firstname=}, {lastname=})'


class Admin(User):
    pass


