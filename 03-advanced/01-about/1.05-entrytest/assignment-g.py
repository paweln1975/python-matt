# %% About
# - Name: About EntryTest ToListDict
# - Difficulty: easy
# - Lines: 2
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
# 1. Convert `DATA` from  `list[tuple]` to `list[dict]`
# 2. First row has column names (keys in result `dict`)
# 2. Define variable `result` with the result
# 3. Run doctests - all must succeed

# %% Polish
# 1. Przekonwertuj `DATA` z `list[tuple]` do `list[dict]`
# 2. Pierwszy wiersz ma nazwy kolumn (klucze w wynikowym `dict`)
# 3. Zdefiniuj zmienną `result` z wynikiem
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Example
# >>> result
# [{'firstname': 'Alice', 'lastname': 'Apricot', 'age': 30},
#  {'firstname': 'Bob', 'lastname': 'Blackthorn', 'age': 31},
#  {'firstname': 'Carol', 'lastname': 'Corn', 'age': 32},
#  {'firstname': 'Dave', 'lastname': 'Durian', 'age': 33},
#  {'firstname': 'Eve', 'lastname': 'Elderberry', 'age': 34},
#  {'firstname': 'Mallory', 'lastname': 'Melon', 'age': 15}]

# %% Why
# - Convert data from `list[tuple]` to `list[dict]`
# - `list[tuple]` is used to represent CSV data
# - `list[tuple]` is used to represent database rows
# - `list[dict]` is used to represent JSON data
# - CSV is the most popular format in data science

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> result = list(result)
>>> assert type(result) is list, \
'Result must be a list'

>>> assert len(result) > 0, \
'Result cannot be empty'

>>> assert all(type(element) is dict for element in result), \
'All elements in result must be a dict'

>>> from pprint import pprint
>>> pprint(result, sort_dicts=False)
[{'firstname': 'Alice', 'lastname': 'Apricot', 'age': 30},
 {'firstname': 'Bob', 'lastname': 'Blackthorn', 'age': 31},
 {'firstname': 'Carol', 'lastname': 'Corn', 'age': 32},
 {'firstname': 'Dave', 'lastname': 'Durian', 'age': 33},
 {'firstname': 'Eve', 'lastname': 'Elderberry', 'age': 34},
 {'firstname': 'Mallory', 'lastname': 'Melon', 'age': 15}]
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -f -v myfile.py`

# %% Imports

# %% Types
result: list[dict[str,str|int]]

# %% Data
DATA = [
    ('firstname', 'lastname', 'age'),
    ('Alice', 'Apricot', 30),
    ('Bob', 'Blackthorn', 31),
    ('Carol', 'Corn', 32),
    ('Dave', 'Durian', 33),
    ('Eve', 'Elderberry', 34),
    ('Mallory', 'Melon', 15),
]


# %% Result
header, *rows = DATA

result = [dict(zip(header, row)) for row in rows]
