# Zamienić User i Group na User i Group
"""
* Assignment: Pandas Read PythonObj
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Non-functional requirements:
        a. Use `,` to separate mission fields
        b. Use `;` to separate groups
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z DATA jako result: pd.DataFrame
    2. Wymagania niefunkcjonalne:
        a. Użyj `,` do oddzielania pól mission
        b. Użyj `;` do oddzielenia groups
    2. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Hints:
    * `vars(obj)`
    * dict.pop()
    * Nested `for`
    * `str.join(';', sequence)`
    * `str.join(',', sequence)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` has invalid type, should be `pd.DataFrame`'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname  lastname           groups
    0      Mark    Watney          1,users
    1   Melissa     Lewis  1,users;2,staff
    2      Rick  Martinez
"""

import pandas as pd


class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = list(groups) if groups else []


class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name


DATA = [
    User('Mark', 'Watney', groups=[
        Group(1, 'users')]),

    User('Melissa', 'Lewis', groups=[
        Group(1, 'users'),
        Group(2, 'staff')]),

    User('Rick', 'Martinez', groups=[]),
]


# Convert DATA to list[dict], then flatten
# type: list[dict]
data = ...

# Convert `data` to DataFrame
# type: pd.DataFrame
result = ...

