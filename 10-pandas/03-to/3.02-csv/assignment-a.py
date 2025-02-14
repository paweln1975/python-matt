"""
Name: DataFrame Export CSV
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
>>> from os import remove

>>> result = open(FILE).read()
>>> remove(FILE)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be `str`'

>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
,Event
135,LM lunar landing.
136,LM powered descent  engine cutoff.
137,Decision made to  proceed with EVA prior to first rest period.
138,Preparation for EVA  started.
139,EVA started (hatch  open).
140,CDR completely outside  LM on porch.
141,Modular equipment  stowage assembly deployed (CDR).
142,First clear TV picture  received.
143,"CDR at foot of ladder (starts to report, then pauses to listen)."
144,CDR at foot of ladder and described surface as almost like a powder.
145,1st step  taken lunar surface (CDR). That's one small step for a man...one giant leap  for mankind.
<BLANKLINE>

"""

# %% SetUp

import pandas as pd

DATA = 'https://python3.info/_static/apollo11.html'
FILE = r'_temporary.csv'

# English
# 1. Export data from column `Event` to file the `FILE`
# 2. Data has to be in CSV format
# 3. Run doctests - all must succeed

# Polish
# 1. Wyeksportuj dane z kolumny `Event` do pliku `FILE`
# 2. Dane mają być w formacie CSV
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = (pd
  .read_html(DATA, header=0)[0]
  .head(n=146)
  .tail(n=11)
)