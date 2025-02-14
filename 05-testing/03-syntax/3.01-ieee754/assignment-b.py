"""
Name: Math IEEE754 IntFix
Difficulty: easy
Lines: 3
Minutes: 2

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result
0.3

"""

# %% SetUp

candy: int
cookie: int
result: float

CENT = 1
DOLLAR = 100*CENT

# English
# 1. Define variables with prices:
#    - candy = 0.10 USD
#    - cookie = 0.20 USD
# 2. Define `result: float` with sum of prices for a candy and a cookie
# 3. Fix precision error from IEEE-754
# 4. Use `int` type for that reason
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienne z cenami:
#    - cukierek (candy) = 0,10 USD
#    - ciasteczko (cookie) = 0,20 USD
# 2. Zdefiniuj `result: float` z sumą cen za ciasteczko i cukierek
# 3. Uwzględnij poprawkę na błąd precyzji wynikający z IEEE-754
# 4. W tym celu wykorzystaj typ `int`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
candy = ...
cookie = ...
result = ...