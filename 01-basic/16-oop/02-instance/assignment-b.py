"""
* Assignment: OOP Instance Many
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Create instance `mark` of a class `User`
    2. Create instance `melissa` of a class `Admin`
    3. Create instance `rick` of a class `User`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz instancję `mark` klasy `User`
    2. Stwórz instancję `melissa` klasy `Admin`
    3. Stwórz instancję `rick` klasy `User`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert isclass(Admin)

    >>> assert isinstance(mark, User)
    >>> assert isinstance(melissa, Admin)
    >>> assert isinstance(rick, User)
"""

class User:
    pass

class Admin:
    pass


# Create instance `mark` of a class `User`
# type: User
mark = User()

# Create instance `melissa` of a class `Admin`
# type: Admin
melissa = Admin()

# Create instance `rick` of a class `User`
# type: User
rick = User()


