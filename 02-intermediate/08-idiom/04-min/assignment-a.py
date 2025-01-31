# %% About
# - Name: Idiom Min Impl
# - Difficulty: easy
# - Lines: 1
# - Minutes: 2

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
# 1. Define variable `result: int` with calculated
#    number of elements from shorter list: `DATA1` and `DATA2`
# 2. Run doctests - all must succeed

# %% Polish
# 1. Zdefiniuj zmienną `result: int` z wyliczoną
#    liczbą elementów krótszej z list: `DATA1` i `DATA2`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Hints
# - `min()`
# - `len()`

# %% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result
3
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v myfile.py`

# %% Imports

# %% Types
result: int

# %% Data
DATA1 = ['Mark', 'Melissa', 'Rick', 'Alex']
DATA2 = ['Watney', 'Lewis', 'Martinez']

# %% Result
result = min(len(item) for item in [DATA1, DATA2])