"""
Name: About Tutorial A
Difficulty: easy
Lines: 1
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
>>> from pprint import pprint

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is int, \
'Variable `result` has invalid type, should be int'

>>> pprint(result)
1

Why:
Warmup before entry test
Verify that environment is set up correctly
Learn how to run doctests
Learn how to use IDE test runner
Learn how to read doctests output
Learn how to compare doctests output with results

"""

# %% SetUp

result: int

# English
# 1. Define variable `result` with value 1
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z wartością 1
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...