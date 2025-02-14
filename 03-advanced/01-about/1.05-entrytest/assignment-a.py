"""
Name: About EntryTest ToListDict
Difficulty: easy
Lines: 2
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
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
[{'firstname': 'Mark', 'lastname': 'Watney', 'age': 41},
 {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 40},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'age': 39},
 {'firstname': 'Alex', 'lastname': 'Vogel', 'age': 40},
 {'firstname': 'Chris', 'lastname': 'Beck', 'age': 36},
 {'firstname': 'Beth', 'lastname': 'Johanssen', 'age': 29}]

Why:
Convert data from `list[tuple]` to `list[dict]`
`list[tuple]` is used to represent CSV data
`list[tuple]` is used to represent database rows
`list[dict]` is used to represent JSON data
CSV is the most popular format in data science

"""

# %% SetUp

result: list[dict[str,str|int]]

DATA = [
    ('firstname', 'lastname', 'age'),
    ('Mark', 'Watney', 41),
    ('Melissa', 'Lewis', 40),
    ('Rick', 'Martinez', 39),
    ('Alex', 'Vogel', 40),
    ('Chris', 'Beck', 36),
    ('Beth', 'Johanssen', 29),
]

# English
# 1. Define `result: list[dict]`:
# 2. Convert `DATA` from `list[tuple]` to `list[dict]`
#    - key - name from the header
#    - value - numerical value or species name
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[dict]`:
# 2. Przekonwertuj `DATA` z `list[tuple]` do `list[dict]`
#    - klucz - nazwa z nagłówka
#    - wartość - wartość numeryczna lub nazwa gatunku
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
headers, *row = DATA
result = dict(zip(headers, row))