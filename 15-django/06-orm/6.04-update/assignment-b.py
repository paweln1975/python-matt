"""
Name: Database ORM Create
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> assert result is not Ellipsis, \
'Assign your result to variable `result`'
>>> assert type(result) is int, \
'Variable `result` has invalid type, should be int'

>>> result
1

>>> john = Customer.objects.filter(firstname='John', lastname='Doe')
>>> jane = Customer.objects.filter(firstname='Jane', lastname='Doe')

>>> assert not john.exists()
>>> assert jane.exists()

>>> assert jane.delete()
>>> assert john.delete()

Hints:
`.filter()`
`.update()`

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from shop.models import Customer

result: int

Customer.objects.create(firstname='John', lastname='Doe')

# English
# 0. Use `myproject.shop`
# 1. Define variable `result` with result of ORM call for:
#    Update `Customer` firstname: John, lastname: Doe
#    Set firstname: Jane
# 2. Use `.update()` method

# Polish
# 0. Użyj `myproject.shop`
# 1. Zdefiniuj zmienną `result` z wynikiem zapytania ORM dla:
#    Zaktulizuj `Customer` firstname: John, lastname: Doe
#    Ustaw firstname: Jane
# 2. Użyj metody `.update()`

# %% Result
result = ...