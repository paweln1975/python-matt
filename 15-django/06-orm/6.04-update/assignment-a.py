"""
Name: Database ORM Create
Difficulty: easy
Lines: 3
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

>>> assert result is not Ellipsis, \
'Assign your result to variable `result`'

>>> john = Person.objects.filter(firstname='John', lastname='Doe')
>>> jane = Person.objects.filter(firstname='Jane', lastname='Doe')

>>> assert not john.exists()
>>> assert jane.exists()

# >>> assert jane.delete()
# >>> assert john.delete()

Hints:
`.get()`
`.save()`

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
import django; django.setup()
from demo.models import Person

result: Person

Person.objects.create(firstname='John', lastname='Doe')

# English
# 0. Use `myproject.shop`
# 1. Using ORM get user:
#    firstname: John, lastname: Doe
# 2. Update his firstname to Jane
# 3. Use `.save()` method

# Polish
# 0. Użyj `myproject.shop`
# 1. Używając ORM znajdź użytkownika:
#    firstname: John, lastname: Doe
# 2. Zmień jego imię na Jane
# 3. Użyj metody `.save()`

# %% Result
result = Person.objects.get(firstname='John', lastname='Doe')
result.firstname = 'Jane'
result.save()
