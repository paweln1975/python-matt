"""
Name: Series Mapping Clean
Difficulty: medium
Lines: 15
Minutes: 13

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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
0    Pana Twardowskiego III
1    Pana Twardowskiego III
2    Pana Twardowskiego III
3    Pana Twardowskiego III
4    Pana Twardowskiego III
5    Pana Twardowskiego III
6    Pana Twardowskiego III
7    Pana Twardowskiego III
8    Pana Twardowskiego III
9    Pana Twardowskiego III
dtype: object

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = [
    'UL. Pana \tTWArdoWskIEGO 3',
    'ul Pana TwaRDOWSkiego III',
    '\tul. Pana Twardowskiego trzeciego',
    'ulicaPana Twardowskiego III',
    'Pana \nTWARDOWSKIEGO 3',
    'UL. Pana TWARDowsKIEGO III',
    'ULICA Pana TWARDOWSKIEGO III ',
    'ULICA. Pana TWARDowsKIEGO III',
    ' Pana Twardowskiego 3 ',
    'Pana\tTwardowskiego III ',
]

# English
# 1. Convert `DATA` to `pd.Series`
# 2. Write function to clean up data
# 3. Function takes one `str` argument
# 4. Function returns cleaned text
# 5. Apply function to all elements of `pd.Series`
# 6. Run doctests - all must succeed

# Polish
# 1. Przekonwertuj `DATA` do `pd.Series`
# 2. Napisz funkcję czyszczącą dane
# 3. Funkcja przyjmuje jeden argument typu `str`
# 4. Funkcja zwraca oczyszczony tekst
# 5. Zaaplikuj funkcję na wszystkich elementach `pd.Series`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def clean(text: str) -> str:
    ...

result = ...