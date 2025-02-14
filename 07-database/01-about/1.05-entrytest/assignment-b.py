"""
Name: About EntryTest ToListTuple
Difficulty: easy
Lines: 5
Minutes: 5

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 12), \
'Python 3.12+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> result = list(result)
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert len(result) > 0, \
'Variable `result` should not be empty'
>>> assert all(type(row) is tuple for row in result), \
'Variable `result` should be a list[tuple]'

>>> from pprint import pprint
>>> pprint(result)
[('firstname', 'lastname', 'age'),
 ('Mark', 'Watney', 41),
 ('Melissa', 'Lewis', 40),
 ('Rick', 'Martinez', 39),
 ('Alex', 'Vogel', 40),
 ('Chris', 'Beck', 36),
 ('Beth', 'Johanssen', 29)]

Why:
Convert data from `list[dict]` to `list[tuple]`
`list[dict]` is used to represent JSON data
`list[tuple]` is used to represent CSV data
`list[tuple]` is used to represent database rows
JSON is the most popular format in web development

"""

# %% SetUp

type header = tuple[str,...]
type row = tuple[float,float,float,float,str]
result: list[header|row]

DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney', 'age': 41},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 40},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'age': 39},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'age': 40},
    {'firstname': 'Chris', 'lastname': 'Beck', 'age': 36},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'age': 29},
]

# English
# 1. Load `DATA` from `list[dict]` format (similar to JSON)
# 2. Convert data to `result: list[tuple]`
# 3. Add header as a first line
# 4. Run doctests - all must succeed

# Polish
# 1. Wczytaj `DATA` z formatu `list[dict]` (podobny do JSON)
# 2. Przekonwertuj dane do `result: list[tuple]`
# 3. Dodaj nagłówek jako pierwszą linię
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...