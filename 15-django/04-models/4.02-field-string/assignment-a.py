"""
Name: Django Model String
Difficulty: easy
Lines: 5
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

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _

Person: type

# English
# 0. Use `myproject.demo`
# 1. Create model `Person`
# 2. Add field `lastname` as `models.CharField`:
#    - verbose_name=_('Lastname')
#    - max_length=30
#    - null=False
#    - blank=False
#    - db_index=True
# 3. Add method `__str__` which returns `lastname`
# 4. Add class `Meta` with:
#    - app_label = 'demo'
#    - verbose_name = _('Person')
#    - verbose_name_plural = _('People')
#    - ordering = ['lastname']
# 5. Use `gettext_lazy`
# 6. Run `makemigrations`
# 7. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Stwórz model `Person`
# 2. Dodaj pole `lastname` jako `models.CharField`:
#    - verbose_name=_('Lastname')
#    - max_length=30
#    - null=False
#    - blank=False
#    - db_index=True
# 3. Dodaj metodę `__str__` która zwraca `lastname`
# 4. Dodaj klasę `Meta` z:
#    - app_label = 'demo'
#    - verbose_name = _('Person')
#    - verbose_name_plural = _('People')
#    - ordering = ['lastname']
# 5. Użyj `gettext_lazy`
# 6. Uruchom `makemigrations`
# 7. Uruchom `migrate`

# - `Create model Person`
# - `Applying demo.0001_initial... OK`

# %% Result
class Person(models.Model):
    lastname = models.CharField(verbose_name=_('Lastname'), max_length=30, null=False, blank=False, db_index=True)

    def __str__(self):
        return self.lastname

    class Meta:
        app_label = 'demo'
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        ordering = ['lastname']