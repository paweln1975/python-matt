
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
    >>> from pprint import pprint
    >>> from os import remove

    >>> pprint(result, sort_dicts=False)
    [{'firstname': 'Mark', 'lastname': 'Watney', 'group': 1},
     {'firstname': 'Melissa', 'lastname': 'Lewis', 'group': 3},
     {'firstname': 'Rick', 'lastname': 'Martinez', 'group': 1},
     {'firstname': 'Alex', 'lastname': 'Vogel', 'group': None},
     {'firstname': 'Beth', 'lastname': 'Johanssen', 'group': 2},
     {'firstname': 'Chris', 'lastname': 'Beck', 'group': 1}]

    >>> remove(FILE)
"""

import pickle

FILE = r'_temporary.pkl'

with open(FILE, mode='wb') as file:
    file.write(
        b'\x80\x04\x95\xca\x00\x00\x00\x00\x00\x00\x00]'
        b'\x94(}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94'
        b'\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x05group\x94K\x01u}'
        b'\x94(h\x02\x8c\x07Melissa\x94h\x04\x8c\x05Lewis\x94h\x06K\x03u}'
        b'\x94(h\x02\x8c\x04Rick\x94h\x04\x8c\x08Martinez\x94h\x06K\x01u}'
        b'\x94(h\x02\x8c\x04Alex\x94h\x04\x8c\x05Vogel\x94h\x06Nu}'
        b'\x94(h\x02\x8c\x04Beth\x94h\x04\x8c\tJohanssen\x94h\x06K\x02u}'
        b'\x94(h\x02\x8c\x05Chris\x94h\x04\x8c\x04Beck\x94h\x06K\x01ue.'
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


