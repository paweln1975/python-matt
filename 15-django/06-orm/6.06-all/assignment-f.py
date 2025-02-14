"""
Name: Database ORM All
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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> assert result is not Ellipsis, \
'Assign your result to variable `result`'

>>> from django.db.models.query import QuerySet
>>> assert type(result) is QuerySet, \
'Variable `result` has invalid type, should be QuerySet'

>>> from pprint import pprint
>>> pprint(result)
<QuerySet [('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Rick', 'Martinez'), ('Alex', 'Vogel'), ('Beth', 'Johanssen'), ('Chris', 'Beck')]>

Hints:
`.values_list()`

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from django.db.models import QuerySet
from shop.models import Customer

result: QuerySet

# English
# 0. Use `myproject.shop`
# 1. Define variable `result` with result of query:
#    Select `firstname` and `lastname` of all customers
# 2. Result should be a `QuerySet` of `list[tuple]`

# Polish
# 0. Użyj `myproject.shop`
# 1. Zdefiniuj zmienną `result` z wynikiem zapytania:
#    Wybierz `firstname` i `lastname` wszystkich klientów
# 2. Wynik powinien być jako `QuerySet` od `list[tuple]`

# %% Result
result = ...