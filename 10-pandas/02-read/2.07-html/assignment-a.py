"""
Name: Pandas Read HTML
Difficulty: easy
Lines: 2
Minutes: 5

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
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result['Name']
0      Samantha Cristoforetti
1             Alexander Gerst
2            Andreas Mogensen
3              Luca Parmitano
4              Thomas Pesquet
5             Matthias Maurer
6             Rosemary Coogan
7               Sophie Adenot
8     Pablo Álvarez Fernández
9            Raphaël Liégeois
10               Marco Sieber
Name: Name, dtype: object

Hints:
`pip install --upgrade lxml`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/european-astronaut-corps.html'

# English
# 1. Read data from `DATA` as `data: pd.DataFrame`
# 2. Define `result` with active European Space Agency astronauts
# 3. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `data: pd.DataFrame`
# 2. Zdefiniuj `result` z aktywnymi astronautami Europejskiej Agencji Kosmicznej
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...