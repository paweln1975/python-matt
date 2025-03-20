"""
Name: Functional Lambda Chain
Difficulty: easy
Lines: 2
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> type(result) is float
True
>>> result
245.0

Hints:
`mean = sum(...) / len(...)`
type cast to `list()` before calculating mean to expand generator

"""

# %% SetUp

result: float

def odd(x):
    return x % 2

def cube(x):
    return x ** 3

# English
# 1. Inline functions `odd()` and `cube()` with `lambda` expressions
# 2. Run doctests - all must succeed

# Polish
# 1. Zastąp funkcje `odd()` i `cube()` wyrażeniami `lambda`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = range(0,10)
result = filter(lambda x: x % 2, result)
result = map(lambda x: x ** 3, result)
result = list(result)
result = sum(result) / len(result)