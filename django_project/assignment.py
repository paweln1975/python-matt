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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> result
[<Role: Cleaner>, <Role: Trainer>]

>>> assert Role.objects.filter(name='Cleaner').delete()
>>> assert Role.objects.filter(name='Trainer').delete()


Hints:
`.create()`

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
import django; django.setup()
from demo.models import Role

result: Role

# English
# 0. Use `myproject.shop`
# 1. Define variable `result` with result of ORM call for
#    create a new `Customer`:
#    - firstname: John
#    - lastname: Doe
# 2. Use `.create()` method

# Polish
# 0. Użyj `myproject.shop`
# 1. Zdefiniuj zmienną `result` z wynikiem zapytania ORM dla
#    stworzenia nowego `Customer`:
#    - firstname: John
#    - lastname: Doe
# 2. Użyj metody `.create()`

# %% Result
roles_list = [
    Role(name='Cleaner', comment='Cleaner'),
    Role(name='Trainer', comment='Trainer')
]
result = Role.objects.bulk_create(roles_list)

