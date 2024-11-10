"""
* Assignment: Pickle Dump list[dict]
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

DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney', 'group': 1},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'group': 3},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'group': 1},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'group': None},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'group': 2},
    {'firstname': 'Chris', 'lastname': 'Beck', 'group': 1},
]

# Write `DATA` to `FILE`
# Use `pickle` module
...

