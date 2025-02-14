"""
Name: DataFrame Join
Difficulty: medium
Lines: 25
Minutes: 21

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

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

# >>> assert result is not Ellipsis, \
# 'Assign result to variable: `result`'
# >>> assert type(result) is pd.DataFrame, \
# 'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
Ellipsis

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

# English

# Polish
# 1. Na podstawie podanych URL:
#    - https://www.worldspaceflight.com/bios/eva/eva.php
#    - https://www.worldspaceflight.com/bios/eva/eva2.php
#    - https://www.worldspaceflight.com/bios/eva/eva3.php
#    - https://www.worldspaceflight.com/bios/eva/eva4.php
# 2. Scrapuj stronę wykorzystując `pandas.read_html()`
# 3. Połącz dane wykorzystując `pd.concat`
# 4. Przygotuj plik `CSV` z danymi dotyczącymi spacerów kosmicznych
# 5. Zapisz dane do pliku
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...