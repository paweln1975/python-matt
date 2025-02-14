"""
Name: Random Select Sample
Difficulty: easy
Lines: 1
Minutes: 3

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

>>> sorted(result)
[3, 17, 25, 27, 32, 33]

"""

# %% SetUp

from random import sample, seed

result: list[int]

seed(0)

# English
# 1. Define `result: list[int]` with 6 random
#    integers without repetition in range from 1 to 49 (inclusive)
# 2. Use `random.sample()`
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[int]` z 6-oma losowymi
#    i nie powtarzającymi się liczbami całkowitymi
#    z zakresu od 1 do 49 (włącznie)
# 2. Użyj `random.sample()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...