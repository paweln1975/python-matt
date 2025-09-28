# %% About
# - Name: About EntryTest Endswith
# - Difficulty: easy
# - Lines: 6
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
# 1. Collect email addresses with domain listed in `DOMAINS`
# 2. Define variable `result: list[str]` with the result
# 3. Search for emails only in `DATA` -> `rows`
# 4. Run doctests - all must succeed

# %% Polish
# 1. Zbierz adresy email z domeną wylistowaną w `DOMAINS`
# 2. Zdefiniuj zmienną `result: list[str]` z wynikiem
# 3. Szukaj adresów email tylko w `DATA` -> `rows`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Example
# >>> result
# ['alice@example.com',
#  'bob@example.com',
#  'carol@example.com',
#  'dave@example.org']

# %% Why
# - Check if you can filter data
# - Check if you know string methods
# - Check if you know how to iterate over `list[dict]`

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'

>>> assert type(result) is list, \
'Result must be a list'

>>> assert len(result) > 0, \
'Result cannot be empty'

>>> assert all(type(element) is str for element in result), \
'All elements in result must be a str'

>>> from pprint import pprint
>>> result = sorted(result)
>>> pprint(result)
['alice@example.com',
 'bob@example.com',
 'carol@example.com',
 'mallory@example.net']
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -f -v myfile.py`

# %% Imports

# %% Types
result: list[str]

# %% Data
DATA = {
    'database': 'myapp',
    'table': 'users',
    'rows': [
        {'username': 'alice', 'email': 'alice@example.com'},
        {'username': 'bob', 'email': 'bob@example.com'},
        {'username': 'carol', 'email': 'carol@example.com'},
        {'username': 'dave', 'email': 'dave@example.org'},
        {'username': 'eve', 'email': 'eve@example.org'},
        {'username': 'mallory', 'email': 'mallory@example.net'},
    ]
}

DOMAINS = ('example.com', 'example.net')

# %% Result
users = DATA['rows']
result = [
    user['email']
    for user in users
    if user['email'].endswith(DOMAINS)
]