"""
Name: Database ORM Filter
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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> assert result is not Ellipsis, \
'Assign your result to variable `result`'

>>> from django.db.models.query import QuerySet
>>> assert type(result) is Person, \
'Variable `result` has invalid type, should be Person'

>>> result
<Person: Chris Beck>

>>> Person.objects.all().delete()
(6, {'demo.Person': 6})

>>> Person.objects.all().count()
0

Hints:
`.filter()`

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
import django; django.setup()
from django.db.models import QuerySet
from demo.models import Person

persons = [
    Person(firstname='Mark', lastname='Watney'),
    Person(firstname='Melissa', lastname='Lewis'),
    Person(firstname='Rick', lastname='Martinez'),
    Person(firstname='Alex', lastname='Vogel'),
    Person(firstname='Beth', lastname='Johanssen'),
    Person(firstname='Chris', lastname='Beck'),
]

Person.objects.bulk_create(persons)
result: QuerySet

# Polish
# 0. Użyj `myproject.shop`
# 1. Zdefiniuj zmienną `result` z wynikiem zapytania ORM dla:
#    Wybierz pierwszego klienta
# 2. Nie używaj metody `first()`


# %% Result
result = Person.objects.all()[0]

