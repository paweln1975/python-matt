# %% About
# - Name: Idiom Permutations Generate
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
# 2. Use `itertools.permutations()` function
# 3. Run doctests - all must succeed

# %% Polish
# 1. Zdefiniuj zmienną `result` z wygenerowanymi danymi testowymi
# 2. Użyj funkcji `itertools.permutations()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'

>>> assert type(result) is permutations, \
'Variable `result` has invalid type, should be permutations'

>>> result = list(result)

>>> from pprint import pprint
>>> pprint(result, width=72, sort_dicts=False)
[('login', 'edit_profile', 'logout'),
 ('login', 'logout', 'edit_profile'),
 ('edit_profile', 'login', 'logout'),
 ('edit_profile', 'logout', 'login'),
 ('logout', 'login', 'edit_profile'),
 ('logout', 'edit_profile', 'login')]
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v myfile.py`

# %% Imports
from itertools import permutations

# %% Types
result: permutations

# %% Data
ACTIONS = ['login', 'edit_profile', 'logout']

# %% Result
result = permutations(ACTIONS)