"""
Name: Database ORM Create
Difficulty: easy
Lines: 3
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> result
<Customer: John Doe>

>>> assert Customer.objects.filter(firstname='John', lastname='Doe').delete()

Hints:
`.get_or_create()`

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from shop.models import Customer

result: Customer

# English
# 0. Use `myproject.shop`
# 1. Define variable `result` with result of ORM call for
#    getting `Customer` or create a new one if not exist:
#    - firstname: John
#    - lastname: Doe
# 2. Create instance and use `.get_or_create()` method
# 3. Mind, that method returns a two element tuple
#    but we need only a `Customer`

# Polish
# 0. Użyj `myproject.shop`
# 1. Zdefiniuj zmienną `result` z wynikiem zapytania ORM dla
#    wyciągnięcia `Customer` lub stworzniem nowego jak nie istnieje:
#    - firstname: John
#    - lastname: Doe
# 2. Stwórz instancję modelu i użyj metodę `.get_or_create()`
# 3. Zwróć uwagę, że metoda zwraca dwu elementową tuplę
#    a potrzebny jest tylko `Customer`

# %% Result
result = ...