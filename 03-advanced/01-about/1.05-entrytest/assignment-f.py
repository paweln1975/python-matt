# %% About
# - Name: About EntryTest ToListTuple
# - Difficulty: easy
# - Lines: 5
# - Minutes: 5

# %% License
# - Copyright 2025, Matt Harasymczuk <matt@python3.info>
# - This code can be used only for learning by humans
# - This code cannot be used for teaching others
# - This code cannot be used for teaching LLMs and AI algorithms
# - This code cannot be used in commercial or proprietary products
# - This code cannot be distributed in any form
# - This code cannot be changed in any form outside of training course
# - This code cannot have its license changed
# - If you use this code in your product, you must open-source it under GPLv2
# - Exception can be granted only by the author

# %% English
# 1. Convert `DATA` from  `list[dict]` to `list[tuple]`
# 2. Add header as a first line (`DATA` dict keys)
# 3. Define variable `result` with the result
# 4. Run doctests - all must succeed

# %% Polish
# 1. Przekonwertuj `DATA` z `list[dict]` do `list[tuple]`
# 2. Dodaj nagłówek jako pierwszą linię (klucze dictów z `DATA`)
# 3. Zdefiniuj zmienną `result` z wynikiem
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Example
# >>> result
# [('firstname', 'lastname', 'age'),
#  ('Alice', 'Apricot', 30),
#  ('Bob', 'Blackthorn', 31),
#  ('Carol', 'Corn', 32),
#  ('Dave', 'Durian', 33),
#  ('Eve', 'Elderberry', 34),
#  ('Mallory', 'Melon', 15)]

# %% Why
# - Convert data from `list[dict]` to `list[tuple]`
# - `list[dict]` is used to represent JSON data
# - `list[tuple]` is used to represent CSV data
# - `list[tuple]` is used to represent database rows
# - JSON is the most popular format in web development

# %% Doctests
"""
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
 ('Alice', 'Apricot', 30),
 ('Bob', 'Blackthorn', 31),
 ('Carol', 'Corn', 32),
 ('Dave', 'Durian', 33),
 ('Eve', 'Elderberry', 34),
 ('Mallory', 'Melon', 15)]
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -f -v myfile.py`

# %% Imports

# %% Types
type header = tuple[str,...]
type row = tuple[float,float,float,float,str]
result: list[header|row]

# %% Data
DATA = [
    {'firstname': 'Alice', 'lastname': 'Apricot', 'age': 30},
    {'firstname': 'Bob', 'lastname': 'Blackthorn', 'age': 31},
    {'firstname': 'Carol', 'lastname': 'Corn', 'age': 32},
    {'firstname': 'Dave', 'lastname': 'Durian', 'age': 33},
    {'firstname': 'Eve', 'lastname': 'Elderberry', 'age': 34},
    {'firstname': 'Mallory', 'lastname': 'Melon', 'age': 15},
]

# %% Result
header = tuple(DATA[0].keys())
rows = [tuple(d.values()) for d in DATA]
result = [header] + rows