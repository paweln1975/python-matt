

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

    >>> pprint(result)
    [User(firstname='Mark', lastname='Watney', group=1),
     User(firstname='Melissa', lastname='Lewis', group=3),
     User(firstname='Rick', lastname='Martinez', group=1),
     User(firstname='Alex', lastname='Vogel', group=None),
     User(firstname='Chris', lastname='Beck', group=1),
     User(firstname='Beth', lastname='Johanssen', group=2)]
"""

import pickle

FILE = r'_temporary.pkl'

DATA = (
    b'\x80\x04\x95\x06\x01\x00\x00\x00\x00\x00\x00]\x94'
    b'(\x8c\x0epickle_dumps_a\x94\x8c\x04User\x94\x93\x94)'
    b'\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c'
    b'\x08lastname\x94\x8c\x06Watney\x94\x8c\x05group\x94K\x01ubh\x03)'
    b'\x81\x94}\x94(h\x06\x8c\x07Melissa\x94h\x08\x8c\x05Lewis'
    b'\x94h\nK\x03ubh\x03)\x81\x94}\x94(h\x06\x8c\x04Rick\x94h'
    b'\x08\x8c\x08Martinez\x94h\nK\x01ubh\x03)\x81\x94}\x94'
    b'(h\x06\x8c\x04Alex\x94h\x08\x8c\x05Vogel\x94h\nNubh\x03)'
    b'\x81\x94}\x94(h\x06\x8c\x05Chris\x94h\x08\x8c\x04Beck\x94h'
    b'\nK\x01ubh\x03)\x81\x94}\x94(h\x06\x8c\x04Beth\x94h\x08\x8c'
    b'\tJohanssen\x94h\nK\x02ube.'
)

class User:
    def __init__(self, firstname, lastname, group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group

    def __repr__(self):
        clsname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        group = self.group
        return f'{clsname}({firstname=}, {lastname=}, {group=})'



