"""
Name: Database ORM Orders
Difficulty: medium
Lines: 6
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> assert result is not Ellipsis, \
'Assign your result to variable `result`'
>>> assert type(result) is dict, \
'Variable `result` has invalid type, should be dict'
>>> assert type(result['country']) is str, \
'Variable `result["country"]` has invalid type, should be str'
>>> assert type(result['count']) is int, \
'Variable `result["count"]` has invalid type, should be int'

>>> from pprint import pprint
>>> pprint(result, sort_dicts=True)
{'count': 29, 'country': 'USA'}

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from django.db.models import Count, F
from shop.models import Order

result: dict[str, str|int]

# English
# 0. Use `myproject.shop`
# 1. Display data which answers the following question:
#    Amount and country name,
#    from which people did the most purchases

# Polish
# 0. Użyj `myproject.shop`
# 1. Wyświetl dane odpowiadające na pytanie:
#    Kwota i nazwa kraju,
#    którego obywatele dokonali najwięcej zakupów

# %% Result
result = ...