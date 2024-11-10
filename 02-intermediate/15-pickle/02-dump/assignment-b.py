"""
* Assignment: Pickle Dump list[tuple]
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Write `DATA` to `FILE`
    2. Use `pickle` module
    3. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do `FILE`
    2. Użyj modułu `pickle`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from os import remove

    >>> with open(FILE, mode='rb') as file:
    ...     result = pickle.load(file)

    >>> pprint(result)
    [('Mark', 'Watney', 1),
     ('Melissa', 'Lewis', 3),
     ('Rick', 'Martinez', 1),
     ('Alex', 'Vogel', None),
     ('Chris', 'Beck', 1),
     ('Beth', 'Johanssen', 2)]

    >>> remove(FILE)
"""

import pickle

FILE = r'_temporary.pkl'

DATA = [
    ('Mark', 'Watney', 1),
    ('Melissa', 'Lewis', 3),
    ('Rick', 'Martinez', 1),
    ('Alex', 'Vogel', None),
    ('Chris', 'Beck', 1),
    ('Beth', 'Johanssen', 2),
]

# Write `DATA` to `FILE`
# Use `pickle` module
...

