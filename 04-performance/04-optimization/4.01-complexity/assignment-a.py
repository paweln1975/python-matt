"""
Name: Performance Complexity Segmentation
Difficulty: easy
Lines: 10
Minutes: 8

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
'Assign your result to variable `result`'
>>> assert type(result) is dict, \
'Variable `result` has invalid type, should be dict'

>>> assert all(type(x) is str for x in result.keys())
>>> assert all(type(x) is int for x in result.values())

>>> result
{'small': 16, 'medium': 19, 'large': 15}

"""

# %% SetUp

result: dict[str,int]

DATA = [
    1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
    0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
    2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
    1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
    4, 8, 1, 9, 6, 3,
]

# English
# 1. Count number from `DATA` by the category:
#    - 'small' - number between 0 and 3 (lower included, upper excluded)
#    - 'medium' - number between 3 and 7 (lower included, upper excluded)
#    - 'large' - number between 7 and 10 (lower included, upper excluded)
# 2. Run doctests - all must succeed

# Polish
# 1. Zlicz liczby z `DATA` ze względu na kategorię:
#    - 'small' - liczba pomiędzy 0 i 3 (dolny włącznie, górny rozłącznie)
#    - 'medium' - liczba pomiędzy 3 i 7 (dolny włącznie, górny rozłącznie)
#    - 'large' - liczba pomiędzy 7 i 10 (dolny włącznie, górny rozłącznie)
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = {'small': 0, 'medium': 0, 'large': 0}