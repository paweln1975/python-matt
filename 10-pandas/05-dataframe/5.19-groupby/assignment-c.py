"""
Name: DataFrame Groupby AstronautTop10
Difficulty: medium
Lines: 5
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
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result.reset_index(drop=True)
                       name  flights
0   Chang-Diaz, Franklin R.        7
1            Ross, Jerry L.        7
2     Brown, Curtis L., Jr.        6
3         Foale, C. Michael        6
4          Krikalev, Sergei        6
5         Malenchenko, Yuri        6
6  Musgrave, Franklin Story        6
7       Wetherbee, James D.        6
8            Young, John W.        6

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = 'https://python3.info/_static/astro-selection.csv'

# English
# 1. Read data from `DATA`
# 2. Create ranking of astronauts with most fligts
# 3. Define `result: pd.Dataframe` with top 9
# 4. Sort by `flights` (descending) and `name` (ascending)
# 5. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA`
# 2. Stwórz ranking astronautów z największą liczbą lotów
# 3. Zdefiniuj `result: pd.Dataframe` z top 9
# 4. Posortuj po `flights` (malejąco) i `name` (rosnąco)
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...