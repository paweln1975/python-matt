"""
* Assignment: Operator String Nested
* Type: class assignment
* Complexity: medium
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Modify classes to overwrite `__str__()` and `__repr__()` methods
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasy aby nadpisać metody `__str__()` and `__repr__()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Define `Accounts.__str__()`
    * Define `User.__str__()`
    * Define `Group.__repr__()`
    * Printing list will call repr on all elements

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = User('Mark', 'Watney')
    >>> print(result)
    Mark Watney
    >>> result = User('Melissa', 'Lewis')
    >>> print(result)
    Melissa Lewis
    >>> result = User('Rick', 'Martinez')
    >>> print(result)
    Rick Martinez

    >>> Group(gid=1, name='admins')
    1(admins)
    >>> Group(gid=2, name='staff')
    2(staff)
    >>> Group(gid=3, name='users')
    3(users)

    >>> result = Accounts(users=[])
    >>> print(result)
    <BLANKLINE>

    >>> result = User('Mark', 'Watney', groups=[
    ...     Group(gid=2, name='staff'),
    ... ])
    >>> print(result)
    Mark Watney member of [2(staff)]

    >>> result = User('Melissa', 'Lewis', groups=[
    ...     Group(gid=1, name='admins'),
    ...     Group(gid=2, name='staff'),
    ... ])
    >>> print(result)
    Melissa Lewis member of [1(admins), 2(staff)]

    >>> result = Accounts([
    ...     User('Mark', 'Watney', groups=[
    ...         Group(gid=2, name='staff'),
    ...     ]),
    ...     User('Melissa', 'Lewis', groups=[
    ...         Group(gid=1, name='admins'),
    ...         Group(gid=2, name='staff'),
    ...     ]),
    ...     User('Rick', 'Martinez'),
    ... ])
    >>>
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    Mark Watney member of [2(staff)]
    Melissa Lewis member of [1(admins), 2(staff)]
    Rick Martinez
"""


class Accounts:
    def __init__(self, users):
        self.users = users


class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups if groups else []


class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name


