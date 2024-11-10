"""
* Assignment: Operator String Repr
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Modify `User` to overwrite `__str__()` method
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User` aby nadpisać metodę `__repr__()`
    2. Uruchom doctesty - wszystkie muszą się powieść
"""

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


