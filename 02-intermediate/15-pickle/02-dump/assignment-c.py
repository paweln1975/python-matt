
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> with open(FILE, mode='rb') as file:
...     result = pickle.load(file)

>>> from os import remove
>>> remove(FILE)

>>> from pprint import pprint
>>> pprint(result, sort_dicts=False)
[{'firstname': 'Mark', 'lastname': 'Watney', 'group': 1},
 {'firstname': 'Melissa', 'lastname': 'Lewis', 'group': 3},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'group': 1},
 {'firstname': 'Alex', 'lastname': 'Vogel', 'group': None},
 {'firstname': 'Beth', 'lastname': 'Johanssen', 'group': 2},
 {'firstname': 'Chris', 'lastname': 'Beck', 'group': 1}]
"""
# endregion

# region Show Imports
import pickle
# endregion

FILE = r'_temporary.pkl'
DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney', 'group': 1},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'group': 3},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'group': 1},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'group': None},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'group': 2},
    {'firstname': 'Chris', 'lastname': 'Beck', 'group': 1},
]

# English
# 1. Write `DATA` to `FILE`
# 2. Use `pickle` module
# 3. Run doctests - all must succeed

# Polish
# 1. Zapisz `DATA` do `FILE`
# 2. Użyj modułu `pickle`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

pickle.dump(DATA, open(FILE, 'wb'))
