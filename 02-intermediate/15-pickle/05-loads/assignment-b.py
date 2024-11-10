

"""
* Assignment: Pickle Load ListObjects
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: list[User]` with data from `FILE`
    2. Use `pickle` module
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[User]` z danymi z `FILE`
    2. Użyj modułu `pickle`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(firstname='Mark', lastname='Watney', age=41, groups='1(users)'),
     User(firstname='Melissa', lastname='Lewis', age=40, groups='1(users),2(staff),3(admins)'),
     User(firstname='Rick', lastname='Martinez', age=39, groups='1(users)'),
     User(firstname='Alex', lastname='Vogel', age=40, groups=''),
     User(firstname='Beth', lastname='Johanssen', age=29, groups='1(users),2(staff)'),
     User(firstname='Chris', lastname='Beck', age=36, groups='1(users)')]
"""

import pickle

FILE = r'_temporary.pkl'

DATA = (
    b'\x80\x04\x95\xe1\x01\x00\x00\x00\x00\x00\x00]\x94'
    b'(\x8c\x0epickle_dumps_b\x94\x8c\x04User\x94\x93\x94)'
    b'\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c'
    b'\x08lastname\x94\x8c\x06Watney\x94\x8c\x03age\x94K)\x8c'
    b'\x06groups\x94]\x94h\x01\x8c\x05Group\x94\x93\x94)\x81\x94}'
    b'\x94(\x8c\x03gid\x94K\x01\x8c\x04name\x94\x8c\x05users'
    b'\x94ubaubh\x03)\x81\x94}\x94(h\x06\x8c\x07Melissa\x94h'
    b'\x08\x8c\x05Lewis\x94h\nK(h\x0b]\x94(h\x0e)\x81\x94}\x94'
    b'(h\x11K\x01h\x12h\x13ubh\x0e)\x81\x94}\x94(h\x11K\x02h\x12\x8c'
    b'\x05staff\x94ubh\x0e)\x81\x94}\x94(h\x11K\x03h\x12\x8c'
    b'\x06admins\x94ubeubh\x03)\x81\x94}\x94(h\x06\x8c'
    b'\x04Rick\x94h\x08\x8c\x08Martinez\x94h\nK\'h\x0b]\x94h\x0e)'
    b'\x81\x94}\x94(h\x11K\x01h\x12h\x13ubaubh\x03)\x81\x94}\x94'
    b'(h\x06\x8c\x04Alex\x94h\x08\x8c\x05Vogel\x94h\nK(h\x0b]\x94ubh'
    b'\x03)\x81\x94}\x94(h\x06\x8c\x04Beth\x94h\x08\x8c\tJohanssen'
    b'\x94h\nK\x1dh\x0b]\x94(h\x0e)\x81\x94}\x94(h\x11K\x01h\x12h'
    b'\x13ubh\x0e)\x81\x94}\x94(h\x11K\x02h\x12h\x1dubeubh\x03)\x81'
    b'\x94}\x94(h\x06\x8c\x05Chris\x94h\x08\x8c\x04Beck\x94h\nK$h'
    b'\x0b]\x94h\x0e)\x81\x94}\x94(h\x11K\x01h\x12h\x13ubaube.'
)


class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

    def __repr__(self):
        return f'{self.gid}({self.name})'


class User:
    def __init__(self, firstname, lastname, age, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.groups = groups if groups else []

    def __repr__(self):
        clsname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        groups = ','.join(repr(x) for x in self.groups)
        age = self.age
        return f'{clsname}({firstname=}, {lastname=}, {age=}, {groups=})'


