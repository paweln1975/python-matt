# %% About
# - Name: Idiom Product Generate
# - Difficulty: easy
# - Lines: 1
# - Minutes: 3

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
# 1. Define variable `result` with generated test data
# 2. Use `itertools.product()` function
# 3. Run doctests - all must succeed

# %% Polish
# 1. Zdefiniuj zmienną `result` z wygenerowanymi danymi testowymi
# 2. Użyj funkcji `itertools.product()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'

>>> assert type(result) is product, \
'Variable `result` has invalid type, should be product'

>>> result = list(result)

>>> from pprint import pprint
>>> pprint(result, width=72, sort_dicts=False)
[('Mark', 'Watney', 'botanist'),
 ('Mark', 'Watney', 'commander'),
 ('Mark', 'Watney', 'pilot'),
 ('Mark', 'Lewis', 'botanist'),
 ('Mark', 'Lewis', 'commander'),
 ('Mark', 'Lewis', 'pilot'),
 ('Mark', 'Martinez', 'botanist'),
 ('Mark', 'Martinez', 'commander'),
 ('Mark', 'Martinez', 'pilot'),
 ('Melissa', 'Watney', 'botanist'),
 ('Melissa', 'Watney', 'commander'),
 ('Melissa', 'Watney', 'pilot'),
 ('Melissa', 'Lewis', 'botanist'),
 ('Melissa', 'Lewis', 'commander'),
 ('Melissa', 'Lewis', 'pilot'),
 ('Melissa', 'Martinez', 'botanist'),
 ('Melissa', 'Martinez', 'commander'),
 ('Melissa', 'Martinez', 'pilot'),
 ('Rick', 'Watney', 'botanist'),
 ('Rick', 'Watney', 'commander'),
 ('Rick', 'Watney', 'pilot'),
 ('Rick', 'Lewis', 'botanist'),
 ('Rick', 'Lewis', 'commander'),
 ('Rick', 'Lewis', 'pilot'),
 ('Rick', 'Martinez', 'botanist'),
 ('Rick', 'Martinez', 'commander'),
 ('Rick', 'Martinez', 'pilot')]
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v myfile.py`

# %% Imports
from itertools import product

# %% Types
result: product

# %% Data
FIRSTNAMES = ['Mark', 'Melissa', 'Rick']
LASTNAMES = ['Watney', 'Lewis', 'Martinez']
ROLES = ['botanist', 'commander', 'pilot']

# %% Result
result = product(FIRSTNAMES, LASTNAMES, ROLES)